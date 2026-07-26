%global source0_hash a9fabf1fdb2d6cc3713fd5413724ecc266f438a53a24595619080db9e51426a1

%?mingw_package_header

Name:           mingw-ftplib
Version:        4.0
Release:        24%{?dist}
Summary:        MinGW Library of FTP routines

License:        Artistic-2.0
URL:            http://nbpfaus.net/~pfau/ftplib/
Source0:        http://nbpfaus.net/~pfau/ftplib/ftplib-%{version}.tar.gz
Source1:        ftplib-rc.rc
Patch0:         ftplib-3.1-1-modernize.patch
Patch1:         ftplib-4.0-mingw.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils

BuildRequires:  autoconf, automake, libtool

%description
ftplib is a set of routines that implement the FTP protocol. They allow
applications to create and access remote files through function calls
instead of needing to fork and exec an interactive ftp client program.
This library is cross-compiled for MinGW.

%package -n mingw32-ftplib
Summary:        MinGW Library of FTP routines

%description -n mingw32-ftplib
ftplib is a set of routines that implement the FTP protocol. They allow
applications to create and access remote files through function calls
instead of needing to fork and exec an interactive ftp client program.
This library is cross-compiled for MinGW.

%package -n mingw64-ftplib
Summary:        MinGW Library of FTP routines

%description -n mingw64-ftplib
ftplib is a set of routines that implement the FTP protocol. They allow
applications to create and access remote files through function calls
instead of needing to fork and exec an interactive ftp client program.
This library is cross-compiled for MinGW.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ftplib-%{version}
%patch -P0 -p1
%patch -P1 -p1
cp -p %{SOURCE1} src/

%build
cd src/
mkdir build_win{32,64}
ln -s %{_builddir}/%{buildsubdir}/src/*.c ./build_win32/
ln -s %{_builddir}/%{buildsubdir}/src/*.h ./build_win32/
ln -s %{_builddir}/%{buildsubdir}/src/*.c ./build_win64/
ln -s %{_builddir}/%{buildsubdir}/src/*.h ./build_win64/
ln -s %{_builddir}/%{buildsubdir}/src/*.rc ./build_win32/
ln -s %{_builddir}/%{buildsubdir}/src/*.rc ./build_win64/
ln -s %{_builddir}/%{buildsubdir}/src/Makefile ./build_win32/
ln -s %{_builddir}/%{buildsubdir}/src/Makefile ./build_win64/
%{mingw32_env}
make -C build_win32 libftp.dll
%{mingw64_env}
make -C build_win64 libftp.dll

%install
mkdir -p $RPM_BUILD_ROOT/%{mingw32_bindir}
mkdir -p $RPM_BUILD_ROOT/%{mingw32_libdir}
mkdir -p $RPM_BUILD_ROOT/%{mingw32_includedir}
mkdir -p $RPM_BUILD_ROOT/%{mingw64_bindir}
mkdir -p $RPM_BUILD_ROOT/%{mingw64_libdir}
mkdir -p $RPM_BUILD_ROOT/%{mingw64_includedir}
cd src/
cp -p build_win32/libftp.dll $RPM_BUILD_ROOT/%{mingw32_bindir}
cp -p build_win32/libftp.dll.a $RPM_BUILD_ROOT/%{mingw32_libdir}
cp -p build_win32/ftplib.h $RPM_BUILD_ROOT/%{mingw32_includedir}
cp -p build_win64/libftp.dll $RPM_BUILD_ROOT/%{mingw64_bindir}
cp -p build_win64/libftp.dll.a $RPM_BUILD_ROOT/%{mingw64_libdir}
cp -p build_win64/ftplib.h $RPM_BUILD_ROOT/%{mingw64_includedir}

%files -n mingw32-ftplib
%license LICENSE
# Docs are provided by native package
%{mingw32_bindir}/libftp.dll
%{mingw32_libdir}/libftp.dll.a
%{mingw32_includedir}/ftplib.h

%files -n mingw64-ftplib
%license LICENSE
# Docs are provided by native package
%{mingw64_bindir}/libftp.dll
%{mingw64_libdir}/libftp.dll.a
%{mingw64_includedir}/ftplib.h

%changelog
%autochangelog
