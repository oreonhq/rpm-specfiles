%global source0_hash 30936feca234addcf7dbc58961750a0efe87023284a4a2f0fe36adeb44daaf91
Name: kiwix-desktop
Version: 2.5.1
Release:        1%{?dist}
License: GPL-3.0-or-later
Summary:        Kiwix desktop application
URL: https://github.com/kiwix/%{name}
Source0:        https://github.com/kiwix/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires: aria2%{?_isa}
Requires: hicolor-icon-theme
Requires: qt6-qtsvg%{?_isa}
Requires: shared-mime-info
ExclusiveArch: %{qt6_qtwebengine_arches}
# oreon:deps
BuildRequires:  aria2
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libkiwix-devel
BuildRequires:  libzim-devel
BuildRequires:  make
BuildRequires:  mustache-devel
BuildRequires:  pugixml-devel
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  qtsingleapplication-qt6-devel
# /oreon:deps
%description
The Kiwix-desktop is a view/manager of zim files for GNU/Linux
and Windows. You can download and view your zim files as you
which.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
mkdir %{_vpath_builddir}
sed -e "/-Werror/d" -e "/static {/,+2d" -i %{name}.pro
rm -rf subprojects

%build

pushd %{_vpath_builddir}
    %qmake_qt6 PREFIX=%{_prefix} CONFIG+=qtsingleapplication ..
popd
%make_build -C %{_vpath_builddir}
%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_vpath_builddir}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
