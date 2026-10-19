%global source1_hash 6b79c3d06d9745d1cce3f38c0c15666596f9aefff25ddb74df3af0a02f011ee1
%global source0_hash c22ebb6aa83847970982682fad52e26a1469212b8703386874b70e1d05eaa994
Name:           mmapper
Version:        24.03.1
Release:        1%{?dist}
Summary:        Graphical MUME mapper
License:        GPL-2.0-or-later
URL:            https://github.com/MUME/MMapper
Source0:        https://github.com/MUME/MMapper/archive/v%{version}/MMapper-%{version}.tar.gz
Source1:        https://github.com/g-truc/glm/releases/download/0.9.9.7/glm-0.9.9.7.zip
Patch0:         %{name}-miniupnp228.patch
Patch1:         0001-Add-missing-include-for-uint64_t.patch
ExcludeArch:    %{ix86}
Requires:       hicolor-icon-theme
Provides:       bundled(glm) = 0.9.9.7
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  miniupnpc-devel
BuildRequires:  openssl-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
MMapper is a graphical mapper for a MUD named MUME (Multi-Users in Middle
Earth). The game is traditionally played in a text-only mode, but MMapper tries
to represent the virtual world in user-friendly graphical environment. It acts
as a proxy between a telnet client and a MUD server, being able to analyze game
data in real time and show player's position in a map.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir MMapper-%{version}
%oreon_prep
%build

mkdir -p %{__cmake_builddir}/external/glm/glm-prefix/src
cp -a %{S:1} %{__cmake_builddir}/external/glm/glm-prefix/src/
%{cmake} \
  -DCMAKE_BUILD_TYPE=Release \
  -DWITH_MAP=OFF \
  -DWITH_UPDATER=OFF \
  %{nil}
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.mume.MMapper.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.mume.MMapper.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
