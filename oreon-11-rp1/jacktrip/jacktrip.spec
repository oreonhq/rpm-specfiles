%global source0_hash fab31a8d96c89702252f3436bdc4d8d27a23226b0af2a20e133f55f52ded904d
Name:           jacktrip
Version:        3.0.1
Release:        1%{?dist}
Summary:        A system for high-quality audio network performance over the Internet
License:        MIT and GPL-3.0-or-later and LGPL-3.0-only
URL:            https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%ifarch aarch64 x86_64
%endif
Requires:       hicolor-icon-theme
Obsoletes:      jacktrip-doc < 1.4.0
# oreon:deps
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  hicolor-icon-theme
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6NetworkAuth)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickControls2)
BuildRequires:  pkgconfig(Qt6ShaderTools)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6WebSockets)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(rtaudio)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  python3-jinja2
BuildRequires:  python3-pyyaml
# /oreon:deps
%description
JackTrip is a Linux and Mac OS X-based system used for multi-machine
network performance over the Internet. It supports any number of
channels (as many as the computer/network can handle) of
bidirectional, high quality, uncompressed audio signal steaming.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dbuildinfo="$(cat /etc/redhat-release)" \
%ifnarch aarch64 x86_64
    -Dnovs=true \
%endif
    -Dnoupdater=true \
    -Drtaudio=enabled \
    -Dlibsamplerate=enabled
%meson_build
%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
