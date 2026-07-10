%global source0_hash 84cf6145f9cc82bfff690005be24392c8f3c52f8e00ff04d8eea371429c09424
%global has_luajit 1

%ifarch ppc64le s390x riscv64
%global has_luajit 0
%endif

# Look, you probably don't want this. scim is so 2012. ibus is the new hotness.
# Enabling this means you'll almost certainly need to pass ECORE_IMF_MODULE=xim
# to get anything to work. (*cough*terminology*cough*)
%global with_scim 0

# Enable avif support (this broke before)
%bcond avif 1

Name:		efl
Version:	1.28.1
Release:	7%{?dist}
Summary:	Collection of Enlightenment libraries
# Automatically converted from old format: BSD and LGPLv2+ and GPLv2 and zlib - review is highly recommended.
License:	LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-only AND Zlib
URL:		http://enlightenment.org/
Source0:	https://download.enlightenment.org/rel/libs/efl/efl-%{version}.tar.xz
# This is hacky, but it gets us building in rawhide again.
# Upstream efl probably needs to rework how they use check in their C tests
Patch1:		efl-1.25.0-check-fix.patch

# Fix headerless .po files that modern gettext doesn't like
Patch2:		efl-1.27.0-gettextfix.patch

# Build ecore_sdl versioned so. So efl no longer requires efl-devel
Patch3:		efl-1.27.0-sdl-version-build.patch

# Handle incompatible pointer types in the bigendian cases
Patch4:		efl-1.27.0-bigendian-gcc-fix.patch

