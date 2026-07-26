%global source0_hash fa830d91b993d15f8a463c8dd68f7106f0dded87928bec36074de934c2c52f73

Summary:        Scan for mDNS/DNS-SD services published on the local network
Name:           mdns-scan
Version:        0.5
Release:        14%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/alteholz/mdns-scan/
Source0:        https://github.com/alteholz/mdns-scan/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         mdns-scan-0.5-typo.patch
BuildRequires:  make
BuildRequires:  gcc

%description
mdns-scan is a tool for scanning for mDNS/DNS-SD services published on
the local network. It works by issuing a mDNS PTR query to the special
RR _services._dns-sd._udp.local for retrieving a list of all currently
registered services on the local link.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .typo

%build
%make_build CFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%make_install
install -D -p -m 0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
