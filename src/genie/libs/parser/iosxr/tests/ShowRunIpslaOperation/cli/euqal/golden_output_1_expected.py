expected_output = {
  "ipsla": {
    "operations": {
      "operation_ids": [
        {
          "oper_id": 100,
          "oper_types": {
            "type": {
              "name": "udp jitter",
              "vrf": "VRF-1",
              "src_addr": "1.1.1.1",
              "dest_addr": "2.2.2.2",
              "packet": {
                "count": 1000,
                "interval": 20
              },
              "time_out": 3000,
              "data_size_req": 500,
              "dest_port": 15000,
              "frequency": 60,
              "verify-data": true
            }
          }
        }
      ]
    }
  }
}