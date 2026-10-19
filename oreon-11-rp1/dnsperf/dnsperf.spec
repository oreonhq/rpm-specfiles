%global source0_hash 134ba69744705bdb65ea57e25713300a6771f7cecbd5d6a74dd9472c18ac2696
%bcond_with    python3
%global forgeurl0 https://codeberg.org/DNS-OARC/dnsperf
Summary:        Benchmarking authorative and recursing DNS servers
Name: dnsperf
Version: 2.14.0
Release:        1%{?dist}
License: Apache-2.0
Url: https://www.dns-oarc.net/tools/dnsperf
Vcs: git:%{forgeurl0}
Source0:        https://www.dns-oarc.net/files/dnsperf/%{name}-%{version}.tar.gz
Source2: dnsperf-data
%if %{with python3}
%endif
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
Recommends: gnuplot
%else
Requires:   gnuplot
%endif
%if %{with python3}
%endif
Provides: %{name}-data = %{version}-%{release}
Obsoletes: %{name}-data < 2.5.1-2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ck-devel
BuildRequires:  gcc
BuildRequires:  ldns-devel
BuildRequires:  libnghttp2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  python3-dns
BuildRequires:  python3-pcapy
# /oreon:deps
%description
This is dnsperf, a collection of DNS server performance testing tools.
For more information, see the dnsperf(1) and resperf(1) man pages.

%if %{with python3}
%package queryparse
Summary: Pcap dns query extraction utility
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
%if %{with python3}
Requires: python3-pcapy python3-dns
%endif
%description queryparse
This is dnsperf, a collection of DNS server performance testing tools.

Provides queryparse, python utility extracting queries from pcap files,
such as recorded by tcpdump or wireshark. Prints output in format
useable by dnsperf and resperf.

%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fi
%configure
%make_build
%if %{with python3}
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} -p -n contrib/queryparse/queryparse
%endif
%install
%make_install dist_doc_DATA=''
%if %{with python3}
install -p contrib/queryparse/queryparse %{buildroot}/%{_bindir}
install -D -m 644 -p contrib/queryparse/queryparse.1 %{buildroot}/%{_mandir}/man1/queryparse.1
gzip %{buildroot}/%{_mandir}/man1/queryparse.1
%endif
mkdir -p %{buildroot}%{_datadir}/%{name}
touch %{buildroot}%{_datadir}/%{name}/queryfile-example-current
install -m 755 -p %{SOURCE2} %{buildroot}%{_bindir}/dnsperf-data
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build check
%if %{with python3}
%{buildroot}/%{_bindir}/queryparse --version
%endif
%files -f %{oreon_filedir}/main.list
%files -n dnsperf-queryparse -f %{oreon_filedir}/dnsperf-queryparse.list

%changelog

%autochangelog
