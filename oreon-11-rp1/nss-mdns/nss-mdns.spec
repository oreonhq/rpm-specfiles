%global source0_hash ddf71453d7a7cdc5921fe53ef387b24fd0c3c49f4dcf94a2a437498596761a21

Name:           nss-mdns
Version:        0.15.1
Release:        %autorelease
Summary:        glibc plugin for .local name resolution
License:        LGPL-2.1-or-later
URL:            https://github.com/avahi/nss-mdns
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

Patch1:         nss-mdns-local-heuristic.patch
Patch2:         nss-mdns-local-heuristic-unit.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(check)
Requires:       (avahi if systemd)
Requires(preun,posttrans): authselect

%description
nss-mdns is a plugin for the GNU Name Service Switch (NSS) functionality of
the GNU C Library (glibc) providing host name resolution via Multicast DNS
(aka Zeroconf, aka Apple Rendezvous, aka Apple Bonjour), effectively allowing
name resolution by common Unix/Linux programs in the ad-hoc mDNS domain .local.

nss-mdns provides client functionality only, which means that you have to
run a mDNS responder daemon separately from nss-mdns if you want to register
the local host name via mDNS (e.g. Avahi).


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%configure
%make_build

%check
%make_build check || (R=$?; cat ./test-suite.log; exit $R)

%install
%make_install

%posttrans
authselect enable-feature with-mdns4 > /dev/null || :

%preun
authselect disable-feature with-mdns4 > /dev/null || :

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md NEWS.md ACKNOWLEDGEMENTS.md
%{_libdir}/libnss_mdns*.so.2*


%changelog
%autochangelog
