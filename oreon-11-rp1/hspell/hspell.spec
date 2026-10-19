%global source0_hash 7310f5d58740d21d6d215c1179658602ef7da97a816bc1497c8764be97aabea3
Summary:        A Hebrew spell checker
Name: hspell
Version: 1.4
Release:        1%{?dist}
License: AGPL-3.0-only
URL: http://hspell.ivrix.org.il/
Source0:        http://hspell.ivrix.org.il/%{name}-%{version}.tar.gz
Patch0: 0001-require-local-module-explicitly.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  hunspell-devel
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  zlib-devel
# /oreon:deps
%description
Hspell is a Hebrew SPELLer and morphological analyzer. It provides a mostly
spell-like interface (gives the list of wrong words in the input text), but can
also suggest corrections (-c). It also provides a true morphological analyzer
(-l), that prints all known meanings of a Hebrew string.
Hspell 1.4 still follows the old (pre June 2017) spelling standard of the
Academy of the Hebrew Language.

%description -l he
Hspell הוא מאיית ומנתח צורני עברי, המספק מנשק דמוי-spell - פולט רשימה של המילים
השגויות המופיעות בקלט. Hspell מקפיד מאוד כללי האקדמיה העברית לכתיב חסר ניקוד
("כתיב מלא").  כמו כן, Hspell מספק (-l) מנתח מורפולוגי אשר מדפיס את כל
המשמעויות האפשריות של מחרוזת אותיות עברית.
גרסה 1.4 תואמת עדיין לכללי האיות הישנים (טרם יוני 2017) של האקדמיה.

%package devel
Summary: Library and include files for Hspell, the Hebrew spell checker
Requires: %{name} = %{version}-%{release}
%description devel
Library and include files for applications that want to use Hspell.

%description -l he devel
ספרייה וקובצי כותרת עבור יישומים שרוצים להשתמש ב-Hspell.

%package -n hunspell-he
Summary: Hebrew hunspell dictionaries
Requires: hunspell
%description -n hunspell-he
Hebrew hunspell dictionaries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P 0 -p1 -b .localreq
/usr/bin/iconv -f hebrew -t utf8 -o WHATSNEW WHATSNEW

%build

%configure --enable-fatverb --enable-linginfo --enable-shared
make
make hunspell
%install
make DESTDIR=$RPM_BUILD_ROOT STRIP=: install
rm -f $RPM_BUILD_ROOT/%{_libdir}/libhspell.a
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp -p he.dic $RPM_BUILD_ROOT/%{_datadir}/hunspell/he_IL.dic
cp -p he.aff $RPM_BUILD_ROOT/%{_datadir}/hunspell/he_IL.aff
%oreon_autofiles hunspell-he usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

! make test | grep FAILED | grep -E -v '1/aspell/[489]'
%files -f %{oreon_filedir}/main.list
%files -n hspell-devel -f %{oreon_filedir}/hspell-devel.list
%files -n hunspell-he -f %{oreon_filedir}/hunspell-he.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4-25
- Prepare for Oreon 11 (RP1)
