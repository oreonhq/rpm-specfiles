%global source0_hash 3b08f5f4f9b4eb82f151a7040bfd6fe6c6fb922efe4b1659c66ea933276965e8

%{?mingw_package_header}

%global pkgname libcharset

Name:          mingw-%{pkgname}
Version:       1.18
Summary:       MinGW Windows libcharset library
Release:       2%{?dist}

BuildArch:     noarch
License:       LGPL-2.0-or-later
URL:           http://www.haible.de/bruno/packages-libcharset.html
Source0:       https://ftp.gnu.org/pub/gnu/libiconv/libiconv-%{version}.tar.gz

BuildRequires: make
BuildRequires: automake autoconf libtool libtool-ltdl-devel bison flex

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc

%description
MinGW Windows libcharset library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows libcharset library

%description -n mingw32-%{pkgname}
MinGW Windows libcharset library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows libcharset library

%description -n mingw64-%{pkgname}
MinGW Windows libcharset library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n libiconv-%{version}

%build
(
cd libcharset
%mingw_configure --disable-static
%mingw_make_build
)

%install
(
cd libcharset
%mingw_make_install
)

find %{buildroot} -name *.la -delete

%files -n mingw32-%{pkgname}
%license libcharset/COPYING.LIB
%{mingw32_bindir}/libcharset-1.dll
%{mingw32_includedir}/*.h
%{mingw32_libdir}/libcharset.dll.a

%files -n mingw64-%{pkgname}
%license libcharset/COPYING.LIB
%{mingw64_bindir}/libcharset-1.dll
%{mingw64_includedir}/*.h
%{mingw64_libdir}/libcharset.dll.a

%changelog
%autochangelog
