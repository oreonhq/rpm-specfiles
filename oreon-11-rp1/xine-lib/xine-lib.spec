%global source0_hash 5f10d6d718a4a51c17ed1b32b031d4f9b80b061e8276535b2be31e5ac4b75e6f

%global         build_type_safety_c 2
%define         _legacy_common_support 1
%global         plugin_abi  2.11
%global         codecdir    %{_libdir}/codecs

%if 0%{?el8}
    %global     _without_gcrypt      1
%endif

%if 0%{?fedora} || 0%{?rhel} >= 9
%global _without_fame 1
%endif

%ifarch %{ix86}
    %global     have_vidix  1
%else
    %global     have_vidix  0
%endif

#global         snapshot    1
%global         date        20250206
%global         revision    15304

Summary:        A multimedia engine
Name:           xine-lib
Version:        1.2.13
Release:        29%{?snapshot:.%{date}hg%{revision}}%{?dist}
License:        GPL-2.0-or-later
URL:            https://www.xine-project.org/
%if ! 0%{?snapshot}
Source0:        https://downloads.sourceforge.net/xine/xine-lib-%{version}.tar.xz
%else
Source0:        xine-lib-%{version}-%{date}hg%{revision}.tar.xz
%endif
# Script to make a snapshot
Source1:        make_xinelib_snapshot.sh

# ffmpeg6 compatibility
# See: https://sourceforge.net/p/xine/xine-lib-1.2/ci/771f4ae27e582123ff3500444718fc8f96186d74/
Patch0:         xine-lib-1.2.13-ffmpeg6-compatibility.patch
#
Patch1:         xine-lib-configure-c99.patch
# See: https://sourceforge.net/p/xine/xine-lib-1.2/ci/1e7b184008860c8be2289c3cefd9dee57f06193a/
Patch2:         xine-lib-1.2.13-ffmpeg6-compatibility_2.patch
# See: https://sourceforge.net/p/xine/xine-lib-1.2/ci/73b833e7fe356cd2d9490dda4ebc9bfe16fce958/
Patch3:         xine-lib-1.2.13-ffmpeg7-compatibility.patch
# See: https://sourceforge.net/p/xine/xine-lib-1.2/ci/ea7071a960a1ca8719422e80e130994c8f549731/
Patch4:         xine-lib-1.2.13-fix_libnfs6.patch
# See:
# https://sourceforge.net/p/xine/xine-lib-1.2/ci/a38be398e202da7b8e414969b74fbd65eb34798d/
# https://sourceforge.net/p/xine/xine-lib-1.2/ci/b5fd08a878bb80072ba5b71e30391ab52698c22f/
Patch5:         xine-lib-1.2.13-gcc_15.patch
# https://sourceforge.net/p/xine/xine-lib-1.2/ci/5a68e8b08fd5378780f76c3ab957d790209388db/
Patch6:         xine-lib-1.2.13-gcc_15-w32dll.patch
# https://sourceforge.net/p/xine/xine-lib-1.2/ci/9bb3977ea7e2b652742b3cdd200b0a4a72eb48bc/
# https://sourceforge.net/p/xine/xine-lib-1.2/ci/a8fffd1193b2247c7f732d4df83dcc03fce96dbe/
Patch7:         xine-lib-1.2.13-ffmpeg8-compatibility.patch

Provides:       xine-lib(plugin-abi) = %{plugin_abi}
Provides:       xine-lib(plugin-abi)%{?_isa} = %{plugin_abi}

Obsoletes:      xine-lib-extras-freeworld < 1.1.21-10
Provides:       xine-lib-extras-freeworld = %{version}-%{release}

BuildRequires:  a52dec-devel
BuildRequires:  aalib-devel
BuildRequires:  alsa-lib-devel
%{!?_without_faad2:BuildRequires:  faad2-devel}
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  ffmpeg-free-devel
%else
BuildRequires:  ffmpeg-devel
%endif
BuildRequires:  flac-devel
BuildRequires:  fontconfig-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnutls-devel
# System lib cannot currently be used
#BuildRequires:  gsm-devel
BuildRequires:  gtk2-devel
%{!?_without_imagemagick:BuildRequires:  ImageMagick-devel}
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  pipewire-jack-audio-connection-kit-devel
%else
BuildRequires:  jack-audio-connection-kit-devel
%endif
BuildRequires:  libaom-devel >= 1.0.0
BuildRequires:  libbluray-devel >= 0.2.1
BuildRequires:  libcaca-devel
BuildRequires:  libcdio-devel
%{!?_without_dav1d:BuildRequires:  libdav1d-devel >= 0.3.1}
BuildRequires:  libdca-devel
%{!?_without_dvdnav:BuildRequires:  libdvdnav-devel}
BuildRequires:  libdvdread-devel
%{!?_without_fame:BuildRequires:  libfame-devel}
%{!?_without_gcrypt:BuildRequires:  libgcrypt-devel}
BuildRequires:  libGLU-devel
BuildRequires:  libmad-devel
BuildRequires:  libmng-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmpcdec-devel
%{!?_without_nfs:BuildRequires:  libnfs-devel}
%{!?_without_png:BuildRequires:  libpng-devel >= 1.6.0}
BuildRequires:  libsmbclient-devel
BuildRequires:  libssh2-devel
BuildRequires:  libtheora-devel
BuildRequires:  libtool
BuildRequires:  libv4l-devel
BuildRequires:  libva-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libvpx-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libxdg-basedir-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXt-devel
BuildRequires:  libXv-devel
%{?_with_xvmc:BuildRequires:  libXvMC-devel}
BuildRequires:  mesa-libEGL-devel
BuildRequires:  openssl-devel >= 1.0.2
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  SDL-devel
BuildRequires:  speex-devel
BuildRequires:  vcdimager-devel
BuildRequires:  wavpack-devel
BuildRequires:  wayland-devel

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
# Keep list of options in mostly the same order as ./configure --help.
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

# Remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install
%find_lang libxine2
mv %{buildroot}%{_docdir}/xine-lib __docs

# Removing useless files
rm -Rf %{buildroot}%{_libdir}/libxine*.la __docs/README \
       __docs/README.{freebsd,irix,macosx,solaris,MINGWCROSS,WIN32}

# Directory for binary codecs
mkdir -p %{buildroot}%{codecdir}

%ldconfig_scriptlets

%files -f libxine2.lang
%doc AUTHORS CREDITS ChangeLog* README TODO
%doc __docs/README.* __docs/faq.*
%license COPYING COPYING.LIB
%dir %{codecdir}/
%{_datadir}/xine-lib/
%{_libdir}/libxine.so.2*
%{_mandir}/man5/xine.5*
%dir %{_libdir}/xine/
%dir %{_libdir}/xine/plugins/
%dir %{_libdir}/xine/plugins/%{plugin_abi}/
%{_libdir}/xine/plugins/%{plugin_abi}/mime.types
# Listing every plugin separately for better control over binary packages
# containing exactly the plugins we want, nothing accidentally snuck in
# nor dropped.
%dir %{_libdir}/xine/plugins/%{plugin_abi}/post/
%{_libdir}/xine/plugins/%{plugin_abi}/post/xineplug_post_audio_filters.so
%{_libdir}/xine/plugins/%{plugin_abi}/post/xineplug_post_goom.so
%{_libdir}/xine/plugins/%{plugin_abi}/post/xineplug_post_mosaico.so
%{_libdir}/xine/plugins/%{plugin_abi}/post/xineplug_post_planar.so
%{_libdir}/xine/plugins/%{plugin_abi}/post/xineplug_post_switch.so
%{_libdir}/xine/plugins/%{plugin_abi}/post/xineplug_post_tvtime.so
%{_libdir}/xine/plugins/%{plugin_abi}/post/xineplug_post_visualizations.so
%if %{have_vidix}
%dir %{_libdir}/xine/plugins/%{plugin_abi}/vidix/
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/cyberblade_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/mach64_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/mga_crtc2_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/mga_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/nvidia_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/pm2_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/pm3_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/radeon_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/rage128_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/savage_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/sis_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/unichrome_vid.so
%endif
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_ao_out_alsa.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_ao_out_oss.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_ao_out_pulseaudio.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_a52.so
%{!?_without_dav1d:%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_dav1d.so}
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_dts.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_dvaudio.so
%{!?_without_faad2:%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_faad.so}
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_ff.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_gsm610.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_libaom.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_libjpeg.so
%{!?_without_png:%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_libpng.so}
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_libvpx.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_lpcm.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_mad.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_mpc.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_mpeg2.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_rawvideo.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_real.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_spu.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_spucc.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_spucmml.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_spudvb.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_spuhdmv.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_to_spdif.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_vdpau.so
%ifarch %{ix86}
%{!?_without_w32dll:%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_w32dll.so}
%endif
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_asf.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_audio.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_fli.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_games.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_image.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_mng.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_modplug.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_nsv.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_playlist.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_pva.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_slave.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_video.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dxr3.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_flac.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_hw_frame_vaapi.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_bluray.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_cdda.so
%{!?_without_gcrypt:%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_crypto.so}
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_dvb.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_dvd.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_mms.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_network.so
%{!?_without_nfs:%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_nfs.so}
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_pvr.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_rtp.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_ssh.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_v4l2.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_vcd.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_vcdo.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_nsf.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_sputext.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_tls_gnutls.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_tls_openssl.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_va_display_drm.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_va_display_glx.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_va_display_wl.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_va_display_x11.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vdr.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_fb.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_gl_glx.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_gl_egl_x11.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_gl_egl_wl.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_opengl.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_opengl2.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_raw.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_vaapi.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_vdpau.so
%if %{have_vidix}
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_vidix.so
%endif
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_xcbshm.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_xcbxv.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_xshm.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_xv.so
%{?_with_xvmc:%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_xvmc.so}
%{?_with_xvmc:%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_xxmc.so}
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_wavpack.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_xiph.so

%files extras
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_ao_out_jack.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_gdk_pixbuf.so
%{!?_without_imagemagick:%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_image.so}
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_smb.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_aa.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_caca.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_sdl.so

%files devel
%doc __docs/hackersguide/*
%{_bindir}/xine-config
%{_bindir}/xine-list*
%{_datadir}/aclocal/xine.m4
%{_includedir}/xine.h
%{_includedir}/xine/
%{_libdir}/libxine.so
%{_libdir}/pkgconfig/libxine.pc
%{_mandir}/man1/xine-config.1*
%{_mandir}/man1/xine-list*.1*

%changelog
%autochangelog
