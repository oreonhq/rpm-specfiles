%global source0_hash 9e77f4b532425b0569b8a437d6d6b2bed489b68cc7a7d9578ee48d81bd7fcf0d
%global srcname Projecteur
Name:           projecteur
Version:        0.10
Release:        1%{?dist}
Summary:        Virtual pointer for the Logitech Spotlight presentation remote
License:        MIT
URL:            https://github.com/jahnf/Projecteur
Source0:        https://github.com/jahnf/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Requires:       hicolor-icon-theme
Requires:       systemd-udev
Recommends:     bash-completion
Suggests:       gnome-shell-extension-appindicator
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  systemd-devel
# /oreon:deps
%description
Projecteur is a virtual laser pointer for use with inertial pointers such as
the Logitech Spotlight. Projecteur can show a colored dot, a highlighted circle
or a zoom effect to act as a pointer. The location of the pointer moves in
response to moving the handheld pointer device. The effect is much like that of
a traditional laser pointer, except that it is captured by recording software
and works across multiple screens.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

%cmake -D CMAKE_INSTALL_UDEVRULESDIR="%{_udevrulesdir}"
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
desktop-file-validate \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
