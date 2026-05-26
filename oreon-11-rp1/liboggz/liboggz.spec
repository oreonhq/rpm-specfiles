Name:           liboggz
Version:        1.1.3
Release:        %autorelease
Summary:        Simple programming interface for Ogg files and streams

License:        BSD-3-Clause
URL:            http://www.xiph.org/oggz/
Source0:        http://downloads.xiph.org/releases/liboggz/%{name}-%{version}.tar.gz
# Always have oggz_off_t == loff_t even on 64-bit platforms
Patch0:		liboggz-1.1.1-multilib.patch
# oreon url source checksums begin
%global source0_sha256 2466d03b67ef0bcba0e10fb352d1a9ffd9f96911657abce3cbb6ba429c656e2f
%global source0_file liboggz-1.1.3.tar.gz
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires:  libogg-devel >= 1.0
BuildRequires:  doxygen
BuildRequires:  docbook-utils
BuildRequires: make

%description
Oggz provides a simple programming interface for reading and writing
Ogg files and streams. Ogg is an interleaving data container developed
by Monty at Xiph.Org, originally to support the Ogg Vorbis audio
format.

%package devel
Summary:	Files needed for development using liboggz
Requires:       liboggz = %{version}-%{release}
Requires:       libogg-devel >= 1.0
Requires:       pkgconfig

%description devel
Oggz provides a simple programming interface for reading and writing
Ogg files and streams. Ogg is an interleaving data container developed
by Monty at Xiph.Org, originally to support the Ogg Vorbis audio
format.

This package contains the header files and documentation needed for
development using liboggz.

%package doc
Summary:        Documentation for liboggz
Requires:	liboggz = %{version}-%{release}

%description doc
Oggz provides a simple programming interface for reading and writing
Ogg files and streams. Ogg is an interleaving data container developed
by Monty at Xiph.Org, originally to support the Ogg Vorbis audio
format.

This package contains HTML documentation needed for development using
liboggz.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/liboggz-1.1.3.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2466d03b67ef0bcba0e10fb352d1a9ffd9f96911657abce3cbb6ba429c656e2f" || { echo "oreon: Source0 SHA256 mismatch for liboggz-1.1.3.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{name}-%{version}
%patch -P0 -p1 -b .multilib

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%check
# Tests disabled for moment because of rpath issue
#make check

%install
%makeinstall docdir=$PWD/__docs_staging INSTALL="%{__install} -p"

# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la

# not particularly interested in the tex docs, the html version has everything
rm -rf __docs_staging/latex

# Multilib fix: ensure generated headers have timestamps
# independent of build time
(cd include/oggz &&
    touch -r oggz_off_t_generated.h.in.multilib \
      %{buildroot}%{_includedir}/oggz/oggz_off_t_generated.h
)


%files
%doc AUTHORS ChangeLog README
%license COPYING
# 0 length NEWS file
# %doc NEWS
%{_libdir}/liboggz.so.*
%{_mandir}/man1/*
%{_bindir}/oggz*

%files devel
%{_includedir}/oggz
%{_libdir}/liboggz.so
%{_libdir}/pkgconfig/oggz.pc

%files doc
%doc __docs_staging/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.3-1
- Prepare for Oreon 11 (RP1)
