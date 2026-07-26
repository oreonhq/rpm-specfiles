%global source0_hash none

Name:		endless-sky
Version:	0.11.0
Release:	1%{?dist}
Summary:	Space exploration, trading, and combat game

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://%{name}.github.io
Source0:	https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	endless-sky-wrapper
# Replace /usr/games with /usr/bin and /usr/share/games with /usr/share per
# https://fedoraproject.org/wiki/SIGs/Games/Packaging.
# Patch not submitted upstream. Upstream conforms to Debian packaging
# standards where the use of /usr/games is acceptable.
Patch0:		endless-sky-0.10.0-remove-games-path.patch

Requires:	%{name}-data = %{version}-%{release}
BuildRequires:	cmake
BuildRequires:  ninja-build
BuildRequires:	gcc-c++
BuildRequires:	SDL2-devel
BuildRequires:	openal-soft-devel
BuildRequires:	glew-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libappstream-glib
BuildRequires:	desktop-file-utils
BuildRequires:	libmad-devel
BuildRequires:	libuuid-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  catch-devel
BuildRequires:  libasan
BuildRequires:  libubsan
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  cmake(flac)
BuildRequires:  flac
BuildRequires:  libavif-devel
BuildRequires:  cmake(ogg)

%description
Explore other star systems. Earn money by trading, carrying passengers, or
completing missions. Use your earnings to buy a better ship or to upgrade the
weapons and engines on your current one. Blow up pirates. Take sides in a civil
war. Or leave human space behind and hope to find some friendly aliens whose
culture is more civilized than your own...

%package data
Summary:	Game data for %{name}
# Sound and images appear to be a mix of Public Domain and CC-BY-SA licensing
# See copyright for details.
License:	Public Domain and CC-BY-SA
BuildArch:	noarch

%description data
Images, sound, and game data for %{name}.

%prep
%autosetup -p1

%build
%cmake -DES_USE_VCPKG=OFF
%cmake_build

%check
appstream-util validate-relax --nonet io.github.endless_sky.endless_sky.appdata.xml
desktop-file-validate io.github.endless_sky.endless_sky.desktop

%install
%cmake_install
mkdir -p %{buildroot}%{_bindir}
install redhat-linux-build/%{name}  %{buildroot}%{_bindir}/%{name}.bin
install -m755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}
sed -i 's|/app|%{_prefix}|g' %{buildroot}%{_bindir}/%{name}
rm -f %{buildroot}%{_datadir}/doc/endless-sky/license.txt

%files
%doc README.md changelog copyright
%license license.txt
%{_bindir}/%{name}*
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/applications/io.github.endless_sky.endless_sky.desktop
%{_datadir}/metainfo/io.github.endless_sky.endless_sky.appdata.xml
%{_mandir}/man6/%{name}.6.gz

%files data
%license copyright
%{_datadir}/%{name}

%changelog
%autochangelog
