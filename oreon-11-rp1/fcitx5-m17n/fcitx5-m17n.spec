%global source0_hash de94d87a2c98e983d3e3f2d2dea9cdef0f24f1161beca8a83fef741e5f2fbecf

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-m17n
Version:    5.1.6
Release:    %autorelease
Summary:    m17n Wrapper for Fcitx5
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2+
URL:        https://github.com/fcitx/fcitx5-m17n
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(fmt)
BuildRequires:  pkgconfig(m17n-gui) > 1.6.3
BuildRequires:  pkgconfig(m17n-db)
BuildRequires:  /usr/bin/appstream-util
Requires:       fcitx5-data
Requires:       pkgconfig(m17n-db)

%description
M17N is a large collection of input method, which can cover
quite a lot languages in the world, including Latin, Arabic,
etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md
%{_libdir}/fcitx5/libm17n.so
%{_datadir}/fcitx5/addon/m17n.conf
%dir %{_datadir}/fcitx5/m17n
%{_datadir}/fcitx5/m17n/default
%{_metainfodir}/org.fcitx.Fcitx5.Addon.M17N.metainfo.xml

%changelog
%autochangelog
