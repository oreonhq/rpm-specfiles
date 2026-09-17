%global source0_hash 6316334f71b3c6aa68ee6cf0c726429f6017c99deb74b8ec418324ab54be027d

%global fullname net.sourceforge.Lifeograph

Name:       lifeograph
Version:    3.0.4
Release:    %autorelease
Summary:    A diary program

License:    GPL-3.0-or-later
URL:        https://lifeograph.sourceforge.net/
Source0:    https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.xz

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
Requires:       hicolor-icon-theme

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

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{fullname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f %{fullname}.lang
%doc AUTHORS NEWS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{fullname}.png
%{_datadir}/icons/hicolor/*/mimetypes/application-x-lifeographdiary.png
%{_datadir}/icons/hicolor/scalable/apps/%{fullname}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{fullname}-symbolic.svg

%{_datadir}/%{fullname}
%{_datadir}/applications/%{fullname}.desktop
%{_metainfodir}/%{fullname}.metainfo.xml
%{_mandir}/man1/%{name}*
%{_datadir}/mime/packages/*%{name}*

%changelog
%autochangelog
