%global source1_hash 15f08c3a0e0ea2af6df3af06ef0c5d8043fe51bd1f4336bc54635dc0a7a2f12f
%global source0_hash 1f1c068206af95c328b165e9ea31006e43faa6ee224aaec6aa0f72d2afa5f011
%{?mingw_package_header}
%global pkgname qextserialport
%global libver 1
%global pre rc
Name:          mingw-%{pkgname}
Version:       1.2
Release:        1%{?dist}
Summary:        MinGW Windows qextserialport library
BuildArch:     noarch
License:       MIT
URL:           https://github.com/qextserialport/qextserialport
Source0:        https://github.com/%{pkgname}/%{pkgname}/a%{pre}hive/%{version}%{pre}/%{pkgname}-%{version}%{pre}.tar.gz
Source1:       https://raw.githubusercontent.com/qt/qt/4.8/src/corelib/kernel/qwineventnotifier_p.h
Patch0:        qextserialport_releasebuild.patch
Patch1:        qextserialport_qwineventnotifier_p.patch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase
# /oreon:deps
%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname} Qt5 library
%description -n mingw32-%{pkgname}-qt5
MinGW Windows %{pkgname} Qt5 library.

%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname} Qt5 library
%description -n mingw64-%{pkgname}-qt5
MinGW Windows %{pkgname} Qt5 library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}%{pre}
cp -a %{SOURCE1} src/

%build

mkdir build_qt5
pushd build_qt5
%mingw_qmake_qt5 ../..
%mingw_make_build
popd
%install
pushd build_qt5
%mingw_make install INSTALL_ROOT=%{buildroot}
popd
rm -f %{buildroot}%{mingw32_libdir}/Qt5ExtSerialPort%{libver}.dll
rm -f %{buildroot}%{mingw64_libdir}/Qt5ExtSerialPort%{libver}.dll
mv %{buildroot}%{mingw32_libdir}/libQt5ExtSerialPort%{libver}.dll.a %{buildroot}%{mingw32_libdir}/libQt5ExtSerialPort.dll.a
mv %{buildroot}%{mingw64_libdir}/libQt5ExtSerialPort%{libver}.dll.a %{buildroot}%{mingw64_libdir}/libQt5ExtSerialPort.dll.a
rm -f %{buildroot}%{mingw32_libdir}/Qt5ExtSerialPort.prl
rm -f %{buildroot}%{mingw64_libdir}/Qt5ExtSerialPort.prl
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-qextserialport-qt5 -f %{oreon_filedir}/mingw32-qextserialport-qt5.list
%files -n mingw64-qextserialport-qt5 -f %{oreon_filedir}/mingw64-qextserialport-qt5.list

%changelog

%autochangelog
