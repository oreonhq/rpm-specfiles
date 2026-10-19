%global source0_hash 84cf6145f9cc82bfff690005be24392c8f3c52f8e00ff04d8eea371429c09424
%global has_luajit 1
%ifarch ppc64le s390x riscv64
%global has_luajit 0
%endif
%global with_scim 0
%bcond avif 1
Name:		efl
Version:	1.28.1
Release:        1%{?dist}
Summary:        Collection of Enlightenment libraries
License:	LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-only AND Zlib
URL:		http://enlightenment.org/
Source0:        https://download.enlightenment.org/rel/libs/efl/efl-%{version}.tar.xz
Patch1:		efl-1.25.0-check-fix.patch
Patch2:		efl-1.27.0-gettextfix.patch
Patch3:		efl-1.27.0-sdl-version-build.patch
Patch4:		efl-1.27.0-bigendian-gcc-fix.patch
%ifnarch s390x
%endif
%if %{with avif}
%endif
%if 0%{?has_luajit}
%else
%endif
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
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL2-devel
BuildRequires:  avahi-devel
BuildRequires:  bullet-devel
BuildRequires:  c-ares-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  dbus-devel
BuildRequires:  doxygen
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  fribidi-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  giflib-devel
BuildRequires:  glibc-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  ibus-devel
BuildRequires:  libX11-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXau-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXtst-devel
BuildRequires:  libblkid-devel
BuildRequires:  libdrm-devel
BuildRequires:  libinput-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libjxl-devel
BuildRequires:  libmount-devel
BuildRequires:  libpng-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtiff-devel
BuildRequires:  libunwind-devel
BuildRequires:  libwebp-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  luajit-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  openjpeg2-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libspectre)
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  rlottie-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  tslib-devel
BuildRequires:  uuid-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
%global oreon_srcdir %{name}-%{version}
%oreon_prep
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
 -Decore-imf-loaders-disabler=scim \
 -Dglib=true \
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
sed -i 's|ecore_sdl|ecore-sdl|g' %{buildroot}%{_libdir}/pkgconfig/elementary.pc
sed -i 's|ecore_sdl|ecore-sdl|g' %{buildroot}%{_libdir}/pkgconfig/elementary-cxx.pc
%if 0%{?__isa_bits} == 64
mv %{buildroot}%{_datadir}/gdb/auto-load/usr/lib %{buildroot}%{_datadir}/gdb/auto-load%{_libdir}
%endif
chmod -x src/bin/edje/edje_cc_out.c
find %{buildroot} -name '*.la' -delete
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_user_post ethumb.service
%postun

%systemd_user_postun ethumb.service
%preun

%systemd_user_preun ethumb.service
%files -f %{oreon_filedir}/main.list
%files -n efl-devel -f %{oreon_filedir}/efl-devel.list

%changelog

%autochangelog
