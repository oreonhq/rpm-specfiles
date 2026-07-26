%global source0_hash 2e0b57ce2fecc9375eef72938ed08ac8c8f6c5238e1cae24458f0b0e8dade7c7

# Allow building with GCC 14+
# This should be fixed properly but upstream is dead
%global optflags %optflags -Wno-incompatible-pointer-types

%global so_major_version 1
%global so_version %{so_major_version}.3.0

Name:           libfishsound
Version:        1.0.0
Release:        35%{?dist}
Summary:        Simple programming interface for Xiph.Org codecs

License:        BSD-3-Clause
URL:            http://www.xiph.org/fishsound/
Source0:        http://downloads.xiph.org/releases/libfishsound/libfishsound-%{version}.tar.gz

# also pulled in by speex-devel
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  flac-devel
BuildRequires:  speex-devel libvorbis-devel liboggz-devel libsndfile-devel
BuildRequires:  doxygen
BuildRequires:  make

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
# note: intentionally not noarch; contains a target-specific Makefile
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
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# overriding docdir does not work
mv $RPM_BUILD_ROOT%{_datadir}/doc/%{name} \
   other-docs
# remove Latex docs, they do not provide hyperlinks and
# thus are less usable than the HTML docs
rm -rf other-docs/latex

# move the examples we want
mkdir -p $RPM_BUILD_ROOT%{_bindir}
(cd src/examples/ && \
  mv .libs/* $RPM_BUILD_ROOT%{_bindir} &&
  make clean && rm -rf .deps .libs Makefile.*)
mv src/examples .

%files
%license COPYING
%doc AUTHORS README
%{_libdir}/*.so.%{so_major_version}
%{_libdir}/*.so.%{so_version}

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/fishsound.pc

%files doc
%doc examples other-docs/*

%files tools
%{_bindir}/*

%changelog
%autochangelog
