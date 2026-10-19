%global source0_hash c72ae438b7ce8bf04c20ae30c33cc23b5243d340f4b486f09b51893b816f7d73
Name:           plasma-smart-video-wallpaper-reborn
Version:        2.14.1
Release:        1%{?dist}
Summary:        Play videos on your Plasma 6 Desktop/Lock Screen
License:        GPL-2.0-only
URL:            https://github.com/luisbocanegra/plasma-smart-video-wallpaper-reborn
Source0:        https://github.com/luisbocanegra/%{name}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       plasma-desktop
Requires:       qt6-qtmultimedia
Recommends:     ffmpeg-free
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(Plasma)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
# /oreon:deps
%description
Plasma 6 wallpaper plugin to play videos on your Desktop/Lock Screen.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%find_lang plasma_wallpaper_luisbocanegra.smart.video.wallpaper.reborn
chmod 755 %{buildroot}%{_datadir}/plasma/wallpapers/luisbocanegra.smart.video.wallpaper.reborn/contents/ui/tools/gdbus_get_signal.sh
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
