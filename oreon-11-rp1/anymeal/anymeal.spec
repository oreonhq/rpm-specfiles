%global source2_hash 70479f0e13d1e41e0c862a07351c68dd486c3ecceadcdf19351b9b6520e300d3
%global source0_hash 75be857dc4ca0b673d0937775e2bb6267d5dc538880ba0cd38a092c2346f84df
Summary:        A free and open source recipe management software
Name:     anymeal
License:  GPL-3.0-or-later
Version:  1.33
Release:        1%{?dist}
URL:      https://github.com/wedesoft/anymeal
Source0:        https://github.com/wedesoft/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:  %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:  https://www.wedesoft.de/gnupg-wedekind.asc
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  recode-devel
BuildRequires:  which
# /oreon:deps
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
%oreon_autofiles main

%check

make check
desktop-file-validate %{buildroot}/%{_datadir}/applications/de.wedesoft.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/de.wedesoft.%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
