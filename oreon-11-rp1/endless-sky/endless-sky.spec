%global source0_hash 066b4c171fa7756b4c538a81e9926d4d7686cdbbe44fb5ab2c83e137a7493278
Name:		endless-sky
Version:	0.11.2
Release:        1%{?dist}
Summary:        Space exploration, trading, and combat game
License:	GPL-3.0-only
URL:		https://%{name}.github.io
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	endless-sky-wrapper
Patch0:		endless-sky-0.10.0-remove-games-path.patch
Requires:	%{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  catch-devel
BuildRequires:  cmake
BuildRequires:  cmake(flac)
BuildRequires:  cmake(ogg)
BuildRequires:  desktop-file-utils
BuildRequires:  flac
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  libappstream-glib
BuildRequires:  libasan
BuildRequires:  libavif-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libmad-devel
BuildRequires:  libpng-devel
BuildRequires:  libubsan
BuildRequires:  libuuid-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  ninja-build
BuildRequires:  openal-soft-devel
# /oreon:deps
%description
Explore other star systems. Earn money by trading, carrying passengers, or
completing missions. Use your earnings to buy a better ship or to upgrade the
weapons and engines on your current one. Blow up pirates. Take sides in a civil
war. Or leave human space behind and hope to find some friendly aliens whose
culture is more civilized than your own...

%package data
Summary:	Game data for %{name}
License:	Public Domain and CC-BY-SA
BuildArch:	noarch
%description data
Images, sound, and game data for %{name}.

%prep
%oreon_prep
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n endless-sky-data -f %{oreon_filedir}/endless-sky-data.list

%changelog

%autochangelog
