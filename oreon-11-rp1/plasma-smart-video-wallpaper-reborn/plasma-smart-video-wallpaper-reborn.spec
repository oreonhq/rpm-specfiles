%global source0_hash 67f7aeef28f4a88c3608f1a093850ff7164fca2f6af91022712171eba41792d7

Name:           plasma-smart-video-wallpaper-reborn
Version:        2.9.0
Release:        1%{?dist}
Summary:        Play videos on your Plasma 6 Desktop/Lock Screen
License:        GPL-2.0-only
URL:            https://github.com/luisbocanegra/plasma-smart-video-wallpaper-reborn
Source0:        %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(KF6CoreAddons)

Requires:       plasma-desktop
Requires:       qt6-qtmultimedia
# Only a recommendation, in case they want to use "the other one"...
Recommends:     ffmpeg-free

%description
Plasma 6 wallpaper plugin to play videos on your Desktop/Lock Screen.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
chmod 755 %{buildroot}%{_datadir}/plasma/wallpapers/luisbocanegra.smart.video.wallpaper.reborn/contents/ui/tools/gdbus_get_signal.sh

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_datadir}/plasma/wallpapers/luisbocanegra.smart.video.wallpaper.reborn/

%changelog
%autochangelog
