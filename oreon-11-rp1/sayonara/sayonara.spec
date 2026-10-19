%global source0_hash f24a8a9dfc9f0d2764e31c79bee852de088cd9c41b6ccf8a4ba32f6fb1f8f4d8
%global __cmake_in_source_build 1
%global prerel beta2
%global stable 1
%global stable_ver stable2
Summary:        A lightweight Qt Audio player
License:        GPL-3.0-or-later
URL:            http://sayonara-player.com
Name:           sayonara
%if 0%{?stable}
Version:        1.11.0
Release:        1%{?dist}
Source0:        https://gitlab.com/luciocarreras/%{name}-player/-/archive/%{version}-%{stable_ver}/%{name}-player-%{version}-%{stable_ver}.tar.bz2
%else
Version:        1.10.0
Release:        1%{?dist}
%endif
Requires:       qt5-qtsvg
Requires:       hicolor-icon-theme
Requires:       gstreamer1-plugins-bad-free
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  libappstream-glib
BuildRequires:  libmtp-devel
BuildRequires:  libnotify-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  taglib-devel
# /oreon:deps
%description
%{name} is a small, clear, not yet platform-independent music player. Low 
CPU usage, low memory consumption and no long loading times are only three 
benefits of this player. Sayonara should be easy and intuitive to use and 
therefore it should be able to compete with the most popular music players.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains html documentation
that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?stable}
%autosetup -p1 -n %{name}-player-%{version}-%{stable_ver}
%else
%autosetup -p1 -n %{name}-player-%{version}-%{prerel}
%endif

sed -i -e 's|1.11.0-stable1|1.11.0-stable2|' CMakeLists.txt

rm -rf .gitignore .gitlab-ci.yml debian
# use system taglib
rm -rf src/3rdParty/Taglib

%build

%cmake . -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
         -DWITH_DOC=ON                       \
         -DWITH_SYSTEM_TAGLIB=ON             \
         -DCMAKE_INSTALL_PREFIX=%{_prefix}
%cmake_build
doxygen -u docs/doxygen.cfg
doxygen docs/doxygen.cfg
%install
%cmake_install
rm -rf %{buildroot}/%{_datadir}/menu
%find_lang %{name} --all-name --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n sayonara-doc -f %{oreon_filedir}/sayonara-doc.list

%changelog

%autochangelog
