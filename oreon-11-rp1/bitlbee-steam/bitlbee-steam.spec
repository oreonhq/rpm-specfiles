%global source0_hash 716bab07dfba5254c8f07d0cd5e29a1a9e6da3e31cdad63803897f814d403f62

Name:           bitlbee-steam
Version:        1.4.2
Release:        19%{?dist}
Summary:        Steam protocol plugin for BitlBee

License:        GPLv2+
URL:            https://github.com/bitlbee/bitlbee-steam
Source0:        https://github.com/bitlbee/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  bitlbee-devel
BuildRequires:  glib2-devel
BuildRequires:  libgcrypt-devel
BuildRequires: make

Requires:       bitlbee%{?_isa}

%global __provides_exclude_from ^%{_libdir}/bitlbee/.*

%description
The Steam protocol plugin for BitlBee.  This plugin uses the Steam Mobile
API allowing it to run alongside the main Steam client.  It is worth
noting that the Steam Mobile API is HTTP based, which does lead to mild
latency.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install
rm $RPM_BUILD_ROOT/%{_libdir}/bitlbee/steam.la

%files
%license COPYING
%doc AUTHORS README
%{_libdir}/bitlbee/steam.so

%changelog
%autochangelog
