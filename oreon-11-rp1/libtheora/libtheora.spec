%global source0_hash f36da409947aa2b3dcc6af0a8c2e3144bc19db2ed547d64e9171c59c66561c61

# enable bootstrap mode (e.g. disables doc generation)
%bcond bootstrap 0
# enable devel-docs (transfig is unavailable in RHEL)
%bcond devel_docs %[%{without bootstrap} && %{undefined rhel}]

Name:           libtheora
Epoch:          1
Version:        1.1.1
Release:        41%{?dist}
Summary:        Theora Video Compression Codec
License:        BSD-3-Clause
URL:            http://www.theora.org
Source0:        http://downloads.xiph.org/releases/theora/libtheora-1.1.1.tar.xz
Patch0:         libtheora-1.1.1-fix-pp_sharp_mod-calc.patch
# https://bugs.archlinux.org/task/35985
Patch1:         libtheora-1.1.1-libpng16.patch
Patch2:         libtheora-1.1.1-libm.patch

BuildRequires: make
BuildRequires:  autoconf automake libtool
BuildRequires:  libogg-devel >= 2:1.1
BuildRequires:  libvorbis-devel
BuildRequires:  SDL-devel libpng-devel
%if %{without devel_docs}
Obsoletes: %{name}-devel-docs < %{epoch}:%{version}-%{release}
%else
BuildRequires:  doxygen
BuildRequires:  tetex-latex transfig
%endif

%description
Theora is Xiph.Org's first publicly released video codec, intended
for use within the Ogg's project's Ogg multimedia streaming system.
Theora is derived directly from On2's VP3 codec; Currently the two are
nearly identical, varying only in encapsulating decoder tables in the
bitstream headers, but Theora will make use of this extra freedom
in the future to improve over what is possible with VP3.


%package devel
Summary:        Development tools for Theora applications
Requires:       libogg-devel >= 2:1.1
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
The libtheora-devel package contains the header files needed to develop
applications with libtheora.


%package devel-docs
Summary:        Documentation for developing Theora applications
BuildArch:      noarch

%description devel-docs
The libtheora-devel-docs package contains the documentation needed
to develop applications with libtheora.


%package -n theora-tools
Summary:        Command line tools for Theora videos
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description -n theora-tools
The theora-tools package contains simple command line tools for use
with theora bitstreams.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -P0 -p1
%patch -P1 -p0 -b .libpng16
%patch -P2 -p1

# Update config.guess/sub to fix builds on new architectures (aarch64/ppc64le)
cp /usr/lib/rpm/redhat/config.* .

%build
./autogen.sh
# no custom CFLAGS please
sed -i 's/CFLAGS="$CFLAGS $cflags_save"/CFLAGS="$cflags_save"/g' configure
%configure --enable-shared --disable-static
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{make_build}

%if %{with devel_docs}
make -C doc/spec %{?_smp_mflags}
%endif


%install
%{make_install}

find %{buildroot} -type f -name "*.la" -delete
rm -r %{buildroot}/%{_docdir}/*

mkdir -p %{buildroot}/%{_bindir}
install -m 755 examples/.libs/dump_video $RPM_BUILD_ROOT/%{_bindir}/theora_dump_video
install -m 755 examples/.libs/encoder_example $RPM_BUILD_ROOT/%{_bindir}/theora_encode
install -m 755 examples/.libs/player_example $RPM_BUILD_ROOT/%{_bindir}/theora_player
install -m 755 examples/.libs/png2theora $RPM_BUILD_ROOT/%{_bindir}/png2theora


%ldconfig_scriptlets


%files
%doc README COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/theora
%{_libdir}/*.so
%{_libdir}/pkgconfig/theora*.pc

%if %{with devel_docs}
%files devel-docs
%doc doc/libtheora/html doc/vp3-format.txt doc/spec/Theora.pdf
%doc doc/color.html doc/draft-ietf-avt-rtp-theora-00.txt
%endif

%files -n theora-tools
%{_bindir}/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.1-41
- Prepare for Oreon 11 (RP1)
