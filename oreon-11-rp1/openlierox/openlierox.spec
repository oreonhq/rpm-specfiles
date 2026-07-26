%global source0_hash none

%define prever rc5

Name:           openlierox
# Because we downgraded from 0.59 to 0.58 as 0.59 never became stable
Epoch:          1
Version:        0.58
Release:        0.38.%{prever}%{?dist}
Summary:        Addictive realtime multi-player 2D shoot-em-up
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://openlierox.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/OpenLieroX_%{version}_%{prever}.src.tar.bz2
Source1:        %{name}.desktop
Source2:        README.fedora
Patch1:         openlierox-gcc13.patch
Patch2:         openlierox-libxml2-buildfix.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  SDL_mixer-devel SDL_image-devel gd-devel
BuildRequires:  libxml2-devel zlib-devel desktop-file-utils libappstream-glib
BuildRequires:  libzip-devel curl-devel binutils-devel cmake
BuildRequires:  hawknl-devel >= 1.68-22
# rhbz#818911
BuildRequires:  binutils-static
Requires:       hicolor-icon-theme
# for people who try to install this using upstream capitalization
Provides:       OpenLieroX = %{version}-%{release}

%description
OpenLierox is an extremely addictive realtime multi-player 2D shoot-em-up
backed by an active gaming community. Dozens of levels and mods are available
to provide endless gaming pleasure.

%prep
%autosetup -p1 -n OpenLieroX
sed -i 's/\r//g' doc/original_lx_docs/*.*
cp -a %{SOURCE2} .
# Remove bundled libs to ensure they are not used
for i in libs/*; do
    if [ "$i" = "libs/pstreams" -o "$i" = "libs/linenoise" ]; then
        # Except for the pstreams and linenoise copylibs
        continue
    fi
    rm -r "$i"
done
# Remove execute permissions from various data files
find -type f -print0 | xargs -0 chmod -x
# Drop obsolete Python 2 scripts which are only for people running a
# dedicated server (which we do not package)
rm -rf share/gamedir/scripts share/gamedir/cfg/*.py

%build
%cmake -DDEBUG=OFF -DHAWKNL_BUILTIN=OFF -DBREAKPAD=OFF -DSYSTEM_DATA_DIR=%{_datadir}
# The CMakefile is not written with out of tree builds in minds. It expects
# this dir, which is part of the source-tree, to be present
mkdir %{_vpath_builddir}/bin
%cmake_build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/OpenLieroX
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -m 755 %{_vpath_builddir}/bin/%{name} $RPM_BUILD_ROOT%{_bindir}
cp -pr share/gamedir/* $RPM_BUILD_ROOT%{_datadir}/OpenLieroX
install -p -m 644 doc/%{name}.6 $RPM_BUILD_ROOT%{_mandir}/man6

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 share/OpenLieroX.svg \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 share/%{name}.appdata.xml \
  $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc README.fedora doc/original_lx_docs/*
%license COPYING.LIB
%{_bindir}/%{name}
%{_datadir}/OpenLieroX
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man6/%{name}.6*

%changelog
%autochangelog
