%global source0_hash 16177e5c3935d604257c6708e82d03ed3681ad00b3ec20a02b8da38df601ff76
Name:       utox
Version:    0.18.1
Release:        1%{?dist}
Summary:        The lightweight Tox client
License:    LicenseRef-Callaway-MIT OR GPL-3.0-or-later
URL:        https://github.com/uTox/uTox/
Source0:        https://github.com/uTox/uTox//archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{name}.appdata.xml
Source2:    third_party.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(filteraudio)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(toxcore)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
# /oreon:deps
%description
%summary

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n uTox-%{version}
%autosetup -N -T -D -a 2 -n uTox-%{version}

%build

%cmake -DCMAKE_BUILD_TYPE="Release"
%cmake_build
%install
%cmake_install
install -Dp -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml
rm -rf %{buildroot}/%{_datadir}/icons/hicolor/14x14
%oreon_autofiles main

%check

%ifnarch %{arm}
%ctest
%endif
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
