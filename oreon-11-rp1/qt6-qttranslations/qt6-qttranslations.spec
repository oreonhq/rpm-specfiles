%global source0_hash 85929c0c30d6f273f23bd879bb69803ea17b010ab73cab2f8abf95357f6f6bbb
%global qt_module qttranslations
%if 0%{?unstable}
%global prerelease rc
%endif
Summary:        Qt6 - QtTranslations module
Name:    qt6-%{qt_module}
Version: 6.12.0
Release:        1%{?dist}
License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)
%if 0%{?unstable}
%else
Source0:        https://download.qt.io/a%{prerelease}hive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-s%{prerelease}-%{version}.tar.xz
%endif
BuildArch: noarch
%if 0%{?_qt6:1}
Provides: %{_qt6}-ar = %{version}-%{release}
Provides: %{_qt6}-ca = %{version}-%{release}
Provides: %{_qt6}-cs = %{version}-%{release}
Provides: %{_qt6}-da = %{version}-%{release}
Provides: %{_qt6}-de = %{version}-%{release}
Provides: %{_qt6}-es = %{version}-%{release}
Provides: %{_qt6}-fa = %{version}-%{release}
Provides: %{_qt6}-fi = %{version}-%{release}
Provides: %{_qt6}-fr = %{version}-%{release}
Provides: %{_qt6}-gl = %{version}-%{release}
Provides: %{_qt6}-gd = %{version}-%{release}
Provides: %{_qt6}-he = %{version}-%{release}
Provides: %{_qt6}-hu = %{version}-%{release}
Provides: %{_qt6}-hr = %{version}-%{release}
Provides: %{_qt6}-it = %{version}-%{release}
Provides: %{_qt6}-ja = %{version}-%{release}
Provides: %{_qt6}-ka = %{version}-%{release}
Provides: %{_qt6}-ko = %{version}-%{release}
Provides: %{_qt6}-lg = %{version}-%{release}
Provides: %{_qt6}-lt = %{version}-%{release}
Provides: %{_qt6}-lv = %{version}-%{release}
Provides: %{_qt6}-nl = %{version}-%{release}
Provides: %{_qt6}-nn = %{version}-%{release}
Provides: %{_qt6}-pl = %{version}-%{release}
Provides: %{_qt6}-pt_BR = %{version}-%{release}
Provides: %{_qt6}-pt_PT = %{version}-%{release}
Provides: %{_qt6}-ru = %{version}-%{release}
Provides: %{_qt6}-sk = %{version}-%{release}
Provides: %{_qt6}-sl = %{version}-%{release}
Provides: %{_qt6}-sv = %{version}-%{release}
Provides: %{_qt6}-uk = %{version}-%{release}
Provides: %{_qt6}-zh_CN = %{version}-%{release}
Provides: %{_qt6}-zh_TW = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  ninja-build
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1

%build

%cmake_qt6
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
