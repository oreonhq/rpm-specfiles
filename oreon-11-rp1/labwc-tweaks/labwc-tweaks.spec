%global source0_hash 1ceaec80ebee898fb70b5d0cd28907fe5ebfca7fac4c339f200ebc431d1d42ba

%global commit 694d0b0d326e95168c7b2e034504c8bd112d1702
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20260128

Name:           labwc-tweaks
Version:        0.1.0~git%{commitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        GUI configuration app for labwc

License:        GPL-2.0-only and BSD-3-Clause
URL:            https://github.com/labwc/labwc-tweaks
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0:         0001-add-unistd_h.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  perl-interpreter

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)

Requires:       labwc

%description
labwc-tweaks is a GUI configuration application for the labwc wayland
compositor

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -S git_am

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/labwc_tweaks.desktop

%files -f %{name}.lang
%license LICENSE BSD-3-Clause
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/metainfo/labwc_tweaks.appdata.xml

%changelog
%autochangelog