%ifnarch s390x
BuildRequires:	libunwind-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:	bullet-devel libpng-devel libjpeg-devel gstreamer1-devel zlib-devel
BuildRequires:	gstreamer1-plugins-base-devel libtiff-devel openssl-devel
BuildRequires:	curl-devel dbus-devel glibc-devel fontconfig-devel freetype-devel
BuildRequires:	fribidi-devel pulseaudio-libs-devel libsndfile-devel libX11-devel
BuildRequires:	libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel
BuildRequires:	libXext-devel libXfixes-devel libXinerama-devel libXrandr-devel
BuildRequires:	libXrender-devel libXScrnSaver-devel libXtst-devel libXcursor-devel
BuildRequires:	libXi-devel mesa-libGL-devel mesa-libEGL-devel
BuildRequires:	libblkid-devel libmount-devel systemd-devel harfbuzz-devel
BuildRequires:	libwebp-devel tslib-devel SDL2-devel SDL-devel c-ares-devel
BuildRequires:	libxkbcommon-devel uuid-devel libxkbcommon-x11-devel avahi-devel
BuildRequires:	rlottie-devel libjxl-devel
BuildRequires:	pkgconfig(poppler-cpp) >= 0.12
BuildRequires:	pkgconfig(libspectre) pkgconfig(libraw)
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.14.0
BuildRequires:	pkgconfig(cairo) >= 1.0.0
%if %{with avif}
BuildRequires:	pkgconfig(libavif)
%endif
%if %{with_scim}
BuildRequires:	scim-devel
%endif
BuildRequires:	ibus-devel
BuildRequires:	doxygen systemd giflib-devel openjpeg2-devel libdrm-devel
BuildRequires:	wayland-devel >= 1.11.0
BuildRequires:	wayland-protocols-devel >= 1.7
BuildRequires:	meson >= 0.50
BuildRequires:	ninja-build gettext-devel mesa-libGLES-devel
BuildRequires:	mesa-libgbm-devel libinput-devel
%if 0%{?has_luajit}
BuildRequires:	luajit-devel
%else
BuildRequires:	compat-lua-devel
%endif
# For AutoReq cmake-filesystem
BuildRequires:	cmake
# These are convenience provides to aid in migration
Provides:	e_dbus%{?_isa} = %{version}-%{release}
Provides:	e_dbus = %{version}-%{release}
Obsoletes:	e_dbus <= 1.7.10
Provides:	ecore = %{version}-%{release}
Provides:	ecore%{?_isa} = %{version}-%{release}
Obsoletes:	ecore <= 1.7.10
Provides:	edje = %{version}-%{release}
Provides:	edje%{?_isa} = %{version}-%{release}
Obsoletes:	edje <= 1.7.10
Provides:	eet = %{version}-%{release}
Provides:	eet%{?_isa} = %{version}-%{release}
Obsoletes:	eet <= 1.7.10
Provides:	eeze = %{version}-%{release}
Provides:	eeze%{?_isa} = %{version}-%{release}
Obsoletes:	eeze <= 1.7.10
Provides:	efreet = %{version}-%{release}
Provides:	efreet%{?_isa} = %{version}-%{release}
Obsoletes:	efreet <= 1.7.10
Provides:	eina%{?_isa} = %{version}-%{release}
Provides:	eio = %{version}-%{release}
Provides:	eio%{?_isa} = %{version}-%{release}
Obsoletes:	eio <= 1.7.10
Provides:	eldbus%{?_isa} = %{version}-%{release}
Provides:	elementary = %{version}-%{release}
Provides:	elementary%{?_isa} = %{version}-%{release}
Obsoletes:	elementary <= 1.17.1
# Provides:	elocation%%{?_isa} = %%{version}-%%{release}
Provides:	elua%{?_isa} = %{version}-%{release}
Provides:	embryo = %{version}-%{release}
Provides:	embryo%{?_isa} = %{version}-%{release}
Obsoletes:	embryo <= 1.7.10
Provides:	emotion = %{version}-%{release}
Provides:	emotion%{?_isa} = %{version}-%{release}
Obsoletes:	emotion <= 1.7.10
Provides:	eo%{?_isa} = %{version}-%{release}
Provides:	eolian%{?_isa} = %{version}-%{release}
Provides:	ephysics%{?_isa} = %{version}-%{release}
Provides:	ethumb = %{version}-%{release}
Provides:	ethumb%{?_isa} = %{version}-%{release}
Obsoletes:	ethumb <= 1.7.10
Provides:	evas = %{version}-%{release}
Provides:	evas%{?_isa} = %{version}-%{release}
Obsoletes:	evas <= 1.7.10
Provides:	evas-generic-loaders = %{version}-%{release}
Provides:	evas-generic-loaders%{?_isa} = %{version}-%{release}
Obsoletes:	evas-generic-loaders <= 1.17.0
Provides:	libeina = %{version}-%{release}
Provides:	libeina%{?_isa} = %{version}-%{release}
Obsoletes:	libeina <= 1.7.10

%description
EFL is a collection of libraries for handling many common tasks a
developer may have such as data structures, communication, rendering,
widgets and more.

