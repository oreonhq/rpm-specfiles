%global source0_hash 3658ac21cc33e79e72bed070454e49c543017991cb6c37f4253c85e9176869d1

Name:           dhcpdump
Version:        1.9
Release:        8%{?dist}
Summary:        Parse DHCP packets

License:        BSD-2-Clause
URL:            https://github.com/bbonev/%{name}
Source0:        https://github.com/bbonev/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/bbonev/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://raw.githubusercontent.com/bbonev/%{name}/v%{version}/debian/upstream/signing-key.asc

BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  perl-podlators
BuildRequires:  gnupg2

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

%files
%license LICENSE
%doc CHANGES CONTACT
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
%autochangelog
