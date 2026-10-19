%global source0_hash 03eb1601e2306adc88c776afdf212217c6547990d2d0f9ca544dad9a8a9dbb8f
%global optflags %optflags -Wno-incompatible-pointer-types
%global so_major_version 1
%global so_version %{so_major_version}.3.0
Name:           libfishsound
Version:        1.0.1
Release:        1%{?dist}
Summary:        Simple programming interface for Xiph.Org codecs
License:        BSD-3-Clause
URL:            http://www.xiph.org/fishsound/
Source0:        http://downloads.xiph.org/releases/libfishsound/libfishsound-%{version}.tar.gz
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  flac-devel
BuildRequires:  gcc
BuildRequires:  liboggz-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  speex-devel
# /oreon:deps
%description
libfishsound provides a simple programming interface for decoding and
encoding audio data using Xiph.Org codecs (FLAC, Speex and Vorbis).

libfishsound by itself is designed to handle raw codec streams from a
lower level layer such as UDP datagrams. When these codecs are used in
files, they are commonly encapsulated in Ogg to produce Ogg FLAC, Speex
and Ogg Vorbis files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
%description    doc
The %{name}-doc package contains the documentation for %{name}.

%package        tools
Summary:        Sample programs bundled with %{name}
Requires:       %{name} = %{version}-%{release}
%description    tools
The %{name}-tools package contains sample programs that use %{name}.
The source code for these are included in %{name}-doc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# These dependencies should not be exported
# http://github.com/kfish/libfishsound/issues/#issue/1
sed -i '/^Requires:.*/d' fishsound.pc.in

%build

%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mv $RPM_BUILD_ROOT%{_datadir}/doc/%{name} \
   other-docs
rm -rf other-docs/latex
mkdir -p $RPM_BUILD_ROOT%{_bindir}
(cd src/examples/ && \
  mv .libs/* $RPM_BUILD_ROOT%{_bindir} &&
  make clean && rm -rf .deps .libs Makefile.*)
mv src/examples .
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libfishsound-devel -f %{oreon_filedir}/libfishsound-devel.list
%files -n libfishsound-doc -f %{oreon_filedir}/libfishsound-doc.list
%files -n libfishsound-tools -f %{oreon_filedir}/libfishsound-tools.list

%changelog

%autochangelog