%package devel
Summary:	Development files for EFL
Requires:	efl%{?_isa} = %{version}-%{release}
Requires:	pkgconfig, libX11-devel
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
Provides:	e_dbus-devel%{?_isa} = %{version}-%{release}
Provides:	e_dbus-devel = %{version}-%{release}
Obsoletes:	e_dbus-devel <= 1.7.10
Provides:	ecore-devel = %{version}-%{release}
Provides:	ecore-devel%{?_isa} = %{version}-%{release}
Obsoletes:	ecore-devel <= 1.7.10
Provides:	edje-devel = %{version}-%{release}
Provides:	edje-devel%{?_isa} = %{version}-%{release}
Obsoletes:	edje-devel <= 1.7.10
Provides:	eet-devel = %{version}-%{release}
Provides:	eet-devel%{?_isa} = %{version}-%{release}
Obsoletes:	eet-devel <= 1.7.10
Provides:	eeze-devel = %{version}-%{release}
Provides:	eeze-devel%{?_isa} = %{version}-%{release}
Obsoletes:	eeze-devel <= 1.7.10
Provides:	efreet-devel = %{version}-%{release}
Provides:	efreet-devel%{?_isa} = %{version}-%{release}
Obsoletes:	efreet-devel <= 1.7.10
Provides:	eina-devel%{?_isa} = %{version}-%{release}
Provides:	eio-devel = %{version}-%{release}
Provides:	eio-devel%{?_isa} = %{version}-%{release}
Obsoletes:	eio-devel <= 1.7.10
Provides:	eldbus-devel%{?_isa} = %{version}-%{release}
Provides:	elementary-devel = %{version}-%{release}
Provides:	elementary-devel%{?_isa} = %{version}-%{release}
Obsoletes:	elementary-devel <= 1.17.1
# Provides:	elocation-devel%%{?_isa} = %%{version}-%%{release}
Provides:	embryo-devel = %{version}-%{release}
Provides:	embryo-devel%{?_isa} = %{version}-%{release}
Obsoletes:	embryo-devel <= 1.7.10
Provides:	emotion-devel = %{version}-%{release}
Provides:	emotion-devel%{?_isa} = %{version}-%{release}
Obsoletes:	emotion-devel <= 1.7.10
Provides:	eo-devel%{?_isa} = %{version}-%{release}
Provides:	eolian-devel%{?_isa} = %{version}-%{release}
Provides:	ephysics-devel%{?_isa} = %{version}-%{release}
Provides:	ethumb-devel = %{version}-%{release}
Provides:	ethumb-devel%{?_isa} = %{version}-%{release}
Obsoletes:	ethumb-devel <= 1.7.10
Provides:	evas-devel = %{version}-%{release}
Provides:	evas-devel%{?_isa} = %{version}-%{release}
Obsoletes:	evas-devel <= 1.7.10
Provides:	libeina-devel = %{version}-%{release}
Provides:	libeina-devel%{?_isa} = %{version}-%{release}
Obsoletes:	libeina-devel <= 1.7.10

%description devel
Development files for EFL.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1

%build
export CFLAGS="%optflags -std=gnu17"
export CXXFLAGS="%optflags -std=gnu++17"
%{meson} \
 -Dxinput22=true \
 -Dsystemd=true \
%if %{with avif}
 -Devas-loaders-disabler=json,heif \
%else
 -Devas-loaders-disabler=json,heif,avif \
%endif
 -Dharfbuzz=true \
 -Dsdl=true \
 -Dbuffer=true \
 -Davahi=true \
%if %{with_scim}
 -Decore-imf-loaders-disabler= \
%else
 -Decore-imf-loaders-disabler=scim \
 -Dglib=true \
%endif
 -Dfb=true \
 -Dwl=true \
 -Ddrm=true \
 -Dinstall-eo-files=true \
%if 0%{?has_luajit}
 -Dbindings=lua,cxx \
 -Dlua-interpreter=luajit \
 -Delua=true \
%else
 -Dbindings=cxx \
 -Dlua-interpreter=lua \
%endif
 -Dphysics=true
%{meson_build}

%install
%{meson_install}

# There is probably a better place to fix this, but I couldn't untangle it.
sed -i 's|ecore_sdl|ecore-sdl|g' %{buildroot}%{_libdir}/pkgconfig/elementary.pc
sed -i 's|ecore_sdl|ecore-sdl|g' %{buildroot}%{_libdir}/pkgconfig/elementary-cxx.pc

# yay pathing
%if 0%{?__isa_bits} == 64
mv %{buildroot}%{_datadir}/gdb/auto-load/usr/lib %{buildroot}%{_datadir}/gdb/auto-load%{_libdir}
%endif

# fix perms
chmod -x src/bin/edje/edje_cc_out.c

find %{buildroot} -name '*.la' -delete

%find_lang %{name}

%post
%systemd_user_post ethumb.service

%postun
%systemd_user_postun ethumb.service

%preun
%systemd_user_preun ethumb.service

