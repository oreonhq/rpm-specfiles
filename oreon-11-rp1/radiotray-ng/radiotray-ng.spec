%global source0_hash 94746f1111c7cd162cf8cbccf7dadeab3dadbb125227cb6ce8ef0b284a35f343

Name:           radiotray-ng
Version:        0.2.9
Release:        6%{?dist}
Summary:        Internet radio player

License:        GPL-3.0-or-later
URL:            https://github.com/ebruck/radiotray-ng
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# radiotray-ng-0.2.9/include/radiotray-ng/i_radiotray_ng.hpp:76:37:
#   error: ‘uint32_t’ has not been declared
Patch0:         radiotray-ng-0.2.9-include_cstdint.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  boost-devel
BuildRequires:  wxGTK-devel
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libxdg-basedir)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme

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
# Remove autostart
rm %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop
# Remove themes
rm -rf %{buildroot}%{_datadir}/icons/Yaru
rm -rf %{buildroot}%{_datadir}/icons/breeze
# Remove self-installed license file
rm %{buildroot}%{_datadir}/licences/%{name}/COPYING
#Remove unneeded script
rm %{buildroot}%{_bindir}/rt2rtng

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/rtng-bookmark-editor.desktop

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_bindir}/rtng-bookmark-editor
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/rtng-bookmark-editor.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/%{name}

%changelog
%autochangelog
