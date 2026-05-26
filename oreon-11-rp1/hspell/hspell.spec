Summary: A Hebrew spell checker
Name: hspell
Version: 1.4
Release: 25%{?dist}
License: AGPL-3.0-only
URL: http://hspell.ivrix.org.il/
Source: http://hspell.ivrix.org.il/%{name}-%{version}.tar.gz
Patch0: 0001-require-local-module-explicitly.patch
# oreon url source checksums begin
%global source0_sha256 7310f5d58740d21d6d215c1179658602ef7da97a816bc1497c8764be97aabea3
%global source0_file hspell-1.4.tar.gz
# oreon url source checksums end

BuildRequires:  gcc, make, hunspell-devel
BuildRequires:  perl-generators, perl-interpreter, zlib-devel
BuildRequires:  perl(Carp), perl(FileHandle)

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/hspell-1.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7310f5d58740d21d6d215c1179658602ef7da97a816bc1497c8764be97aabea3" || { echo "oreon: Source0 SHA256 mismatch for hspell-1.4.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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

%check
# there are three known failures
! make test | grep FAILED | grep -E -v '1/aspell/[489]'

%files
%doc LICENSE README WHATSNEW COPYING
%{_bindir}/hspell
%{_bindir}/hspell-i
%{_bindir}/multispell
%{_libdir}/libhspell.so.0
%{_mandir}/man1/hspell.1*
%{_datadir}/hspell/

%files devel
%{_includedir}/*.h
%{_libdir}/libhspell.so
%{_mandir}/man3/hspell.3*

%files -n hunspell-he
%doc LICENSE
%{_datadir}/hunspell/*

%ldconfig_scriptlets

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4-25
- Prepare for Oreon 11 (RP1)