%files -f %{name}.lang
%license COPYING licenses/COPYING.BSD licenses/COPYING.GPL licenses/COPYING.LGPL licenses/COPYING.SMALL
%doc AUTHORS COMPLIANCE README.md
%{_libdir}/libefl.so.1*
%{_libdir}/libefl_canvas_wl.so.1*
%{_bindir}/efl_debug
%{_bindir}/efl_debugd
%{_datadir}/icons/Enlightenment-X/
# ecore
%{_bindir}/ecore_evas_convert
%{_libdir}/ecore/
%{_libdir}/ecore_buffer/
%{_libdir}/ecore_con/
%{_libdir}/ecore_evas/
%{_libdir}/ecore_imf/
%{_libdir}/ecore_wl2/
%{_libdir}/libecore*.so.*
%{_datadir}/ecore/
%{_datadir}/ecore_con/
%{_datadir}/ecore_imf/
%{_datadir}/ecore_x/
%{_libdir}/libector.so.*
# edje
%{_bindir}/edje*
%{_datadir}/mime/packages/edje.xml
%{_libdir}/edje/
%{_libdir}/libedje.so.1*
# eet
%{_bindir}/diffeet
%{_bindir}/eet
%{_bindir}/eetpack
%{_bindir}/vieet
%{_libdir}/libeet.so.*
# eeze
%attr(0755,root,root) %caps(cap_audit_write,cap_chown,cap_setuid,cap_sys_admin=pe) %{_bindir}/eeze_scanner
%{_bindir}/eeze_scanner_monitor
%{_bindir}/eeze_disk_ls
%{_bindir}/eeze_mount
%{_bindir}/eeze_umount
%{_libdir}/eeze/
%{_libdir}/libeeze.so.1*
# efreet
%{_bindir}/efreetd
# we don't depend on dbus, but we want clean dir ownership here.
%dir %{_datadir}/dbus-1/
%dir %{_datadir}/dbus-1/services/
%{_libdir}/efreet/
%{_libdir}/libefreet.so.1*
%{_libdir}/libefreet_mime.so.1*
%{_libdir}/libefreet_trash.so.1*
# eina
%{_bindir}/eina_btlog
%{_bindir}/eina_modinfo
%{_libdir}/libeina.so.*
# eio
%{_libdir}/libeio.so.1*
# eldbus
%{_bindir}/eldbus-codegen
%{_libdir}/libeldbus.so.1*
# elementary
%{_bindir}/elementary_codegen
%{_bindir}/elementary_config
%{_bindir}/elementary_perf
%{_bindir}/elementary_quicklaunch
%{_bindir}/elementary_run
%{_bindir}/elementary_test
%{_bindir}/elm_prefs_cc
%{_libdir}/libelementary.so.1*
%{_libdir}/elementary/
%{_datadir}/applications/elementary*.desktop
%{_datadir}/elementary/
%{_datadir}/icons/hicolor/*/apps/elementary.png
# elocation
# %%{_libdir}/libelocation.so.1*
# elput
%{_libdir}/libelput.so.1*
# elua
%if 0%{?has_luajit}
%{_bindir}/elua
%{_datadir}/elua/
%{_libdir}/libelua.so.1*
%else
%exclude %{_datadir}/elua/
%endif
# embryo
%{_bindir}/embryo_cc
%{_libdir}/libembryo.so.1*
%{_libdir}/libemile.so.*
# emotion
%{_bindir}/emotion_test*
%{_libdir}/emotion/
%{_libdir}/libemotion.so.1*
# eo
%{_bindir}/eo_debug
%{_libdir}/libeo.so.1*
%{_libdir}/libeo_dbg.so.1*
%{_datadir}/gdb/auto-load/%{_libdir}/libeo.so.1*
# eolian
%{_bindir}/eolian_cxx
%{_bindir}/eolian_gen
%{_libdir}/libeolian.so.1*
# ephysics
%{_libdir}/libephysics.so.1*
# ethumb
%{_bindir}/ethumb
%{_bindir}/ethumbd
%{_bindir}/ethumbd_client
%{_userunitdir}/ethumb.service
%{_libdir}/ethumb/
%{_libdir}/ethumb_client/
%{_libdir}/libethumb.so.1*
%{_libdir}/libethumb_client.so.1*
%{_datadir}/dbus-1/services/org.enlightenment.Ethumb.service
%{_datadir}/ethumb
%{_datadir}/ethumb_client
# evas
# %%{_bindir}/evas_*
%{_libdir}/evas/
%{_libdir}/libevas.so.*
%{_datadir}/evas/
%{_datadir}/mime/packages/evas.xml
# exactness
%{_bindir}/exactness*
%{_libdir}/libexactness*.so.*
%{_datadir}/exactness/

%files devel
%{_includedir}/efl-1/
%{_includedir}/efl-cxx-1/
%{_includedir}/efl-canvas-wl-1/
%{_bindir}/efl_canvas_wl_test*
%{_libdir}/cmake/Efl/
%{_libdir}/libefl.so
%{_libdir}/libefl_canvas_wl.so
%{_libdir}/pkgconfig/efl-core.pc
%{_libdir}/pkgconfig/efl-cxx.pc
%{_libdir}/pkgconfig/efl-net.pc
%{_libdir}/pkgconfig/efl-ui.pc
%{_libdir}/pkgconfig/efl-canvas-wl.pc
%{_libdir}/pkgconfig/efl.pc
# ecore-devel
%{_includedir}/ecore-1/
%{_includedir}/ecore-audio-1/
%{_includedir}/ecore-avahi-1/
%{_includedir}/ecore-buffer-1/
%{_includedir}/ecore-con-1/
%{_includedir}/ecore-cxx-1/
%{_includedir}/ecore-drm2-1/
%{_includedir}/ecore-evas-1/
%{_includedir}/ecore-fb-1/
%{_includedir}/ecore-file-1/
%{_includedir}/ecore-imf-1/
%{_includedir}/ecore-imf-evas-1/
%{_includedir}/ecore-input-1/
%{_includedir}/ecore-input-evas-1/
%{_includedir}/ecore-ipc-1/
%{_includedir}/ecore-sdl-1/
%{_includedir}/ecore-wl2-1/
%{_includedir}/ecore-x-1/
%{_libdir}/cmake/Ecore*/
%{_libdir}/libecore*.so
%{_libdir}/pkgconfig/ecore*.pc
%{_libdir}/libector.so
%{_libdir}/pkgconfig/ector.pc
# edje-devel
%{_libdir}/libedje.so
%{_libdir}/pkgconfig/edje*.pc
%{_datadir}/edje
%{_includedir}/edje-*
%{_libdir}/cmake/Edje/
# eet-devel
%{_includedir}/eet-1/
%{_includedir}/eet-cxx-1/
%{_libdir}/cmake/Eet/
%{_libdir}/cmake/EetCxx/
%{_libdir}/pkgconfig/eet*.pc
%{_libdir}/libeet.so
# eeze-devel
%{_includedir}/eeze-1/
%{_libdir}/cmake/Eeze/
%{_libdir}/libeeze.so
%{_datadir}/eeze/
%{_libdir}/pkgconfig/eeze.pc
# efreet-devel
%{_includedir}/efreet-1/
%{_libdir}/cmake/Efreet/
%{_libdir}/libefreet.so
%{_libdir}/libefreet_mime.so
%{_libdir}/libefreet_trash.so
%{_datadir}/efreet/
%{_libdir}/pkgconfig/efreet.pc
%{_libdir}/pkgconfig/efreet-mime.pc
%{_libdir}/pkgconfig/efreet-trash.pc
# eina-devel
%{_includedir}/eina-1/
%{_includedir}/eina-cxx-1/
%{_libdir}/cmake/Eina*/
%{_libdir}/pkgconfig/eina*.pc
%{_libdir}/libeina.so
# eio-devel
%{_includedir}/eio-1/
%{_includedir}/eio-cxx-1/
%{_libdir}/libeio.so
%{_libdir}/pkgconfig/eio.pc
%{_libdir}/pkgconfig/eio-cxx.pc
%{_libdir}/cmake/Eio/
# eldbus-devel
%{_includedir}/eldbus-1/
%{_includedir}/eldbus-cxx-1/
%{_libdir}/cmake/Eldbus/
%{_libdir}/libeldbus.so
%{_libdir}/pkgconfig/eldbus.pc
%{_libdir}/pkgconfig/eldbus-cxx.pc
# elementary-devel
%{_includedir}/elementary-1/
%{_includedir}/elementary-cxx-1/
%{_libdir}/cmake/Elementary/
%{_libdir}/libelementary.so
%{_libdir}/pkgconfig/elementary.pc
%{_libdir}/pkgconfig/elementary-cxx.pc
# elocation-devel
# %%{_includedir}/elocation-1/
# %%{_libdir}/libelocation.so
# %%{_libdir}/pkgconfig/elocation.pc
# elput-devel
%{_includedir}/elput-1/
%{_libdir}/libelput.so
%{_libdir}/pkgconfig/elput.pc
# elua-devel
%if 0%{?has_luajit}
%{_includedir}/elua-1/
%{_libdir}/libelua.so
%{_libdir}/pkgconfig/elua.pc
%{_libdir}/cmake/Elua/
%else
%exclude %{_libdir}/cmake/Elua/
%endif
# embryo-devel
%{_includedir}/embryo-1/
%{_libdir}/libembryo.so
%{_libdir}/pkgconfig/embryo.pc
%{_datadir}/embryo/
%{_includedir}/emile-1/
%{_libdir}/cmake/Emile/
%{_libdir}/libemile.so
%{_libdir}/pkgconfig/emile.pc
# emotion-devel
%{_includedir}/emotion-1/
%{_libdir}/cmake/Emotion/
%{_libdir}/libemotion.so
%{_libdir}/pkgconfig/emotion.pc
%{_datadir}/emotion/
# eo-devel
%{_includedir}/eo-1/
%{_includedir}/eo-cxx-1/
%{_libdir}/cmake/Eo/
%{_libdir}/cmake/EoCxx/
%{_libdir}/libeo.so
%{_libdir}/libeo_dbg.so
%{_libdir}/pkgconfig/eo.pc
%{_libdir}/pkgconfig/eo-cxx.pc
%{_datadir}/eo/
# eolian-devel
%{_includedir}/eolian-1/
%{_includedir}/eolian-cxx-1/
%{_libdir}/cmake/Eolian/
%{_libdir}/cmake/EolianCxx/
%{_libdir}/pkgconfig/eolian.pc
%{_libdir}/pkgconfig/eolian-cxx.pc
%{_libdir}/libeolian.so
%{_datadir}/eolian/
# ephysics-devel
%{_includedir}/ephysics-1/
%{_libdir}/libephysics.so
%{_libdir}/pkgconfig/ephysics.pc
# ethumb-devel
%{_includedir}/ethumb-1/
%{_includedir}/ethumb-client-1/
%{_libdir}/cmake/Ethumb/
%{_libdir}/cmake/EthumbClient/
%{_libdir}/libethumb.so
%{_libdir}/libethumb_client.so
%{_libdir}/pkgconfig/ethumb.pc
%{_libdir}/pkgconfig/ethumb-client.pc
%{_libdir}/pkgconfig/ethumb_client.pc
# evas-devel
%{_includedir}/evas-1/
%{_includedir}/evas-cxx-1/
%{_libdir}/libevas.so
%{_libdir}/cmake/Evas/
%{_libdir}/cmake/EvasCxx/
%{_libdir}/pkgconfig/evas*.pc
# exactness
%{_libdir}/libexactness*.so

%changelog
%autochangelog