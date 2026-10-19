%global source0_hash 73b3f29e32aae6b4f6cf874008a6a0d302e15f602a62e6378cdf258fc8719d74
%global provider org.rncbc.qpwgraph
Name:           qpwgraph
Version:        1.0.4
Release:        1%{?dist}
Summary:        PipeWire Graph Qt GUI Interface
License:        GPL-2.0-or-later
URL:            https://gitlab.freedesktop.org/rncbc/%{name}
Source0:        https://gitlab.freedesktop.org/rncbc/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Requires:       hicolor-icon-theme
Requires:       shared-mime-info
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  qt6-qtsvg-devel
# /oreon:deps
%description
qpwgraph is a graph manager dedicated to PipeWire, using the Qt C++ framework,
based and pretty much like the same of QjackCtl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{name}-v%{version}

%build

%cmake \
  -DCMAKE_BUILD_TYPE=Release
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{provider}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
