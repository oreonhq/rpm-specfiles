%global source0_hash 69aae21cd29224b4d038d5aef6c9770c6132497ac11edd93247b173ff11bd90d
%{?mingw_package_header}
%global snap dev2507081429
Name:           mingw-python-qt5
Summary:        MinGW Windows PyQt5
Version:        5.15.12
Release:        1%{?dist}
BuildArch:      noarch
License:        GPL-3.0-only
Url:            http://www.riverbankcomputing.com/software/pyqt/
%if 0%{?snap:1}
Source0:        https://www.riverbankcomputing.com/pypi/packages/pyqt5/pyqt5-%{version}.%{snap}.tar.gz
%else
%endif
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-PyQt-builder
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qtlocation
BuildRequires:  mingw32-qt5-qtmultimedia
BuildRequires:  mingw32-qt5-qtsensors
BuildRequires:  mingw32-qt5-qtserialport
BuildRequires:  mingw32-qt5-qtsvg
BuildRequires:  mingw32-qt5-qttools
BuildRequires:  mingw32-qt5-qtwebchannel
BuildRequires:  mingw32-qt5-qtwebkit
BuildRequires:  mingw32-qt5-qtxmlpatterns
BuildRequires:  mingw32-sip
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-PyQt-builder
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qtlocation
BuildRequires:  mingw64-qt5-qtmultimedia
BuildRequires:  mingw64-qt5-qtsensors
BuildRequires:  mingw64-qt5-qtserialport
BuildRequires:  mingw64-qt5-qtsvg
BuildRequires:  mingw64-qt5-qttools
BuildRequires:  mingw64-qt5-qtwebchannel
BuildRequires:  mingw64-qt5-qtwebkit
BuildRequires:  mingw64-qt5-qtxmlpatterns
BuildRequires:  mingw64-sip
# /oreon:deps
%description
MinGW Windows PyQt5

%package -n mingw32-python3-qt5
Summary:       MinGW Windows Python3-Qt5
Requires:      mingw32-python3-pyqt5-sip
%description -n mingw32-python3-qt5
MinGW Windows Python3-Qt5

%package -n mingw64-python3-qt5
Summary:       MinGW Windows Python3-Qt5
Requires:      mingw64-python3-pyqt5-sip
%description -n mingw64-python3-qt5
MinGW Windows Python3-Qt5

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pyqt5-%{version}%{?snap:.%{snap}}

%build

mingw32-sip-build --build-dir=build_win32 --no-make --qt-shared --confirm-license --qmake=%{_bindir}/mingw32-qmake-qt5 --no-tools --verbose
mingw64-sip-build --build-dir=build_win64 --no-make --qt-shared --confirm-license --qmake=%{_bindir}/mingw64-qmake-qt5 --no-tools --verbose
%mingw_make_build
%install
%mingw_make_install INSTALL_ROOT=%{buildroot}
%oreon_autofiles mingw32-python3-qt5 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-python3-qt5 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-qt5 -f %{oreon_filedir}/mingw32-python3-qt5.list
%files -n mingw64-python3-qt5 -f %{oreon_filedir}/mingw64-python3-qt5.list

%changelog

%autochangelog
