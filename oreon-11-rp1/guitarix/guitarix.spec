%global source0_hash none

%global _lto_cflags %nil

# guitarix has merged with gx_head branch and tarball is distributed as guitarix2
# project name remains guitarix however
%global altname gx_head
%global altname2 guitarix2

Name:           guitarix
Version:        0.47.0
Release:        1%{?dist}
Summary:        A virtual guitar amplifier
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/brummer10/%{name}
Source0:        https://github.com/brummer10/%{name}/releases/download/V%{version}/%{altname2}-%{version}.tar.xz
Patch0:         %{name}-cassert-include.patch

BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  %{_bindir}/find
BuildRequires:  desktop-file-utils
BuildRequires:  faust
BuildRequires:  fftw-devel >= 3.3.8
BuildRequires:  gtk3-devel >= 3.22
BuildRequires:  gtkmm30-devel >= 3.22
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  ladspa-devel
BuildRequires:  libsigc++20-devel
BuildRequires:  libsndfile-devel
BuildRequires:  zita-convolver-devel >= 3.0.2
BuildRequires:  zita-resampler-devel >= 0.1.1-3
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  boost-devel
BuildRequires:  liblrdf-devel
BuildRequires:  lv2-devel
BuildRequires:  lilv-devel
BuildRequires:  gperf
BuildRequires:  avahi-gobject-devel
BuildRequires:  eigen3-devel
BuildRequires:  libcurl-devel >= 7.26.0
BuildRequires:  google-roboto-condensed-fonts
BuildRequires:  %{_bindir}/sassc
BuildRequires:  glade-devel
BuildRequires:  libappstream-glib

Requires:       clearlooks-compact-gnome-theme
Requires:       google-roboto-condensed-fonts

# LADSPA support has been removed
Obsoletes:      ladspa-%{name}-plugins < %{version}

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

# validate appdata
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.%{name}.%{name}.metainfo.xml

%find_lang %{name}

%files -f %{name}.lang
%doc changelog README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{altname}/
%{_datadir}/pixmaps/*
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/org.%{name}.%{name}.metainfo.xml

%files -n libgxw
%{_libdir}/libgxw.so.0*

%files -n libgxwmm
%{_libdir}/libgxwmm.so.0*

%files -n libgxw-devel
%{_libdir}/libgxw.so
%{_includedir}/gxw
%{_includedir}/gxw.h
%{_libdir}/pkgconfig/gxw.pc

%files -n libgxwmm-devel
%{_libdir}/libgxwmm.so
%{_includedir}/gxwmm
%{_includedir}/gxwmm.h
%{_libdir}/pkgconfig/gxwmm.pc

%files -n gxw-glade
%{_libdir}/glade/modules/libgladegx.so
%{_datadir}/%{name}/icons
%{_datadir}/glade/catalogs/*

%files -n lv2-%{name}-plugins
%{_libdir}/lv2/*

%changelog
%autochangelog
