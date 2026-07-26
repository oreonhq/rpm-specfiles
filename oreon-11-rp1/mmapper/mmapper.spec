%global source0_hash c22ebb6aa83847970982682fad52e26a1469212b8703386874b70e1d05eaa994

Name:           mmapper
Version:        24.03.1
Release:        10%{?dist}
Summary:        Graphical MUME mapper

License:        GPL-2.0-or-later
URL:            https://github.com/MUME/MMapper
Source0:        https://github.com/MUME/MMapper/archive/v%{version}/MMapper-%{version}.tar.gz
Source1:        https://github.com/g-truc/glm/releases/download/0.9.9.7/glm-0.9.9.7.zip
Patch0:         %{name}-miniupnp228.patch
Patch1:         0001-Add-missing-include-for-uint64_t.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  /usr/bin/appstream-util
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  miniupnpc-devel
BuildRequires:  openssl-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  zlib-devel

Requires:       hicolor-icon-theme

Provides:       bundled(glm) = 0.9.9.7

%description
MMapper is a graphical mapper for a MUD named MUME (Multi-Users in Middle
Earth). The game is traditionally played in a text-only mode, but MMapper tries
to represent the virtual world in user-friendly graphical environment. It acts
as a proxy between a telnet client and a MUD server, being able to analyze game
data in real time and show player's position in a map.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n MMapper-%{version}

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

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.mume.MMapper.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.mume.MMapper.desktop

%files
%license COPYING.txt
%doc NEWS.txt
%{_bindir}/mmapper
%{_datadir}/applications/org.mume.MMapper.desktop
%{_datadir}/icons/hicolor/*/apps/org.mume.MMapper.png
%{_datadir}/metainfo/org.mume.MMapper.appdata.xml

%changelog
%autochangelog
