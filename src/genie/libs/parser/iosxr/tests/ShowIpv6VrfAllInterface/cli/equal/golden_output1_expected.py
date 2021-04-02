expected_output = {
    "GigabitEthernet0/0/0/0": {
        "enabled": True,
        "int_status": "shutdown",
        "ipv6": {
            "2001:db8:1:1::1/64": {
                "ipv6": "2001:db8:1:1::1",
                "ipv6_prefix_length": "64",
                "ipv6_status": "tentative",
                "ipv6_subnet": "2001:db8:1:1::",
            },
            "2001:db8:2:2::2/64": {
                "ipv6": "2001:db8:2:2::2",
                "ipv6_prefix_length": "64",
                "ipv6_status": "tentative",
                "ipv6_subnet": "2001:db8:2:2::",
            },
            "2001:db8:3:3:a8aa:bbff:feff:8888/64": {
                "ipv6": "2001:db8:3:3:a8aa:bbff:feff:8888",
                "ipv6_eui64": True,
                "ipv6_prefix_length": "64",
                "ipv6_status": "tentative",
                "ipv6_subnet": "2001:db8:3:3::",
            },
            "2001:db8:4:4::4/64": {
                "ipv6": "2001:db8:4:4::4",
                "ipv6_prefix_length": "64",
                "ipv6_route_tag": "10",
                "ipv6_status": "tentative",
                "ipv6_subnet": "2001:db8:4:4::",
            },
            "complete_glean_adj": "0",
            "complete_protocol_adj": "0",
            "dad_attempts": "1",
            "dropped_glean_req": "0",
            "dropped_protocol_req": "0",
            "icmp_redirects": "disabled",
            "icmp_unreachables": "enabled",
            "incomplete_glean_adj": "0",
            "incomplete_protocol_adj": "0",
            "ipv6_groups": ["ff02::2", "ff02::1"],
            "ipv6_link_local": "fe80::a8aa:bbff:feff:8888",
            "ipv6_link_local_state": "tentative",
            "ipv6_mtu": "1600",
            "ipv6_mtu_available": "1586",
            "nd_adv_retrans_int": "0",
            "nd_cache_limit": "1000000000",
            "nd_dad": "enabled",
            "nd_reachable_time": "0",
            "stateless_autoconfig": True,
            "table_id": "0xe0800011",
        },
        "ipv6_enabled": False,
        "oper_status": "down",
        "vrf": "VRF1",
        "vrf_id": "0x60000002",
    },
    "GigabitEthernet0/0/0/0.10": {
        "enabled": True,
        "int_status": "shutdown",
        "ipv6": {
            "2001:db8:1:3::1/64": {
                "ipv6": "2001:db8:1:3::1",
                "ipv6_prefix_length": "64",
                "ipv6_subnet": "2001:db8:1:3::",
            },
            "complete_glean_adj": "0",
            "complete_protocol_adj": "0",
            "dad_attempts": "1",
            "dropped_glean_req": "0",
            "dropped_protocol_req": "0",
            "icmp_redirects": "disabled",
            "icmp_unreachables": "enabled",
            "incomplete_glean_adj": "0",
            "incomplete_protocol_adj": "0",
            "ipv6_groups": [
                "ff02::1:ff00:1",
                "ff02::1:ffa6:78c5",
                "ff02::2",
                "ff02::1",
            ],
            "ipv6_link_local": "fe80::5054:ff:fea6:78c5",
            "ipv6_mtu": "1514",
            "ipv6_mtu_available": "1500",
            "nd_adv_duration": "160-240",
            "nd_adv_retrans_int": "0",
            "nd_cache_limit": "1000000000",
            "nd_dad": "enabled",
            "nd_reachable_time": "0",
            "nd_router_adv": "1800",
            "stateless_autoconfig": True,
            "table_id": "0xe0800000",
        },
        "ipv6_enabled": False,
        "oper_status": "down",
        "vrf": "default",
        "vrf_id": "0x60000000",
    },
    "GigabitEthernet0/0/0/1": {
        "enabled": True,
        "int_status": "up",
        "ipv6": {
            "2001:db8:1:5::1/64": {
                "ipv6": "2001:db8:1:5::1",
                "ipv6_prefix_length": "64",
                "ipv6_subnet": "2001:db8:1:5::",
            },
            "complete_glean_adj": "1",
            "complete_protocol_adj": "1",
            "dad_attempts": "1",
            "dropped_glean_req": "0",
            "dropped_protocol_req": "0",
            "icmp_redirects": "disabled",
            "icmp_unreachables": "enabled",
            "incomplete_glean_adj": "0",
            "incomplete_protocol_adj": "0",
            "ipv6_groups": [
                "ff02::1:ff00:1",
                "ff02::1:ff78:ebe0",
                "ff02::2",
                "ff02::1",
            ],
            "ipv6_link_local": "fe80::5054:ff:fe78:ebe0",
            "ipv6_mtu": "1514",
            "ipv6_mtu_available": "1500",
            "nd_adv_duration": "160-240",
            "nd_adv_retrans_int": "0",
            "nd_cache_limit": "1000000000",
            "nd_dad": "enabled",
            "nd_reachable_time": "0",
            "nd_router_adv": "1800",
            "stateless_autoconfig": True,
            "table_id": "0xe0800010",
        },
        "ipv6_enabled": True,
        "oper_status": "up",
        "vrf": "VRF1",
        "vrf_id": "0x60000001",
    },
    "GigabitEthernet0/0/0/2": {
        "enabled": True,
        "int_status": "up",
        "ipv6": {
            "2001:db8:20:1:5::1/64": {
                "ipv6": "2001:db8:20:1:5::1",
                "ipv6_prefix_length": "64",
                "ipv6_subnet": "2001:db8:20:1::",
            },
            "complete_glean_adj": "2",
            "complete_protocol_adj": "0",
            "dad_attempts": "1",
            "dropped_glean_req": "0",
            "dropped_protocol_req": "0",
            "icmp_redirects": "disabled",
            "icmp_unreachables": "enabled",
            "incomplete_glean_adj": "0",
            "incomplete_protocol_adj": "0",
            "ipv6_groups": [
                "ff02::1:ff00:1",
                "ff02::1:ff15:c05c",
                "ff02::2",
                "ff02::1",
            ],
            "ipv6_link_local": "fe80::5054:ff:fe15:c05c",
            "ipv6_mtu": "1514",
            "ipv6_mtu_available": "1500",
            "nd_adv_duration": "160-240",
            "nd_adv_retrans_int": "0",
            "nd_cache_limit": "1000000000",
            "nd_dad": "enabled",
            "nd_reachable_time": "0",
            "nd_router_adv": "1800",
            "stateless_autoconfig": True,
            "table_id": "0xe0800011",
        },
        "ipv6_enabled": True,
        "oper_status": "up",
        "vrf": "VRF2",
        "vrf_id": "0x60000002",
    },
    "GigabitEthernet0/0/0/3": {
        "enabled": False,
        "int_status": "up",
        "ipv6_enabled": True,
        "oper_status": "up",
        "vrf": "default",
        "vrf_id": "0x60000000",
    },
    "GigabitEthernet0/0/0/4": {
        "enabled": False,
        "int_status": "up",
        "ipv6_enabled": True,
        "oper_status": "up",
        "vrf": "default",
        "vrf_id": "0x60000000",
    },
    "GigabitEthernet0/0/0/5": {
        "enabled": False,
        "int_status": "shutdown",
        "ipv6_enabled": False,
        "oper_status": "down",
        "vrf": "default",
        "vrf_id": "0x60000000",
    },
    "GigabitEthernet0/0/0/6": {
        "enabled": False,
        "int_status": "shutdown",
        "ipv6_enabled": False,
        "oper_status": "down",
        "vrf": "default",
        "vrf_id": "0x60000000",
    },
    "MgmtEth0/0/CPU0/0": {
        "enabled": False,
        "int_status": "shutdown",
        "ipv6_enabled": False,
        "oper_status": "down",
        "vrf": "default",
        "vrf_id": "0x60000000",
    },
}
