#!/usr/bin/env python3
import dns.resolver


def query_dns_records(domain_name):
    """
    Function to fetch dns records

    Args:
        domain_name(string):

    Returns:
        dns information like A, AAAA, MX, NS, TXT, etc
    """
    record_type = ["A", "AAAA", "MX", "NS", "TXT", "SOA"]
    result = {}
    resolver = dns.resolver.Resolver()
    for record in record_type:
        try:
            result[record] = resolver.resolve(
                    domain_name,
                    record
            )
        except (
            dns.resolver.NoAnswer,
            dns.resolver.NXDOMAIN,
            dns.resolver.NoNameservers
        ):
            pass
    return result


if __name__ == "__main__":
    import sys
    domain_name = sys.argv[1]
    results = query_dns_records(domain_name)
    for record_type, response_text in results.items():
        print(f"\n{record_type} Records:")
        print(response_text.response.to_text())
    print("\nResults dictionary:", results)
