%global source0_hash ecfb0d1c9e6b3968c2e62d1cbf0e8a513b20cefe2b2d091a27f943b63c53004e

Summary:        Facebook protocol plugin for BitlBee
Name:           bitlbee-facebook
Version:        1.2.2
Release:        14%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/bitlbee/bitlbee-facebook
Source0:        https://github.com/bitlbee/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(bitlbee) >= 3.4
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.14.0
# Tests
# script(1) comes from somewhere in the overall util-linux* package mess
BuildRequires:  %{_bindir}/script

%description
The Facebook protocol plugin for BitlBee. This plugin uses the Facebook
Mobile API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/bitlbee/facebook.la

%check
echo -e "[settings]\nRunMode = Inetd\nPluginDir = $RPM_BUILD_ROOT%{_libdir}/bitlbee/" > bitlbee.conf
script -c 'timeout --preserve-status --signal=TERM 5s bitlbee -c bitlbee.conf' -e -f check.log -q
! grep -q 'Error: ' check.log || { cat check.log; exit 1; }  # Any other BitlBee error during startup?

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/bitlbee/facebook.so

%changelog
%autochangelog
