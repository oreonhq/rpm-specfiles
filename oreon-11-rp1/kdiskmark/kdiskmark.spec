%global source0_hash f0c5d695d3566b36ef86eda1286edc5b4cb1c3d447ec5a4d36c6878e79cea113
ExcludeArch: %{ix86}
%global singleapplication_commit f1e15081dc57a9c03f7f4f165677f18802e1437a
%global singleapplication_shortcommit %(c=%{singleapplication_commit}; echo ${c:0:7})
Name: kdiskmark
Version: 3.3.0
Release:        1%{?dist}
Summary:        Simple open-source disk benchmark tool for Linux distros
License: GPL-3.0-or-later
URL: https://github.com/JonMagon/KDiskMark
Source0:        https://github.com/JonMagon/KDiskMark/archive/%{version}/%{name}-%{version}.tar.gz
Requires: fio%{?_isa} >= 3.1
Requires: fio-engine-libaio%{?_isa}
Requires: hicolor-icon-theme
Provides: bundled(singleapplication) = 3.3.4
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(PolkitQt5-1)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
# /oreon:deps
%description
KDiskMark is an HDD and SSD benchmark tool with a very friendly graphical user
interface. KDiskMark with its presets and powerful GUI calls Flexible I/O Tester
and handles the output to provide an easy to view and interpret comprehensive
benchmark result. The application is written in C++ with Qt and doesn't have any
KDE dependencies.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n KDiskMark-%{version}
%autosetup -n KDiskMark-%{version} -DT 

mv SingleApplication-%{singleapplication_commit}/* src/singleapplication/

%build

%cmake -D USE_QT5=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
