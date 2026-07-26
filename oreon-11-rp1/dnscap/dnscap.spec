%global source0_hash 3ce7cbb09d497ff40f74a21bdb12cee72e20ebd38d5c9fa7beff94dee4a2f10c

%global filesurl https://www.dns-oarc.net/files/%{name}
Name:           dnscap
Version:        2.5.2
Release:        1%{?dist}
Summary:        Network capture utility designed specifically for DNS traffic
License:        BSD-3-Clause AND ISC
URL:            https://www.dns-oarc.net/tools/dnscap
Source:         %{filesurl}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libpcap-devel
BuildRequires:  ldns-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  perl-YAML
BuildRequires:  cryptopant-devel
BuildRequires:  pkgconfig
BuildRequires:  lz4-devel
BuildRequires:  bzip2-devel
BuildRequires:  libzstd-devel
BuildRequires:  xz-devel

%description
dnscap is a network capture utility designed specifically for DNS
traffic. It produces binary data in pcap(3) format. This utility
is similar to tcpdump(1), but has a number of features tailored
to DNS transactions and protocol options.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

%build
autoreconf -fsi
%configure

# Most dnscap plugins are linked against libraries that are not actually used by them.
# https://docs.fedoraproject.org/en-US/package-maintainers/CommonRpmlintIssues/#unused_direct_shlib_dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
%make_install
rm -f %{buildroot}/%{_docdir}/%{name}/LICENSE

%check
%make_build test

%files
%{_libdir}/%{name}/
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*
%license LICENSE
%doc CONTRIBUTORS CHANGES README.md

%changelog
%autochangelog
