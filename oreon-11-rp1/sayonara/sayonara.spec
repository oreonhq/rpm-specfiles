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
Release:        4.%{stable_ver}%{?dist}
#Release:        3%%{?dist}
Source0:        https://gitlab.com/luciocarreras/sayonara-player/-/archive/%{version}-%{stable_ver}/sayonara-player-%{version}-%{stable_ver}.tar.bz2
%else
Version:        1.10.0
Release:        0.6.%{prerel}%{?dist}
Source0:        https://gitlab.com/luciocarreras/sayonara-player/-/archive/%{version}-%{prerel}/sayonara-player-%{version}-%{prerel}.tar.bz2
%endif

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  libappstream-glib
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  libnotify-devel
BuildRequires:  taglib-devel
BuildRequires:  libmtp-devel
Requires:       qt5-qtsvg
Requires:       hicolor-icon-theme
Requires:       gstreamer1-plugins-bad-free
ExcludeArch:    %{ix86}

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

# build docs
# update Doxyfile
doxygen -u docs/doxygen.cfg
# build docs
doxygen docs/doxygen.cfg

%install
%cmake_install

# remove menu dir, because it's not necessary
rm -rf %{buildroot}/%{_datadir}/menu

%find_lang %{name} --all-name --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files -f %{name}.lang
%license LICENSE
%doc MANUAL README.md INSTALL.md
%{_bindir}/%{name}
%{_bindir}/%{name}-ctl
%{_bindir}/%{name}-query
%{_datadir}/applications/com.%{name}-player.Sayonara.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/metainfo/com.%{name}-player.Sayonara.appdata.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%dir %{_datadir}/%{name}/translations/icons
%{_datadir}/%{name}/translations/icons/*.png
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/%{name}-ctl.1.gz
%{_mandir}/man1/%{name}-query.1.gz

%files doc
#doc docs/html
%{_datadir}/doc/%{name}/doxygen/html

%changelog
%autochangelog
