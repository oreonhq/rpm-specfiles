%global source0_hash dee22e893cb5fc2b2b6ebd60b88478ab8556cb3b93f9a0d7ce8f3b61851871d4
Name:           libmpeg2
Version:        0.5.1
Release:        33%{?dist}
Summary:        MPEG-2 decoder libraries
License:        GPL-2.0-or-later
URL:            http://libmpeg2.sourceforge.net
Source0:        https://distfiles.macports.org/libmpeg2/libmpeg2-%{version}.tar.gz
Patch0:         libmpeg2-inline.patch
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libXt-devel
BuildRequires:  libXv-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
libmpeg2 is a free library for decoding mpeg-2 and mpeg-1 video
streams. It is released under the terms of the GPL license.

%package -n     mpeg2dec
Summary:        MPEG-2 decoder program
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n mpeg2dec
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1
autoreconf -fiv

iconv -f ISO-8859-1 -t UTF-8 AUTHORS > AUTHORS.tmp
touch -r AUTHORS AUTHORS.tmp 
cp -p -f AUTHORS.tmp AUTHORS
rm AUTHORS.tmp

#Disable ppc altivec case
sed -i -e 's/ppc-/noppc64-/' configure.ac configure
sed -i -e 's/powerpc-/nopowerpc64-/' configure.ac configure

%build

%configure --disable-static \
%ifarch %{ix86} ppc
  --disable-accel-detect \
%endif
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{make_build} \
%ifarch %{ix86}
  OPT_CFLAGS="-fPIC -DPIC" \
%else
  OPT_CFLAGS="" \
%endif
%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
install -pm 0644 libmpeg2/mpeg2_internal.h \
  %{buildroot}%{_includedir}/mpeg2dec/
%ldconfig_scriptlets
%oreon_autofiles mpeg2dec usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mpeg2dec -f %{oreon_filedir}/mpeg2dec.list
%files -n libmpeg2-devel -f %{oreon_filedir}/libmpeg2-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.1-33
- Import
