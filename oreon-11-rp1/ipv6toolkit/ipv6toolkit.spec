%global source0_hash b6a1af3d3cf417a81dbb4cd99cf710d16a62338be4bfbbb14b8d1cb298849338
Summary:        Security assessment and troubleshooting tools for IPv6 protocols
Name:           ipv6toolkit
Version:        2.2
Release:        1%{?dist}
License:        GPL-3.0-or-later AND GFDL-1.3-no-invariants-or-later AND MPL-2.0
URL:            https://www.si6networks.com/research/tools/ipv6toolkit/
Source0:        https://github.com/fgont/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       curl
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  perl(Crypt::X509)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Net::IP)
BuildRequires:  perl(Socket)
BuildRequires:  perl(constant)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The SI6 Networks IPv6 toolkit is a suite of IPv6 security assessment and
troubleshooting tools. It can be used to assess the security of IPv6
networks, evaluate the resilience of IPv6 devices by subjecting them to
real-world attacks, and troubleshoot IPv6 networking issues. The toolkit
comprises tools ranging from packet-crafting tools for sending arbitrary
Neighbor Discovery packets to a comprehensive IPv6 network scanning tool.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
for file in *.TXT; do mv -f ${file} $(basename ${file} .TXT); done

%build

export CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
%make_build PREFIX=%{_prefix}
%install
%make_install PREFIX=%{_prefix} MANPREFIX=%{_datadir} \
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
  SBINPATH=$RPM_BUILD_ROOT%{_sbindir}
%oreon_autofiles main
%endif
%check

make unit_tests
for tool in tools/*; do if grep -q -E '^#!/.*perl' ${tool}; then perl -c ${tool}; fi; done
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
