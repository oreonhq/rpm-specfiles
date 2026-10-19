%global source0_hash 37f878899a525443bc11e847b234640e094ca2924a115e994d1c9e8a7eed9360
%undefine __cmake_in_source_build
Name:           seadrive-gui
Version:        3.0.18
Release:        1%{?dist}
Summary:        GUI part of Seafile Drive client
License:        Apache-2.0 AND MIT AND OFL-1.1
URL:            https://seafile.com
Source0:        https://github.com/haiwen/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        seadrive.appdata.xml
Patch:          seadrive-gui-3.0.13-CMake-4.x-compatibility.patch
ExclusiveArch:  %{qt6_qtwebengine_arches}
Provides:       bundled(QtAwesome)
Provides:       bundled(fontawesome-fonts) = 3.2.1
Requires:       hicolor-icon-theme
Requires:       seadrive-daemon = %{version}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libsearpc)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
# /oreon:deps
%description
Seafile is a next-generation open source cloud storage system, with advanced
support for file syncing, privacy protection and teamwork.

Seafile allows users to create groups with file syncing, wiki, and discussion
to enable easy collaboration around documents within a team.

This package contains the GUI part of Seafile Drive client. The Drive client
enables you to access files on the server without syncing to local disk.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# ensure that these don't affect the build
rm -rf third_party/{CrawlScopeCommandLine,MPMessagePack.framework,WinSparkle-0.5.3}

%build

%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build
%install
%cmake_install
install -D -m 644 -pv %{SOURCE1} %{buildroot}%{_metainfodir}/seadrive.appdata.xml
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/seadrive.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/seadrive.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
