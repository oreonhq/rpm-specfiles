%global source0_hash ebdf77a8f5c0a8f7a9e42323844fa09502b34eb1d1fece7b5f54da41fe2122ec
%bcond bootstrap 0
%bcond devel_docs %[%{without bootstrap} && %{undefined rhel}]
Name:           libtheora
Epoch:          1
Version:        1.2.0
Release:        1%{?dist}
Summary:        Theora Video Compression Codec
License:        BSD-3-Clause
URL:            http://www.theora.org
Source0:        http://downloads.xiph.org/releases/theora/%{name}-%{version}.tar.xz
%if %{without devel_docs}
Obsoletes: %{name}-devel-docs < %{epoch}:%{version}-%{release}
%else
%endif
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  make
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

# Update config.guess/sub to fix builds on new architectures (aarch64/ppc64le)
cp /usr/lib/rpm/redhat/config.* .

%build

./autogen.sh
sed -i 's/CFLAGS="$CFLAGS $cflags_save"/CFLAGS="$cflags_save"/g' configure
%configure --enable-shared --disable-static
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
%oreon_autofiles theora-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libtheora-devel -f %{oreon_filedir}/libtheora-devel.list
%files -n libtheora-devel-docs -f %{oreon_filedir}/libtheora-devel-docs.list
%files -n theora-tools -f %{oreon_filedir}/theora-tools.list

%changelog

%autochangelog
