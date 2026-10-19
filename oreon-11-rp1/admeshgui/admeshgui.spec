%global source0_hash cb1ff08025bac74f4c891ce96382a0c6725a3aafd6d5a5221b9c1649de42b67c
Name:           admeshgui
%global         camelname ADMeshGUI
Version:        1.0.1
Release:        1%{?dist}
Summary:        STL viewer and manipulation tool
License:        AGPL-3.0-only AND (LGPL-3.0-only OR LicenseRef-Callaway-CC-BY-SA)
URL:            https://github.com/vyvledav/%{camelname}
Source0:        https://github.com/vyvledav/%{camelname}/archive/v%{version}.tar.gz
Patch0:         %{name}-qt571.patch
Requires:       hicolor-icon-theme
Provides:       %{camelname}%{_isa} = %{version}-%{release}
Provides:       %{camelname} = %{version}-%{release}
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
ExcludeArch:    %{ix86}
%endif
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libadmesh)
BuildRequires:  stlsplit-devel
# /oreon:deps
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
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
