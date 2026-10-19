%global source0_hash f18abd3bd2cb05960d00f15f36c63f97eb1759f9571977e3e42191ff16b9b467
%global _lto_cflags %nil
%global altname gx_head
%global altname2 guitarix2
Name:           guitarix
Version:        0.47.0
Release:        1%{?dist}
Summary:        A virtual guitar amplifier
License:        GPL-2.0-or-later
URL:            https://github.com/brummer10/%{name}
Source0:        https://github.com/brummer10/%{name}/releases/download/V%{version}/%{altname2}-%{version}.tar.xz
Patch0:         %{name}-cassert-include.patch
Requires:       clearlooks-compact-gnome-theme
Requires:       google-roboto-condensed-fonts
Obsoletes:      ladspa-%{name}-plugins < %{version}
# oreon:deps
BuildRequires:  /usr/bin/find
BuildRequires:  /usr/bin/sassc
BuildRequires:  avahi-gobject-devel
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  eigen3-devel
BuildRequires:  faust
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glade-devel
BuildRequires:  google-roboto-condensed-fonts
BuildRequires:  gperf
BuildRequires:  gtk3-devel
BuildRequires:  gtkmm30-devel
BuildRequires:  intltool
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  ladspa-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  liblrdf-devel
BuildRequires:  libsigc++20-devel
BuildRequires:  libsndfile-devel
BuildRequires:  lilv-devel
BuildRequires:  lv2-devel
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  zita-convolver-devel
BuildRequires:  zita-resampler-devel
# /oreon:deps
%description
Guitarix takes the signal from your guitar as any real amp would do:
as a mono-signal from your sound card.
The input is processed by a main amp and a rack-section.
Both can be routed separately and deliver a processed stereo-signal via Jack.
You may fill the rack with effects from more than 25 built-in modules,
including stuff from a simple noise gate to brain-slashing modulation f/x
like flanger, phaser or auto-wah.

%package -n libgxw
Summary:        Guitarix GTK library
License:        GPL-2.0-or-later 
%description -n libgxw
This package contains the Guitarix GTK widget library

%package -n libgxwmm
Summary:        Guitarix GTK C++ library
License:        GPL-2.0-or-later 
%description -n libgxwmm
This package contains the Guitarix GTK C++ widget library

%package -n libgxw-devel
Summary:        Development files for libgxw
License:        GPL-2.0-or-later 
Requires:       libgxw%{?_isa} = %{version}-%{release}
%description -n libgxw-devel
This package contains files required to use the libgxw C Guitarix 
widget library

%package -n libgxwmm-devel
Summary:        Development files for libgxwmm
License:        GPL-2.0-or-later 
Requires:       libgxwmm%{?_isa} = %{version}-%{release}
%description -n libgxwmm-devel
This package contains files required to use the libgxwmm C++ Guitarix widget 
library

%package -n gxw-glade
Summary:        Guitarix GTK library glade support
License:        GPL-2.0-or-later 
Requires:       glade
Requires:       libgxw-devel%{?_isa} = %{version}-%{release}
%description -n gxw-glade
This package contains support for using the Guitarix GTK widget library
with glade

%package -n lv2-%{name}-plugins
Summary:        Collection of LV2 guitarix plug-ins
License:        GPL-2.0-or-later AND ISC
Requires:       lv2
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n lv2-%{name}-plugins
This package contains the guitarix amp plug-ins that come together with 
guitarix, but can also be used by any other ladspa host.

%prep

%autosetup -p1 -n %{name}-%{version}

# Fix unversioned python shebangs
%py3_shebang_fix \
    $(find -name wscript) \
    waf \
    tools/make_jsonrpc_methods \
    src/gx_head/builder/make \
    .

# The build system does not use these bundled libraries by default. But
# just to make sure:
rm -fr src/zita-convolver* src/zita-resampler*
sed -i -e 's|-O3||' wscript

%build

%set_build_flags
CXXFLAGS+=" -fomit-frame-pointer -ftree-loop-linear -ffinite-math-only -fno-math-errno -fno-signed-zeros -fstrength-reduce"
%ifarch %{ix86}
CXXFLAGS+=" -mfxsr"
%endif
./waf -vv configure --prefix=%{_prefix} --libdir=%{_libdir}          \
      --shared-lib --lib-dev --no-ldconfig --glade-support           \
      --lv2dir=%{_libdir}/lv2 \
      --cxxflags-release="-DNDEBUG"
./waf -vv build %{?_smp_mflags}
%install
./waf -vv install --destdir="%{buildroot}" --libdir="%{_libdir}"
desktop-file-install                                    \
--add-category="X-DigitalProcessing"                    \
--dir=%{buildroot}%{_datadir}/applications              \
%{buildroot}/%{_datadir}/applications/%{name}.desktop
chmod 755 %{buildroot}%{_libdir}/libgxw*.so.0.1
rm -rf %{buildroot}%{_libdir}/libgxw*.so
ln -s libgxwmm.so.0.1 %{buildroot}%{_libdir}/libgxwmm.so
ln -s libgxw.so.0.1 %{buildroot}%{_libdir}/libgxw.so
chmod 755 %{buildroot}%{_libdir}/glade/modules/libgladegx.so
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.%{name}.%{name}.metainfo.xml
%find_lang %{name}
%oreon_autofiles libgxw usr/*/lib*.so.*
%oreon_autofiles libgxwmm usr/*/lib*.so.*
%oreon_autofiles libgxw-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libgxwmm-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles gxw-glade usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libgxw -f %{oreon_filedir}/libgxw.list
%files -n libgxwmm -f %{oreon_filedir}/libgxwmm.list
%files -n libgxw-devel -f %{oreon_filedir}/libgxw-devel.list
%files -n libgxwmm-devel -f %{oreon_filedir}/libgxwmm-devel.list
%files -n gxw-glade -f %{oreon_filedir}/gxw-glade.list
%files -n lv2-guitarix-plugins -f %{oreon_filedir}/lv2-guitarix-plugins.list

%changelog

%autochangelog
