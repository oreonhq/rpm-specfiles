%global source0_hash 58c7737dd27e1a69b326afa2fca99f9921557fd17dc47cd6acb144245496a5d4

Name:           jacktrip
Version:        2.7.2
Release:        %autorelease
Summary:        A system for high-quality audio network performance over the Internet

License:        MIT and GPL-3.0-or-later and LGPL-3.0-only
URL:            https://github.com/%{name}/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson, gcc-c++
BuildRequires:  python3-pyyaml, python3-jinja2
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(rtaudio)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  dbus-devel
BuildRequires:  help2man
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6NetworkAuth)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickControls2)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6ShaderTools)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6WebSockets)
%ifarch aarch64 x86_64
BuildRequires:  pkgconfig(Qt6WebEngineCore)
BuildRequires:  pkgconfig(Qt6WebChannel)
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme
Obsoletes:      jacktrip-doc < 1.4.0

%description
JackTrip is a Linux and Mac OS X-based system used for multi-machine
network performance over the Internet. It supports any number of
channels (as many as the computer/network can handle) of
bidirectional, high quality, uncompressed audio signal steaming.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

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

%check
%meson_test

%files
%doc README.md
%license LICENSE.md LICENSES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/org.jacktrip.JackTrip.desktop
%{_metainfodir}/org.jacktrip.JackTrip.metainfo.xml

%changelog
%autochangelog
