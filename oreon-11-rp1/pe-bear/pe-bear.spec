%global source3_hash b740899234c847dae7162084471fcc392d1d6b5c7f04a2ed2e874a34bf2cbe34
%global source2_hash e1384f39c013751b9b644119cce06e66a5ee3af88257cfe8fcc3dd443d79a3fa
%global source1_hash 428f3ff1cdefdb7b270ce1250ecaa73be3555f35dec392530db1940f6a171785
%global source0_hash 8f98d0c99bc34db8943ab1ccbe256db7ae3ca798251fcbb48d06a1711c41ba20
%global appname PE-bear
%global commit1 e2bfabf5d8c4b9c47596853be50260f8841b21ed
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})
%global commit2 80ede42453ce5717c1808cad512a4410fcb9df5a
%global shortcommit2 %(c=%{commit2}; echo ${c:0:7})
%global commit3 1ac3b1a55c00a8f685d5bf2a722045e5bc49d1b6
%global shortcommit3 %(c=%{commit3}; echo ${c:0:7})
Name: pe-bear
Version: 0.7.2
Release:        1%{?dist}
License: GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause
Summary:        Portable Executable analyzing tool with a friendly GUI
URL: https://github.com/hasherezade/%{name}
Source0:        https://github.com/hasherezade/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: https://github.com/hasherezade/bearparser/archive/%{commit1}/bearparser-%{shortcommit1}.tar.gz
Source2: https://github.com/capstone-engine/capstone/archive/%{commit2}/capstone-%{shortcommit2}.tar.gz
Source3: https://github.com/hasherezade/sig_finder/archive/%{commit3}/sig_finder-%{shortcommit3}.tar.gz
Provides: bundled(bearparser) = 0.5~git%{shortcommit1}
Provides: bundled(capstone) = 5.0~git%{shortcommit2}
Provides: bundled(sig_finder) = 0~git%{shortcommit3}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
# /oreon:deps
%description
PE-bear is a multiplatform analyzing tool for PE (Portable Executable)
files. Its objective is to deliver fast and flexible "first view" for
malware analysts, stable and capable to handle malformed PE files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Unpacking submodules...
tar -xf %{SOURCE1} -C bearparser --strip=1
tar -xf %{SOURCE2} -C capstone --strip=1
tar -xf %{SOURCE3} -C sig_finder --strip=1

%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DRELATIVE_LIBS:BOOL=OFF \
    -DSHOW_CONSOLE:BOOL=OFF \
    -DUSE_QT4:BOOL=OFF \
    -DUSE_QT5:BOOL=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
