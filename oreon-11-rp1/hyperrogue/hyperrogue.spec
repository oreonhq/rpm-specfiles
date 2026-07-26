%global source0_hash none

%global version_tag 13.0w
%global _lto_cflags %nil

Name:           hyperrogue
Version:        13.0
Release:        4.w%{?dist}
Summary:        An SDL roguelike in a non-euclidean world

# The game is under the GPLv2 (savepng.* is under zlib) and the music under CC-BY-SA (v3) and sounds under CC-BY-SA 4.0, CC-BY 4.0 and CC0
# Automatically converted from old format: GPLv2 and BSD and zlib - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-BSD AND Zlib
URL:            http://www.roguetemple.com/z/hyper/
Source0:        https://github.com/zenorogue/hyperrogue/archive/v%{version_tag}/%{name}-%{version_tag}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Source3:        http://roguetemple.com/z/hyper/bigicon-osx.png
Patch0:         %{name}-gccfix.patch

BuildRequires:  gcc, gcc-c++
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel, SDL_ttf-devel, SDL_gfx-devel
BuildRequires:  libpng-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  glew-devel
BuildRequires: make

Requires: dejavu-sans-fonts

Provides: bundled(mtrand)
Provides: bundled(savepng)

Requires: %{name}-data

# Hmm.. it seems that hyperrogue does not build on 32-bit arm anymore?
# "as: out of memory allocating 32 bytes after a total of 3020046336 bytes"
# https://kojipkgs.fedoraproject.org//work/tasks/8579/50098579/build.log
ExcludeArch: armv7hl

%description
You are a lone outsider in a strange, non-Euclidean world.
Fight to find treasures and get the fabulous Orbs of Yendor!

%package data
Requires: %{name}
Obsoletes:     %{name}-music < 12.0
Summary: Data for hyperrogue
BuildArch: noarch
# Automatically converted from old format: CC-BY - review is highly recommended.
License: LicenseRef-Callaway-CC-BY

%description data
Data files for hypperrogue.

%prep
%setup -q -n %{name}-%{version_tag}
%patch -P0 -p1

%build
%make_build CXXFLAGS="%{optflags} -Wno-invalid-offsetof -I%{_includedir}/SDL -DHYPERPATH=\\\"%{_datadir}/%{name}/\\\" -DHYPERFONTPATH=\\\"%{_datadir}/fonts/dejavu-sans-fonts/\\\""

%install
# Upstream not provides "install" target. I have to install files "by hands".
mkdir -p %{buildroot}%{_bindir}
install -pDm755 -p hyperrogue %{buildroot}%{_bindir}/%{name}

# Install music files.
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

# Install the desktop file.
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -pDm644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Install the appdata file.
mkdir %{buildroot}%{_datadir}/appdata/
install -pDm644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/

%check
#Test the appdata file.
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%files
#%%license COPYING
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_defaultdocdir}/%{name}/README.md

%files data
%{_datadir}/%{name}

%changelog
%autochangelog
