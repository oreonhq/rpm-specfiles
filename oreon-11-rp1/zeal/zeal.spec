%global source0_hash 0af711d8a37c4355b8e914855a637f47d0fd3ca8c66ba239523a65d45d5a15f5

Name:           zeal
Version:        0.9.1
Release:        %autorelease
Summary:        Offline documentation browser inspired by Dash

License:        GPL-3.0-or-later
URL:            https://zealdocs.org/
Source:         https://github.com/zealdocs/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:  cmake(Qt6Core) >= 6.2.0
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6Network)

BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
Requires:       hicolor-icon-theme

%description
Zeal is a simple offline documentation browser inspired by Dash.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
# turn off shared libs building:
# - it's only used from Zeal itself
# - build scripts not configured to install the lib
%cmake_qt6 \
  -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.zealdocs.zeal.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.zealdocs.zeal.appdata.xml

%files
%license COPYING
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/applications/org.zealdocs.zeal.desktop
%{_metainfodir}/org.zealdocs.zeal.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
%autochangelog
