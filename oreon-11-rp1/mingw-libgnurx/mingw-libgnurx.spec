%global source0_hash 7147b7f806ec3d007843b38e19f42a5b7c65894a57ffc297a76b0dcd5f675d76
%?mingw_package_header
Name:           mingw-libgnurx
Version:        2.5.1
Release:        40%{?dist}
Summary:        MinGW Regex library
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://mingw.sourceforge.net/
Source0:        http://kent.dl.sourceforge.net/sourceforge/mingw/mingw-libgnurx-%{version}-src.tar.gz
Source1:        mingw32-libgnurx-configure.ac
Source2:        mingw32-libgnurx-Makefile.am
Patch0:         mingw32-libgnurx-honor-destdir.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
MinGW Windows regular expression library.

# Win32
%package -n mingw32-libgnurx
Summary:        MinGW Regex library
%description -n mingw32-libgnurx
MinGW Windows regular expression library.

%package -n mingw32-libgnurx-static
Summary:        Static version of the MinGW Windows regular expression library
Requires:       mingw32-libgnurx = %{version}-%{release}
%description -n mingw32-libgnurx-static
Static version of the MinGW Windows regular expression library.

# Win64
%package -n mingw64-libgnurx
Summary:        MinGW Regex library
%description -n mingw64-libgnurx
MinGW Windows regular expression library.

%package -n mingw64-libgnurx-static
Summary:        Static version of the MinGW Windows regular expression library
Requires:       mingw64-libgnurx = %{version}-%{release}
%description -n mingw64-libgnurx-static
Static version of the MinGW Windows regular expression library.

%?mingw_debug_package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mingw-libgnurx-%{version}
%patch -P0 -p0

# The Makefile which is delivered with this package can't create static
# libraries and misnames the resulting import libraries
# So replace the buildsystem by a more proper one
cp %{SOURCE1} configure.ac
cp %{SOURCE2} Makefile.am
touch NEWS
touch AUTHORS
libtoolize --copy
aclocal
autoconf
automake --add-missing

%build

%global mingw32_cppflags -std=c99
%global mingw64_cppflags -std=c99
%mingw_configure --enable-static --enable-shared
%mingw_make %{?_smp_mflags}
%install
mkdir -p $RPM_BUILD_ROOT%{mingw32_includedir} $RPM_BUILD_ROOT%{mingw64_includedir}
%mingw_make DESTDIR=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT%{mingw32_libdir}/libgnurx.a $RPM_BUILD_ROOT%{mingw32_libdir}/libregex.a
mv $RPM_BUILD_ROOT%{mingw64_libdir}/libgnurx.a $RPM_BUILD_ROOT%{mingw64_libdir}/libregex.a
mv $RPM_BUILD_ROOT%{mingw32_libdir}/libgnurx.dll.a $RPM_BUILD_ROOT%{mingw32_libdir}/libregex.dll.a
mv $RPM_BUILD_ROOT%{mingw64_libdir}/libgnurx.dll.a $RPM_BUILD_ROOT%{mingw64_libdir}/libregex.dll.a
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man
find $RPM_BUILD_ROOT -name "*.la" -delete
%oreon_autofiles mingw32-libgnurx usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libgnurx-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libgnurx usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libgnurx-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libgnurx -f %{oreon_filedir}/mingw32-libgnurx.list
%files -n mingw32-libgnurx-static -f %{oreon_filedir}/mingw32-libgnurx-static.list
%files -n mingw64-libgnurx -f %{oreon_filedir}/mingw64-libgnurx.list
%files -n mingw64-libgnurx-static -f %{oreon_filedir}/mingw64-libgnurx-static.list

%changelog

%autochangelog
