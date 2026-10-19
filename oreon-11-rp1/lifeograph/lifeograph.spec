%global source0_hash e20a602621bedb51e8013c4a308e105d4d85af24a7b5db3193ed8d284f44e061
%global fullname net.sourceforge.Lifeograph
Name:       lifeograph
Version:    3.1.4
Release:        1%{?dist}
Summary:        A diary program
License:    GPL-3.0-or-later
URL:        https://lifeograph.sourceforge.net/
Source0:        https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.xz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  enchant2-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtkmm4.0-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libchamplain-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libshumate-devel
BuildRequires:  meson
# /oreon:deps
%description
Lifeograph is a diary program to take personal notes on life. It has all
essential functionality expected in a diary program and strives to have
a clean and streamlined user interface.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
sed -i 's|<build_time.h>|"build_time.h"|' src/lifeograph.cpp
# We don't want it do anything, so we clear it out
echo "#!/usr/bin/python3" > meson_post_install.py
echo "print('no op')" >> meson_post_install.py

%build

./create_time_build_time_header.sh %{name} ./src/ ./src/
find . -name "build_time.h" -print
%meson
%meson_build
%install
%meson_install
%find_lang %{fullname}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{fullname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
