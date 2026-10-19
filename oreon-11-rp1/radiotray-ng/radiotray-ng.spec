%global source0_hash 94746f1111c7cd162cf8cbccf7dadeab3dadbb125227cb6ce8ef0b284a35f343
Name:           radiotray-ng
Version:        0.2.9
Release:        1%{?dist}
Summary:        Internet radio player
License:        GPL-3.0-or-later
URL:            https://github.com/ebruck/radiotray-ng
Source0:        https://github.com/ebruck/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         radiotray-ng-0.2.9-include_cstdint.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake3
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxdg-basedir)
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1
# Correct build flags
sed -i 's|-Wall -Wextra -Werror -Wpedantic|%{optflags}|' CMakeLists.txt
sed -i '/execute_process(COMMAND lsb_release/d' package/CMakeLists.txt
# Fix build with GCC 13
# https://github.com/ebruck/radiotray-ng/pull/193
sed -i "s|#include <string>|#include <string>\n#include <cstdint>|" include/radiotray-ng/i_config.hpp

%build

%cmake3 \
    -DLSB_RELEASE_EXECUTABLE="lsb_release" \
    -DDISTRIBUTOR_ID="fedora"
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop
rm -rf %{buildroot}%{_datadir}/icons/Yaru
rm -rf %{buildroot}%{_datadir}/icons/breeze
rm %{buildroot}%{_datadir}/licences/%{name}/COPYING
rm %{buildroot}%{_bindir}/rt2rtng
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/rtng-bookmark-editor.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
