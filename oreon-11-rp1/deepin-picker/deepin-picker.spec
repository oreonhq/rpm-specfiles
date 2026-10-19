%global source0_hash 380eb45f5bce47d2e7b1e93011217d354e12eb67bca2c86add246233ec7c4c58
Name:           deepin-picker
Version:        6.0.12
Release:        1%{?dist}
Summary:        A color picker tool for deepin
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/%{name}
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0002: 0002-Fix-lang-code-in-desktop-entry-file.patch
%if 0%{?openeuler}
%else
Requires:      hicolor-icon-theme
%endif
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXtst-devel
BuildRequires:  libxcb-devel
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dtkgui)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  qt5-linguist
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export PATH=%{_qt5_bindir}:$PATH
mkdir build && pushd build
%qmake_qt5 ../
%make_build
popd
%install
%make_install -C build INSTALL_ROOT="%buildroot"
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
