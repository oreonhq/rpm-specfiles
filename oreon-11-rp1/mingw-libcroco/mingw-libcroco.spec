%global source0_hash ddc4b5546c9fb4280a5017e2707fbd4839034ed1aba5b7d4372212f34f84f860

%{?mingw_package_header}

Name:           mingw-libcroco
Version:        0.6.12
Release:        23%{?dist}
Summary:        A CSS2 parsing library for MinGW

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://ftp.gnome.org/pub/GNOME/sources/libcroco/
Source:         http://download.gnome.org/sources/libcroco/0.6/libcroco-%{version}.tar.xz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-pkg-config
BuildRequires:  mingw64-pkg-config
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-libxml2

%description
CSS2 parsing and manipulation library for GNOME

This is the MinGW version of this library.

%package -n mingw32-libcroco
Summary:        MinGW A CSS2 parsing library
Requires:       pkgconfig

%description -n mingw32-libcroco
This package contains the header files and libraries needed to develop MinGW
applications that use libcroco.

%package -n mingw32-libcroco-static
Summary:        MinGW static A CSS2 parsing library
Requires:       mingw32-libcroco = %{version}-%{release}

%description -n mingw32-libcroco-static
This package contains the static libraries needed to develop MinGW
applications that use libcroco-0.6.

%package -n mingw64-libcroco
Summary:        MinGW A CSS2 parsing library
Requires:       pkgconfig

%description -n mingw64-libcroco
This package contains the header files and libraries needed to develop MinGW
applications that use libcroco-0.6.

%package -n mingw64-libcroco-static
Summary:        MinGW static A CSS2 parsing library
Requires:       mingw64-libcroco = %{version}-%{release}

%description -n mingw64-libcroco-static
This package contains the static libraries needed to develop MinGW
applications that use libcroco-0.6.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libcroco-%{version}

%build
%mingw_configure --without-pic
%mingw_make %{?_smp_mflags} V=1

%install
%mingw_make_install "DESTDIR=$RPM_BUILD_ROOT"

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

%files -n mingw32-libcroco
%license COPYING
%doc AUTHORS README NEWS
%{mingw32_bindir}/croco-0.6-config
%{mingw32_bindir}/csslint-0.6.exe
%{mingw32_bindir}/libcroco-0.6-3.dll
%{mingw32_includedir}/libcroco-0.6
%{mingw32_libdir}/libcroco-0.6.dll.a
%{mingw32_libdir}/pkgconfig/*.pc

%files -n mingw32-libcroco-static
%{mingw32_libdir}/libcroco-0.6.a

%files -n mingw64-libcroco
%license COPYING
%doc AUTHORS README NEWS
%{mingw64_bindir}/croco-0.6-config
%{mingw64_bindir}/csslint-0.6.exe
%{mingw64_bindir}/libcroco-0.6-3.dll
%{mingw64_includedir}/libcroco-0.6
%{mingw64_libdir}/libcroco-0.6.dll.a
%{mingw64_libdir}/pkgconfig/*.pc

%files -n mingw64-libcroco-static
%{mingw64_libdir}/libcroco-0.6.a

%changelog
%autochangelog
