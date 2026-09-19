%global source0_hash e41ddc3a473b555bdc0cbd80703dcb1f4610c1a7700d3b9d3d0c14a416e1074b

%{?mingw_package_header}

%global pkgname fcgi

Name:           mingw-%{pkgname}
Version:        2.4.7
Release:        2%{?dist}
Summary:        MinGW Windows %{pkgname} library
BuildArch:      noarch

License:        OML
URL:            https://fastcgi-archives.github.io/
Source0:        https://github.com/FastCGI-Archives/fcgi2/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Fix multiple initializations from incompatible pointer types
Patch0:         fcgi-incompat-pointer-types.patch

BuildRequires: make
BuildRequires: autoconf automake libtool

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++

%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}2-%{version}
# remove DOS End Of Line Encoding
sed -i 's/\r//' doc/fastcgi-prog-guide/ch2c.htm
# fix file permissions
chmod a-x include/fcgios.h libfcgi/os_unix.c

%build
autoreconf -ifv
%mingw_configure --disable-static
%mingw_make_build

%install
%mingw_make_install

# Delete *.la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Drop manpages
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/cgi-fcgi.exe
%{mingw32_bindir}/libfcgi-0.dll
%{mingw32_bindir}/libfcgi++-0.dll
%{mingw32_libdir}/libfcgi.dll.a
%{mingw32_libdir}/libfcgi++.dll.a
%{mingw32_libdir}/pkgconfig/fcgi.pc
%{mingw32_libdir}/pkgconfig/fcgi++.pc
%{mingw32_includedir}/*

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/cgi-fcgi.exe
%{mingw64_bindir}/libfcgi-0.dll
%{mingw64_bindir}/libfcgi++-0.dll
%{mingw64_libdir}/libfcgi.dll.a
%{mingw64_libdir}/libfcgi++.dll.a
%{mingw64_libdir}/pkgconfig/fcgi.pc
%{mingw64_libdir}/pkgconfig/fcgi++.pc
%{mingw64_includedir}/*

%changelog
%autochangelog
