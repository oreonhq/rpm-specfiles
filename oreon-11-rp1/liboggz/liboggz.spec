%global source0_hash 2466d03b67ef0bcba0e10fb352d1a9ffd9f96911657abce3cbb6ba429c656e2f
Name:           liboggz
Version:        1.1.3
Release:        1%{?dist}
Summary:        Simple programming interface for Ogg files and streams
License:        BSD-3-Clause
URL:            http://www.xiph.org/oggz/
Source0:        http://downloads.xiph.org/releases/liboggz/%{name}-%{version}.tar.gz
Patch0:		liboggz-1.1.1-multilib.patch
# oreon:deps
BuildRequires:  docbook-utils
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libogg-devel
BuildRequires:  make
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}
%patch -P0 -p1 -b .multilib

%build

%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%check

%install
%makeinstall docdir=$PWD/__docs_staging INSTALL="%{__install} -p"
rm -f %{buildroot}%{_libdir}/*.la
rm -rf __docs_staging/latex
(cd include/oggz &&
    touch -r oggz_off_t_generated.h.in.multilib \
      %{buildroot}%{_includedir}/oggz/oggz_off_t_generated.h
)
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n liboggz-devel -f %{oreon_filedir}/liboggz-devel.list
%files -n liboggz-doc -f %{oreon_filedir}/liboggz-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.3-1
- Prepare for Oreon 11 (RP1)
