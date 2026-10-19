%global source0_hash 83e6704730683d004d20e21b8f7f55dcb3383cdf84c0daedf30bde175f774638
%?mingw_package_header
Name:           mingw-libogg
Version:        1.3.6
Release:        1%{?dist}
Summary:        The Ogg bitstream file format library
License:        LicenseRef-Callaway-BSD
URL:            http://www.xiph.org/
Source0:        http://downloads.xiph.org/releases/ogg/libogg-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
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
rm -rf $RPM_BUILD_ROOT%{mingw32_docdir}
rm -rf $RPM_BUILD_ROOT%{mingw64_docdir}
find $RPM_BUILD_ROOT -name "*.la" -delete
%oreon_autofiles mingw32-libogg usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libogg usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libogg -f %{oreon_filedir}/mingw32-libogg.list
%files -n mingw64-libogg -f %{oreon_filedir}/mingw64-libogg.list

%changelog

%autochangelog
