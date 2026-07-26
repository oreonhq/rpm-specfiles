%global source0_hash c2e8a485110b97550f453226ec644ebac6cb29d1caef2902c007edab4308d985

%?mingw_package_header

Name:           mingw-libogg
Version:        1.3.3
Release:        19%{?dist}
Summary:        The Ogg bitstream file format library

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.xiph.org/
Source:         http://downloads.xiph.org/releases/ogg/libogg-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils

%description
Libogg is a library for manipulating Ogg bitstream file formats.
Libogg supports both making Ogg bitstreams and getting packets from
Ogg bitstreams.

# Win32
%package -n mingw32-libogg
Summary:        The Ogg bitstream file format library
Requires:       pkgconfig

%description -n mingw32-libogg
Libogg is a library for manipulating Ogg bitstream file formats.
Libogg supports both making Ogg bitstreams and getting packets from
Ogg bitstreams.

# Win64
%package -n mingw64-libogg
Summary:        The Ogg bitstream file format library
Requires:       pkgconfig

%description -n mingw64-libogg
Libogg is a library for manipulating Ogg bitstream file formats.
Libogg supports both making Ogg bitstreams and getting packets from
Ogg bitstreams.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libogg-%{version}

%build
sed -i "s/-O20/-O2/" configure
sed -i "s/-ffast-math//" configure
%mingw_configure --disable-static
%mingw_make %{?_smp_mflags}

%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

# zap docs, redundant with native package
rm -rf $RPM_BUILD_ROOT%{mingw32_docdir}
rm -rf $RPM_BUILD_ROOT%{mingw64_docdir}

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

# Win32
%files -n mingw32-libogg
%license COPYING
%doc AUTHORS CHANGES README.md
%{mingw32_bindir}/libogg-0.dll
%{mingw32_libdir}/libogg.dll.a
%{mingw32_libdir}/pkgconfig/ogg.pc
%dir %{mingw32_includedir}/ogg
%{mingw32_includedir}/ogg/ogg.h
%{mingw32_includedir}/ogg/os_types.h
%{mingw32_includedir}/ogg/config_types.h
%{mingw32_datadir}/aclocal/ogg.m4

# Win64
%files -n mingw64-libogg
%license COPYING
%doc AUTHORS CHANGES README.md
%{mingw64_bindir}/libogg-0.dll
%{mingw64_libdir}/libogg.dll.a
%{mingw64_libdir}/pkgconfig/ogg.pc
%dir %{mingw64_includedir}/ogg
%{mingw64_includedir}/ogg/ogg.h
%{mingw64_includedir}/ogg/os_types.h
%{mingw64_includedir}/ogg/config_types.h
%{mingw64_datadir}/aclocal/ogg.m4

%changelog
%autochangelog
