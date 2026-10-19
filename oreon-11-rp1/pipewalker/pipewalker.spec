%global source0_hash 59c4746a1b3c703fb498792e9b54d3295b73b24bbbcc39565d41b14e1daf6b18
Name: pipewalker
Summary:        Puzzle game about connecting components into a single circuit
License: MIT
Version: 1.1
Release:        6%{?dist}
URL: https://github.com/artemsen/pipewalker
Source0:        https://github.com/artemsen/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
Source11: %{name}.metainfo.xml
Patch2: 0002-no-games-subdir-for-data.patch
Patch3: 0003-fix-levels-being-already-solved.patch
Patch4: 0004-missing-includes.patch
Requires: hicolor-icon-theme
Requires: %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  meson
# /oreon:deps
%description
PipeWalker is a puzzle game in which you need to combine the components
into a single circuit: connect all computers to a network server,
bring water to the taps, etc.

%package data
Summary: Data files for PipeWalker
BuildArch: noarch
%description data
This package provides data files (themes and sounds effects)
required to play PipeWalker.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix violation of Icon Theme Specification
sed -e 's/^Icon=pipewalker\.xpm$/Icon=pipewalker/' -i extra/%{name}.desktop

%build

%meson -Dversion=%{version}
cat %{_vpath_builddir}/buildcfg.h
%meson_build
%install
%meson_install
install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 -p %{SOURCE11} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n pipewalker-data -f %{oreon_filedir}/pipewalker-data.list

%changelog

%autochangelog
