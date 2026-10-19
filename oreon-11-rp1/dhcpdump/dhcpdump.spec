%global source2_hash c459c03d0ae871d59b60255303bb972a3ece8ff4a4a63a1f8c90229f64234ecf
%global source1_hash 26fb3024cd55c2324bf6117a99cf5012ddadee812766a5901b603076dfcb527b
%global source0_hash 41c79aa975662f33b1b7acaa0ab4c071b654cc78166c6475e82e3f0cfbe4b009
Name:           dhcpdump
Version:        2.00
Release:        1%{?dist}
Summary:        Parse DHCP packets
License:        BSD-2-Clause
URL:            https://github.com/bbonev/%{name}
Source0:        https://github.com/bbonev/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/bbonev/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://raw.githubusercontent.com/bbonev/%{name}/v%{version}/debian/upstream/signing-key.asc
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  perl-podlators
# /oreon:deps
%description
A utility to analyze sniffed DHCP packets.

%global _hardened_build 1

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%make_build
%install
install -D -p -m 755 -t %{buildroot}%{_bindir} %{name}
install -D -p -m 644 -t %{buildroot}%{_mandir}/man8/ %{name}.8
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
