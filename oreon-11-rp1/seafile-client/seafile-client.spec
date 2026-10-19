%global source0_hash f1768f9ff0c19a61911fd8f55a39c024ece5fe2caa1cf6f4ddfa4bf465c0b231
%global _hardened_build 1
Name:           seafile-client
Version:        9.0.16
Release:        1%{?dist}
Summary:        Seafile cloud storage desktop client
License:        Apache-2.0 AND MIT AND OFL-1.1
URL:            https://www.seafile.com/
Source0:        https://github.com/haiwen/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        seafile.appdata.xml
Patch:          https://github.com/haiwen/seafile-client/pull/1506.patch#/Add-ENABLE_LOG_UPLOADER-CMake-option.patch
Patch:          seafile-client-qt-6.9-missing-includes.patch
ExclusiveArch:  %{qt6_qtwebengine_arches}
Provides:       bundled(QtAwesome)
Provides:       bundled(fontawesome-fonts) = 3.2.1
Requires:       seafile = %{version}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libseafile)
BuildRequires:  pkgconfig(libsearpc)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Seafile is a next-generation open source cloud storage system, with advanced
support for file syncing, privacy protection and teamwork.

Seafile allows users to create groups with file syncing, wiki, and discussion
to enable easy collaboration around documents within a team.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# ensure that these third-party sources are not used during the build
rm -rf third_party/{WinSparkle-0.5.3,quazip}

%build

%cmake \
    -DCMAKE_BUILD_TYPE:STRING=Release \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.10 \
    -DBUILD_LOG_UPLOADER:BOOL=OFF     \
    -DBUILD_SHIBBOLETH_SUPPORT:BOOL=ON
%cmake_build
%install
%cmake_install
install -D -m 644 -pv %{SOURCE1} %{buildroot}%{_metainfodir}/seafile.appdata.xml
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/seafile.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
