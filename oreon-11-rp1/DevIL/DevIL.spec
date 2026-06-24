%global source0_hash none

Name:           DevIL
Version:        1.7.8
Release:        53%{?dist}
Summary:        A cross-platform image library
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://openil.sourceforge.net/
Source0:        http://downloads.sourceforge.net/openil/%{name}-%{version}.tar.gz
Patch0:         DevIL-1.7.5-allegropicfix.patch
Patch1:         DevIL-1.7.5-il_endian_h.patch
Patch2:         DevIL-1.7.8-CVE-2009-3994.patch
Patch3:         DevIL-1.7.8-libpng15.patch
Patch4:         DevIL-1.7.8-gcc5.patch
Patch5:         devil-1.7.8-jasper2.patch
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  allegro-devel
BuildRequires:  libGLU-devel
BuildRequires:  libICE-devel
BuildRequires:  libXext-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  jasper-devel
BuildRequires:  SDL-devel => 1.2.5
BuildRequires: make

%description
Developer's Image Library (DevIL) is a programmer's library to develop
applications with very powerful image loading capabilities, yet is easy for a
developer to learn and use. Ultimate control of images is left to the
developer, so unnecessary conversions, etc. are not performed. DevIL utilizes
a simple, yet powerful, syntax. DevIL can load, save, convert, manipulate,
filter and display a wide variety of image formats.


%package devel
Summary:        Development files for DevIL
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for DevIL


%package ILUT
Summary:        The libILUT component of DevIL
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description ILUT
The libILUT component of DevIL


%package ILUT-devel
Summary:        Development files for the libILUT component of DevIL
Requires:       %{name}-ILUT%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       allegro-devel libGLU-devel

%description ILUT-devel
Development files for the libILUT component of DevIL


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n devil-%{version}
iconv -f iso8859-1 CREDITS -t utf8 > CREDITS.conv
touch -r CREDITS CREDITS.conv
mv CREDITS.conv CREDITS
chmod -x src-IL/src/il_*.c
sed -i 's|png12|png16|g' configure


%build
%ifarch x86_64
DISABLE_SSE="--disable-sse3"
%endif
%ifarch %{ix86}
DISABLE_SSE="--disable-sse --disable-sse2 --disable-sse3"
%endif
%configure --enable-ILU --enable-ILUT --disable-static --disable-allegrotest \
           $DISABLE_SSE
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|LD_RUN_PATH|DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/*.la
rm %{buildroot}%{_infodir}/dir


%ldconfig_scriptlets
%ldconfig_scriptlets ILUT


%files
%{_bindir}/ilur
%{_libdir}/libIL.so.*
%{_libdir}/libILU.so.*
%license COPYING
%doc AUTHORS ChangeLog CREDITS README TODO

%files devel
%{_libdir}/libIL.so
%{_libdir}/libILU.so
%{_libdir}/pkgconfig/IL.pc
%{_libdir}/pkgconfig/ILU.pc
%dir %{_includedir}/IL
%{_includedir}/IL/il.h
%{_includedir}/IL/ilu.h
%{_includedir}/IL/ilu_region.h
%{_infodir}/DevIL_manual.info.*

%files ILUT
%{_libdir}/libILUT.so.*

%files ILUT-devel
%{_libdir}/libILUT.so
%{_libdir}/pkgconfig/ILUT.pc
%{_includedir}/IL/devil_cpp_wrapper.hpp
%{_includedir}/IL/ilut.h


%changelog
%autochangelog

