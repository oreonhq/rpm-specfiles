%global source3_hash 1946079cd66bdc099f1a85412e633878bad0ec615fd15cfe5d6fe9d8c73c8091
%global source0_hash 3f82d0f0ab92c9a7d66d36599862caea279b60e876b1b0b4f69b3204f3972cb3
%global version_tag 13.0w
%global _lto_cflags %nil
Name:           hyperrogue
Version:        13.1o
Release:        1%{?dist}
Summary:        An SDL roguelike in a non-euclidean world
License:        GPL-2.0-only AND LicenseRef-Callaway-BSD AND Zlib
URL:            http://www.roguetemple.com/z/hyper/
Source0:        https://github.com/zenorogue/%{name}/archive/v%{version_tag}/%{name}-%{version_tag}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Source3:        http://roguetemple.com/z/hyper/bigicon-osx.png
Patch0:         %{name}-gccfix.patch
Requires: dejavu-sans-fonts
Provides: bundled(mtrand)
Provides: bundled(savepng)
Requires: %{name}-data
ExcludeArch: armv7hl
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  libappstream-glib
BuildRequires:  libpng-devel
BuildRequires:  make
# /oreon:deps
%description
You are a lone outsider in a strange, non-Euclidean world.
Fight to find treasures and get the fabulous Orbs of Yendor!

%package data
Requires: %{name}
Obsoletes:     %{name}-music < 12.0
Summary: Data for hyperrogue
BuildArch: noarch
License: LicenseRef-Callaway-CC-BY
%description data
Data files for hypperrogue.

%prep

%setup -q -n %{name}-%{version_tag}
%patch -P0 -p1

%build

%make_build CXXFLAGS="%{optflags} -Wno-invalid-offsetof -I%{_includedir}/SDL -DHYPERPATH=\\\"%{_datadir}/%{name}/\\\" -DHYPERFONTPATH=\\\"%{_datadir}/fonts/dejavu-sans-fonts/\\\""
%install
mkdir -p %{buildroot}%{_bindir}
install -pDm755 -p hyperrogue %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}/music
install -pDm644 music/* %{buildroot}%{_datadir}/%{name}/music/
mkdir -p %{buildroot}%{_datadir}/%{name}/sounds
install -pDm644 sounds/* %{buildroot}%{_datadir}/%{name}/sounds/
mkdir -p %{buildroot}%{_datadir}/%{name}/rogueviz
install -pDm644 rogueviz/*.cpp rogueviz/*.h %{buildroot}%{_datadir}/%{name}/rogueviz/
install -pDdm644 rogueviz/ads rogueviz/dhrg rogueviz/models rogueviz/nilrider rogueviz/sag rogueviz/som %{buildroot}%{_datadir}/%{name}/rogueviz/
install -pDm644 hyperrogue-music.txt %{buildroot}%{_datadir}/%{name}/
chmod a+x %{buildroot}%{_datadir}/%{name}/rogueviz/
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
install -pDm644 README.md %{buildroot}%{_defaultdocdir}/%{name}/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -pDm644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png
mkdir %{buildroot}%{_datadir}/appdata/
install -pDm644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n hyperrogue-data -f %{oreon_filedir}/hyperrogue-data.list

%changelog

%autochangelog
