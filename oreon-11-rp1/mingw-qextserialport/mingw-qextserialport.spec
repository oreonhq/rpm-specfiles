%global source0_hash 1f1c068206af95c328b165e9ea31006e43faa6ee224aaec6aa0f72d2afa5f011

%{?mingw_package_header}

%global pkgname qextserialport
%global libver 1
%global pre rc

Name:          mingw-%{pkgname}
Version:       1.2
Release:       0.22%{?pre:.%pre}%{?dist}
Summary:       MinGW Windows %{pkgname} library
BuildArch:     noarch

License:       MIT
URL:           https://github.com/qextserialport/qextserialport
Source0:       https://github.com/qextserialport/qextserialport/archive/%{version}%{pre}/%{pkgname}-%{version}%{pre}.tar.gz
# A private qt4 header, just grab it separately instead of adding a mingw-qt-private subpackage, since qt4 will not receive any updates anymore anyway
Source1:       https://raw.githubusercontent.com/qt/qt/4.8/src/corelib/kernel/qwineventnotifier_p.h

# Only do a release build
Patch0:        qextserialport_releasebuild.patch
# Use bundled qwineventnotifier_p.h (see SOURCE1)
Patch1:        qextserialport_qwineventnotifier_p.patch

BuildRequires: make
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-qt5-qtbase

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-qt5-qtbase

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

# Remove duplicate dlls
rm -f %{buildroot}%{mingw32_libdir}/Qt5ExtSerialPort%{libver}.dll
rm -f %{buildroot}%{mingw64_libdir}/Qt5ExtSerialPort%{libver}.dll

# Fix import library names
mv %{buildroot}%{mingw32_libdir}/libQt5ExtSerialPort%{libver}.dll.a %{buildroot}%{mingw32_libdir}/libQt5ExtSerialPort.dll.a
mv %{buildroot}%{mingw64_libdir}/libQt5ExtSerialPort%{libver}.dll.a %{buildroot}%{mingw64_libdir}/libQt5ExtSerialPort.dll.a

# Remove unused files
rm -f %{buildroot}%{mingw32_libdir}/Qt5ExtSerialPort.prl
rm -f %{buildroot}%{mingw64_libdir}/Qt5ExtSerialPort.prl

%files -n mingw32-%{pkgname}-qt5
%license LICENSE
%{mingw32_bindir}/Qt5ExtSerialPort%{libver}.dll
%{mingw32_libdir}/libQt5ExtSerialPort.dll.a
%{mingw32_includedir}/qt5/QtExtSerialPort/
%{mingw32_datadir}/qt5/mkspecs/features/extserialport.prf

%files -n mingw64-%{pkgname}-qt5
%license LICENSE
%{mingw64_bindir}/Qt5ExtSerialPort%{libver}.dll
%{mingw64_libdir}/libQt5ExtSerialPort.dll.a
%{mingw64_includedir}/qt5/QtExtSerialPort/
%{mingw64_datadir}/qt5/mkspecs/features/extserialport.prf

%changelog
%autochangelog
