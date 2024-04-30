expected_output = {
    "sslproxy_statistics": {
        "connection_statistics": {
            "total_connections": 2989,
            "proxied_connections": 1872,
            "non_proxied_connections": 1036,
            "clear_connections": 0,
            "active_proxied_connections": 6,
            "active_non_proxied_connections": 0,
            "active_clear_connections": 0,
            "max_conc_proxied_connections": 143,
            "max_conc_non_proxied_connections": 43,
            "max_conc_clear_connections": 0,
            "tunneled_proxied_connections": 0,
            "tunneled_non_proxied_connections": 0,
            "active_tunneled_proxied_flows": 0,
            "active_tunneled_non_proxied_flows": 0,
            "max_conc_tunneled_proxied_flows": 0,
            "max_conc_tunneled_non_proxied_flows": 0,
            "ssl_encrypted_marked_non_ssl_flows": 0,
            "total_closed_connections": 2983,
        },
        "non_proxied_connection_reasons": {
            "unsupported_cipher": 0,
            "unsupported_ssl_version": 0,
            "non_ssl_traffic": 0,
            "memory_allocation_failure": 0,
            "memory_access_failure": 0,
            "handshake_unsupported": 0,
            "ssl_parse_failure": 0,
            "ssl_error": 0,
            "unexpected_packet": 0,
            "ism_state_error": 0,
            "exception": 0,
            "endpoint_alert": 0,
            "fin_rst_received_during_handshake": 0,
            "pushdown_by_sc": 0,
            "ism_flow_create_failure": 0,
            "pushdown_default": 0,
        },
        "dropped_connection_reasons": {
            "unsupported_ssl_version": 0,
            "unsupported_cipher": 0,
            "untrusted_certificate": 0,
            "unable_to_get_proxy_certificate": 0,
            "expired_certificate": 0,
            "ocsp_cert_verification_failure": 0,
            "handshake_unsupported": 0,
            "endpoint_alert": 0,
            "fin_rst_received_during_handshake": 81,
            "read_in_invalid_state": 0,
            "invalid_fsm_event_received": 0,
            "invalid_msg_type_rcvd_from_ism_de": 0,
            "event_received_in_wrong_state": 0,
            "ism_key_packet_send_fail": 0,
            "ism_flow_create_failure": 0,
            "failed_to_load_key_in_de": 0,
            "invalid_peer_segment": 0,
            "fail_to_get_orig_ch_during_pushdown": 0,
            "decrypt_encrypt_failure": 0,
            "rst_rcvd_during_ps_pc_key_pending": 0,
            "no_ssl_record_in_flow_segment": 0,
            "memory_allocation_failure": 0,
            "memory_access_failure": 0,
            "abort_on_ssl_parse_failure": 0,
            "invalid_ssl_record_header": 0,
            "unable_to_send_hs_message_to_ism": 0,
            "fail_to_get_memory_from_pool_in_ism": 0,
        },
        "alert_generated": {"c2s": 0, "s2c": 0},
        "alert_received": {"c2s": 0, "s2c": 0},
        "connection_closure_statistics": {
            "c2s": {
                "fin_received_at_ps": 1762,
                "fin_rec_after_ssl_handshake_at_ps": 897,
                "fin_rec_during_ssl_handshake_at_ps": 188,
                "fin_rec_for_non_ssl_conn_at_ps": 677,
                "fin_sent_to_sc_from_ps": 1681,
                "fin_received_at_pc_from_sc": 0,
                "fin_sent_to_server": 1830,
                "rst_generated_by_ps": 257,
                "rst_received_at_ps": 372,
                "rst_sent_to_sc_from_ps": 629,
                "rst_received_at_pc_from_sc": 0,
                "rst_sent_to_server": 1163,
                "close_notify_received_at_ps": 2,
                "close_notify_fin_sent_to_sc_from_ps": 0,
                "close_notify_fin_rec_at_pc_from_sc": 0,
                "close_notify_sent_to_server": 0,
            },
            "s2c": {
                "fin_received_at_pc": 0,
                "fin_rec_after_ssl_handshake_at_pc": 0,
                "fin_rec_during_ssl_handshake_at_pc": 0,
                "fin_rec_for_non_ssl_conn_at_pc": 0,
                "fin_sent_to_sc_from_pc": 1820,
                "fin_received_at_ps_from_sc": 791,
                "fin_sent_to_client": 1791,
                "rst_generated_by_pc": 257,
                "rst_received_at_pc": 1082,
                "rst_sent_to_sc_from_pc": 1163,
                "rst_received_at_ps_from_sc": 29,
                "rst_sent_to_client": 1192,
                "close_notify_received_at_pc": 0,
                "close_notify_fin_sent_to_sc_from_pc": 0,
                "close_notify_fin_rec_at_ps_from_sc": 1000,
                "close_notify_sent_to_client": 1000,
            },
        },
        "proxy_server": {
            "lwssl_flow_create": 2989,
            "lwssl_flow_delete": 2983,
            "lfs_mem_alloc_failure": 0,
            "fin_generated_by_sc": 0,
            "rst_generated_by_sc": 1163,
            "close_notify_sent": 0,
        },
        "proxy_client": {
            "lwssl_flow_create": 2989,
            "lwssl_flow_delete": 2983,
            "lfs_mem_alloc_failure": 0,
            "fin_generated_by_sc": 0,
            "rst_generated_by_sc": 1163,
            "close_notify_sent": 0,
        },
        "ism": {
            "ism_flow_create": 0,
            "ism_flow_delete": 0,
            "ism_fifo_enqueue_failed": 0,
            "ism_sem_post_failed": 0,
            "lwssl_failed_to_send_msg": 0,
            "lwssl_mem_alloc_failed_for_ism_msg": 0,
        },
        "resource_manager": {
            "session_alloc_success": 0,
            "session_alloc_failures": 0,
            "session_free_success": 0,
            "session_free_failures": 0,
        },
        "oscp_statistics": {
            "app_statistics": {
                "ocsp_requests": 0,
                "ocsp_responses": 0,
                "ocsp_timeouts": 0,
                "ocsp_failures": 0,
                "ocsp_good_responses": 0,
                "ocsp_revoked_responses": 0,
                "ocsp_unknown_responses": 0,
                "ocsp_internal_errors": 0,
            },
            "client_statistics": {
                "ocsp_requests": 0,
                "ocsp_responses": 0,
                "ocsp_timeouts": 0,
                "ocsp_failures": 0,
                "ocsp_good_responses": 0,
                "ocsp_revoked_responses": 0,
                "ocsp_unknown_responses": 0,
                "ocsp_internal_errors": 0,
            },
        },
        "oscp_stapling": {
            "ocsp_stapling_requests": 0,
            "ocsp_stapling_responses": 0,
            "ocsp_stapling_valid_responses": 0,
            "ocsp_stapling_revoked_responses": 0,
            "ocsp_stapling_unknown_responses": 0,
            "ocsp_response_validation_failure": 0,
        },
        "ssl_statistics": {
            "flow_requested_ssl_tls_version": {
                "ssl_v2_flows": 0,
                "ssl_v3_flows": 0,
                "tls_1.0_flows": 0,
                "tls_1.1_flows": 0,
                "tls_1.2_flows": 0,
                "tls_1.3_flows": 0,
            },
            "flow_selected_ssl_tls_version": {
                "tls_1.0_flows": 0,
                "tls_1.1_flows": 0,
                "tls_1.2_flows": 0,
                "tls_1.3_flows": 0,
            },
            "client_hello_extensions": {
                "pushdown": 0,
                "bypass": 0,
                "strip": 0,
                "process": 0,
            },
            "ssl_handshake_statistics": {
                "ssl_handshakes_started": 0,
                "ssl_handshakes_completed": 0,
                "full_ssl_handshakes": 0,
                "ssl_renegotiation": 0,
                "ssl_resumption": 0,
                "ssl_resumption_session_id": 0,
                "ssl_resumption_session_tkt": 0,
                "ssl_fallback_to_full_hs": 0,
                "ssl_failed_renego": 0,
                "ssl_server_cert_validation_reqs": 0,
                "ssl_server_cert_validation_success": 0,
                "server_cert_verify_failed_expired": 0,
                "server_cert_verify_failed_untrusted": 0,
                "ssl_client_cert_validation_reqs": 0,
                "ssl_client_cert_validation_success": 0,
                "client_cert_verify_failed_expired": 0,
                "client_cert_verify_failed_untrusted": 0,
                "revocation_check_requests": 0,
                "revocation_check_good_response": 0,
            },
            "policy_statistics": {
                "drop": {
                    "expired_certificate": 0,
                    "failure_mode": 0,
                    "unknown_status": 0,
                    "unsupported_cipher_suites": 0,
                    "unsupported_protocol_versions": 0,
                    "untrusted_certificate": 0,
                },
                "decrypt": {
                    "expired_certificate": 0,
                    "failure_mode": 0,
                    "unknown_status": 0,
                    "untrusted_certificate": 0,
                },
                "no_decrypt": {
                    "unsupported_cipher_suites": 0,
                    "unsupported_protocol_versions": 0,
                },
            },
        },
        "packet_counters": {
            "proxy_server": {
                "from_client": 8736,
                "to_sc": 8586,
                "from_sc": 16635,
                "to_client": 18553,
            },
            "proxy_client": {
                "from_server": 0,
                "to_sc": 0,
                "from_sc": 0,
                "to_server": 0,
            },
            "clear_packets": {
                "proxy_server": {
                    "from_client": 1590,
                    "to_sc": 1590,
                    "from_sc": 3977,
                    "to_client": 3977,
                },
                "proxy_client": {
                    "from_server": 0,
                    "to_sc": 0,
                    "from_sc": 0,
                    "to_server": 0,
                },
            },
            "dropped_packets": {"c2s_wcapi_deny_packet": 0, "s2c_wcapi_deny_packet": 0},
        },
    }
}

