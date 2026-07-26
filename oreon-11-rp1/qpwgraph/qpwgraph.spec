%global source0_hash ae7b043b69605e2ea0947e86207fe43e0f38fb865b94c4c2086c7e19c1b64091

%global provider org.rncbc.qpwgraph

Name:           qpwgraph
Version:        1.0.0
Release:        1%{?dist}
Summary:        PipeWire Graph Qt GUI Interface
# Main license is GPL-2.0-or-later in sources,
License:        GPL-2.0-or-later
URL:            https://gitlab.freedesktop.org/rncbc/%{name}
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme
Requires:       shared-mime-info

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

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{provider}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/%{provider}.desktop
%{_metainfodir}/%{provider}.metainfo.xml
%{_datadir}/mime/packages/%{provider}.xml
%{_mandir}/man1/qpwgraph.1.gz

%changelog
%autochangelog
