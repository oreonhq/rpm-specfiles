%global source0_hash cb1ff08025bac74f4c891ce96382a0c6725a3aafd6d5a5221b9c1649de42b67c

Name:           admeshgui
%global         camelname ADMeshGUI
Version:        1.0.1
Release:        %autorelease
Summary:        STL viewer and manipulation tool
# Code is AGPLv3 logo/license is LGPLv3 or CC-BY-SA
# Automatically converted from old format: AGPLv3 and (LGPLv3 or CC-BY-SA) - review is highly recommended.
License:        AGPL-3.0-only AND (LGPL-3.0-only OR LicenseRef-Callaway-CC-BY-SA)
URL:            https://github.com/vyvledav/%{camelname}
Source0:        https://github.com/vyvledav/%{camelname}/archive/v%{version}.tar.gz

# https://github.com/admesh/ADMeshGUI/commit/1732bc83cb2c949089d98cd9be0e922ac4af4a28
Patch0:         %{name}-qt571.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libadmesh) >= 0.98.2
BuildRequires:  pkgconfig(Qt5Core) >= 5.4
BuildRequires:  pkgconfig(Qt5Gui) >= 5.4
BuildRequires:  pkgconfig(Qt5OpenGL) >= 5.4
BuildRequires:  pkgconfig(Qt5Svg) >= 5.4
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4
BuildRequires:  pkgconfig(Qt5) >= 5.4
BuildRequires:  stlsplit-devel
BuildRequires: make

Requires:       hicolor-icon-theme

Provides:       %{camelname}%{_isa} = %{version}-%{release}
Provides:       %{camelname} = %{version}-%{release}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif

%description
Extension for ADMesh tool in the form of graphical user interface. ADMesh tool
allows to manipulate and repair 3D models in the STL format. This graphical
user interface allows the user to view the model in 3D viewer, to perform
selected actions and to get visual feedback of those.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{camelname}-%{version}

%build
%{qmake_qt5} PREFIX=%{buildroot}/usr
make %{?_smp_mflags}

%install
make install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files
%license LICENSE LOGO-LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/appdata/admeshgui.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/symbolic/apps/%{name}-symbolic.svg

%changelog
%autochangelog
