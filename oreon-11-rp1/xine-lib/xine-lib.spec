%global source0_hash 5f10d6d718a4a51c17ed1b32b031d4f9b80b061e8276535b2be31e5ac4b75e6f
%global         build_type_safety_c 2
%define         _legacy_common_support 1
%global         plugin_abi  2.11
%global         codecdir    %{_libdir}/codecs
%if 0%{?el8}
    %global     _without_gcrypt      1
%endif
%if 0%{?fedora} || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global _without_fame 1
%endif
%ifarch %{ix86}
    %global     have_vidix  1
%else
    %global     have_vidix  0
%endif
%global         date        20250206
%global         revision    15304
Summary:        A multimedia engine
Name:           xine-lib
Version:        1.2.13
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://www.xine-project.org/
%if ! 0%{?snapshot}
Source0:        https://downloads.sourceforge.net/xine/xine-lib-%{version}.tar.xz
%else
%endif
Source1:        make_xinelib_snapshot.sh
Patch0:         xine-lib-1.2.13-ffmpeg6-compatibility.patch
Patch1:         xine-lib-configure-c99.patch
Patch2:         xine-lib-1.2.13-ffmpeg6-compatibility_2.patch
Patch3:         xine-lib-1.2.13-ffmpeg7-compatibility.patch
Patch4:         xine-lib-1.2.13-fix_libnfs6.patch
Patch5:         xine-lib-1.2.13-gcc_15.patch
Patch6:         xine-lib-1.2.13-gcc_15-w32dll.patch
Patch7:         xine-lib-1.2.13-ffmpeg8-compatibility.patch
Provides:       xine-lib(plugin-abi) = %{plugin_abi}
Provides:       xine-lib(plugin-abi)%{?_isa} = %{plugin_abi}
Obsoletes:      xine-lib-extras-freeworld < 1.1.21-10
Provides:       xine-lib-extras-freeworld = %{version}-%{release}
%{!?_without_faad2:BuildRequires:  faad2-devel}
%{!?_without_imagemagick:BuildRequires:  ImageMagick-devel}
%{!?_without_dav1d:BuildRequires:  libdav1d-devel >= 0.3.1}
%{!?_without_dvdnav:BuildRequires:  libdvdnav-devel}
%{!?_without_fame:BuildRequires:  libfame-devel}
%{!?_without_gcrypt:BuildRequires:  libgcrypt-devel}
%{!?_without_nfs:BuildRequires:  libnfs-devel}
%{!?_without_png:BuildRequires:  libpng-devel >= 1.6.0}
%{?_with_xvmc:BuildRequires:  libXvMC-devel}
# oreon:deps
BuildRequires:  ImageMagick-devel
BuildRequires:  SDL-devel
BuildRequires:  a52dec-devel
BuildRequires:  aalib-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  faad2-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  flac-devel
BuildRequires:  fontconfig-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnutls-devel
BuildRequires:  gtk2-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libGLU-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXt-devel
BuildRequires:  libXv-devel
BuildRequires:  libaom-devel
BuildRequires:  libbluray-devel
BuildRequires:  libcaca-devel
BuildRequires:  libcdio-devel
BuildRequires:  libdav1d-devel
BuildRequires:  libdca-devel
BuildRequires:  libdvdnav-devel
BuildRequires:  libdvdread-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libmad-devel
BuildRequires:  libmng-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libnfs-devel
BuildRequires:  libpng-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libssh2-devel
BuildRequires:  libtheora-devel
BuildRequires:  libtool
BuildRequires:  libv4l-devel
BuildRequires:  libva-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libvpx-devel
BuildRequires:  libxcb-devel
BuildRequires:  libxdg-basedir-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  speex-devel
BuildRequires:  vcdimager-devel
BuildRequires:  wavpack-devel
BuildRequires:  wayland-devel
# /oreon:deps
%description
This package contains the Xine library.  It can be used to play back
various media, decode multimedia files from local disk drives, and display
multimedia streamed over the Internet. It interprets many of the most
common multimedia formats available - and some uncommon formats, too.

%package        devel
Summary:        Xine library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zlib-devel%{?_isa}
%description    devel
This package contains development files for %{name}.

%package        extras
Summary:        Additional plugins for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    extras
This package contains extra plugins for %{name}:
  - JACK
  - GDK-Pixbuf
  - SMB
  - SDL
  - AA-lib
  - Libcaca
%{!?_without_imagemagick:  - Image decoding}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if ! 0%{?snapshot}
%autosetup -p1
%else
%setup -n %{name}-%{version}-%{date}hg%{revision}
%endif

%build

autoreconf -fiv
%configure \
    --disable-dependency-tracking \
    --enable-ipv6 \
    --enable-v4l2 \
    --enable-libv4l \
%{?_with_xvmc:    --enable-xvmc} \
    --disable-gnomevfs \
    %{?_without_faad2:--disable-faad} \
    --enable-antialiasing \
    --with-freetype \
    --with-fontconfig \
    --with-caca \
    %{!?_without_dvdnav:--with-external-dvdnav} \
    --with-xv-path=%{_libdir} \
    --with-libflac \
    --without-esound \
    --with-wavpack \
%{?_without_w32dll:    --enable-w32dll=no} \
    --with-real-codecs-path=%{codecdir} \
    --with-w32-path=%{codecdir}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
%find_lang libxine2
mv %{buildroot}%{_docdir}/xine-lib __docs
rm -Rf %{buildroot}%{_libdir}/libxine*.la __docs/README \
       __docs/README.{freebsd,irix,macosx,solaris,MINGWCROSS,WIN32}
mkdir -p %{buildroot}%{codecdir}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n xine-lib-devel -f %{oreon_filedir}/xine-lib-devel.list
%files -n xine-lib-extras -f %{oreon_filedir}/xine-lib-extras.list

%changelog

%autochangelog
