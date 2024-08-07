import unittest
from unittest.mock import patch, MagicMock
import ids

class TestIDS(unittest.TestCase):

    @patch('ids.sniff')
    def test_start_sniffing(self, mock_sniff):
        ids.start_sniffing('test_interface')
        mock_sniff.assert_called_once_with(iface='test_interface', prn=ids.packet_callback, store=0)

    def test_packet_callback(self):
        packet = MagicMock()
        packet.haslayer.return_value = True
        packet.getlayer.return_value.src = '192.168.1.1'
        packet.getlayer.return_value.dport = 80

        initial_total_packets = ids.traffic_stats['total_packets']

        ids.packet_callback(packet)

        self.assertEqual(ids.traffic_stats['total_packets'], initial_total_packets + 1)
        self.assertIn('192.168.1.1', ids.traffic_stats['udp_traffic'])

    @patch('ids.logging.info')
    def test_check_udp_flood(self, mock_logging):
        ip_layer = MagicMock()
        ip_layer.src = '192.168.1.1'
        ip_layer.dst = '192.168.1.2'  # Specify a destination IP
        udp_layer = MagicMock()
        udp_layer.dport = 80

        ids.traffic_stats['udp_traffic']['192.168.1.1'] = 11
        ids.check_udp_flood(ip_layer, udp_layer)
        mock_logging.assert_called_once_with('UDP Flood Alert: 192.168.1.1 -> 192.168.1.2 (Port: 80)')

if __name__ == '__main__':
    unittest.main()
