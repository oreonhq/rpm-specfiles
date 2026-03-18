Name:           libmpeg2
Version:        0.5.1
Release:        33%{?dist}
Summary:        MPEG-2 decoder libraries

License:        GPL-2.0-or-later
URL:            http://libmpeg2.sourceforge.net
Source0:        %{url}/files/libmpeg2-%{version}.tar.gz
# https://github.com/videolan/vlc/blob/master/contrib/src/libmpeg2/libmpeg2-inline.patch
Patch0:         libmpeg2-inline.patch

BuildRequires:  gcc
BuildRequires:  SDL-devel
BuildRequires:  libXt-devel
BuildRequires:  libXv-devel
# bootstrap deps
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires: make


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

# mpeg2dec have rpath
# remove rpath from libtool
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


#Fix datatype internal definitions
install -pm 0644 libmpeg2/mpeg2_internal.h \
  %{buildroot}%{_includedir}/mpeg2dec/

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_libdir}/*.so.*

%files -n mpeg2dec
%{_bindir}/corrupt_mpeg2
%{_bindir}/extract_mpeg2
%{_bindir}/mpeg2dec
%{_mandir}/man1/*.1*

%files devel
%doc CodingStyle doc/libmpeg2.txt doc/sample*.c
%{_includedir}/mpeg2dec/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmpeg2.pc
%{_libdir}/pkgconfig/libmpeg2convert.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.1-33
- Prepare for Oreon 11 (RP1)
