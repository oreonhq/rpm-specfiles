%global source0_hash 93b68ff1d717db1b745469238d88fdca9a29e87d4b25e97a0410fa8fc7f558d4
%global forgeurl https://github.com/francescmaestre/%{upstream_package_name}
%global tag v%{version}
%global upstream_package_name GitQlient
Name:       gitqlient
Version:    1.6.3
%forgemeta
Release:        1%{?dist}
Summary:        Multi-platform Git client written with Qt
ExclusiveArch: %{qt5_qtwebengine_arches}
License:    LGPL-2.1-or-later
URL:        %{forgeurl}
Source0:        %{forgeurl}/releases/download/%{tag}/%{name}_%{version}.tar.gz
Requires:   git-core
Requires:   hicolor-icon-theme
Requires:   qt5-qtsvg
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
# /oreon:deps
%description
GitQlient, pronounced as git+client (/gɪtˈklaɪənt/) is a multi-platform Git
client originally forked from QGit. Nowadays it goes beyond of just a fork and
adds a lot of new functionality.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}_%{version}
%oreon_prep
%build

%qmake_qt5 \
    PREFIX=%{_prefix} \
    %{upstream_package_name}.pro \
    %{nil}
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
