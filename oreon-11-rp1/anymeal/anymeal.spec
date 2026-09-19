%global source0_hash 75be857dc4ca0b673d0937775e2bb6267d5dc538880ba0cd38a092c2346f84df

Summary:  A free and open source recipe management software 
Name:     anymeal
License:  GPL-3.0-or-later
Version:  1.33
Release:  5%{?dist}

URL:      https://github.com/wedesoft/anymeal
Source0:  %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:  %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:  https://www.wedesoft.de/gnupg-wedekind.asc

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  libappstream-glib
BuildRequires:  recode-devel
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  which

Requires:       hicolor-icon-theme

%description
AnyMeal is a free and open source recipe management software developed
using SQLite3 and Qt6. It can manage a cookbook with more than 250,000
MealMaster recipes, thereby allowing to import, export, search, display,
edit, and print them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version}
# cleanup moc/rcc/uic output in tarball
rm -f anymeal/{moc,qrc,ui}_*

%build

autoreconf -fi
%configure
%make_build

%install
%make_install

%find_lang %{name} --with-qt

%check
make check
desktop-file-validate %{buildroot}/%{_datadir}/applications/de.wedesoft.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/de.wedesoft.%{name}.appdata.xml

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/anymeal
%{_mandir}/man1/anymeal.1*
%{_datadir}/applications/de.wedesoft.%{name}.desktop
%{_metainfodir}/de.wedesoft.%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*.png

%changelog
%autochangelog
