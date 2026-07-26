%global source0_hash ae19ed11dbbdb5a0474f2e69b6eacf9125eeaf765ccc1e4075124b732d91843b

%global srcname UxPlay

Name:           uxplay
Version:        1.73.3
Release:        %autorelease
Summary:        AirPlay Unix mirroring server

License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/FDH2/UxPlay
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Do not use vendored llhttp library
Patch:          uxplay-unvendor-llhttp.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  dbus-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  libplist-devel
BuildRequires:  llhttp-devel
BuildRequires:  openssl-devel

Recommends:     %{name}-beacon = %{version}-%{release}
Recommends:     avahi
Recommends:     gstreamer1-plugin-libav
Recommends:     gstreamer1-plugins-base
Recommends:     gstreamer1-plugins-good
Recommends:     gstreamer1-plugins-bad-free
Recommends:     gstreamer1-vaapi

# Vendored under lib/playfair, provenance and modifications are unclear
Provides:       bundled(playfair)

%description
An AirPlay2 Mirror and AirPlay2 Audio (but not Video) server that provides
screen-mirroring (with audio) of iOS/MacOS clients in a display window on
the server host (which can be shared using a screen-sharing application);
Apple Lossless Audio (ALAC) (e.g.,iTunes) can be streamed from client to
server in non-mirror mode.

%package        beacon
Summary:        Bluetooth LE beacon for UxPlay service discovery
Requires:       python3-gobject
Requires:       python3-psutil

%description    beacon
This package provides a standalone Bluetooth LE beacon to support UxPlay
service discovery on networks that do not allow the user to run a DNS_SD
service.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

# Drop vendored library
rm -r lib/llhttp

%build
%cmake -DNO_MARCH_NATIVE=ON
%cmake_build

%install
%cmake_install

# Remove duplicate docs
rm -r %{buildroot}%{_pkgdocdir}

%files
%license LICENSE lib/playfair/LICENSE.md
%doc README.md
%{_bindir}/uxplay
%{_mandir}/man1/uxplay.1*

%files beacon
%license LICENSE
%{_bindir}/uxplay-beacon.py
%{_mandir}/man1/uxplay-beacon.1*

%changelog
%autochangelog
