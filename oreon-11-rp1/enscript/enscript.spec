%global source0_hash none
%global source1_hash none

Summary: A plain ASCII to PostScript converter
Name: enscript
Version: 1.6.6
Release: 38%{?dist}
# compat/regex.h,strerror.c,xalloc.{c,h} - GPL-2.0-or-later
# states/gram.{c,h}, intl/plural.c - GPL-3.0-or-later WITH Bison-exception-2.2
# intl/hash-string.c - LGPL-2.1-or-later
# compat/*, intl/* - LGPL-2.0-or-later
# afmlib/*, compat/gettext.h, docs/texinfo.tex, src/*, states/*, w32/* - GPL-3.0-or-later
# (unshipped) - ylwrap - GPL-2.0-or-later
License: LGPL-2.0-or-later AND GPL-3.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2 AND LGPL-2.1-or-later
URL: http://www.gnu.org/software/enscript
Source0:        https://mirrors.kernel.org/gnu/enscript/enscript-%{version}.tar.gz
# upstream ruby highlight stub, not shipped on gnu ftp
Source1:        ruby.st
Source2: enscript-php-1.6.4.st

Patch3:        enscript-1.6.1-locale.patch
Patch8:        enscript-wrap_header.patch
Patch10:enscript-1.6.4-rh457720.patch
Patch12:enscript-rh477382.patch
Patch13:enscript-build.patch
Patch14:enscript-manfixes.patch
Patch15:        enscript-bufpos-crash.patch
Patch16:        0001-enscript-newencodings.patch
Patch17:        enscript-CVE-vasnprintf.patch
Patch18:        enscript-c23.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf, automake, gettext
BuildRequires: gettext-devel

Provides: bundled(gnulib)

%description
GNU enscript is a free replacement for Adobe's Enscript
program. Enscript converts ASCII files to PostScript(TM) and spools
generated PostScript output to the specified printer or saves it to a
file. Enscript can be extended to handle different output media and
includes many options for customizing printouts

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P 3 -p1 -b .locale
%patch -P 8 -p1 -b .wrap_header
%patch -P 10 -p1 -b .rh457720
%patch -P 12 -p1 -b .rh477382
%patch -P 13 -p1 -b .build
%patch -P 14 -p1 -b .manfixes
%patch -P 15 -p1 -b .bufpos-crash
%patch -P 16 -p1 -b .newencodings
%patch -P 17 -p1 -b .vasnprintf
%patch -P 18 -p1 -b .c23

install -pm 644 %{SOURCE1} states/hl/ruby.st
install -pm 644 %{SOURCE2} states/hl/php.st

%build
autoreconf -fiv
export CPPFLAGS='-DPROTOTYPES'
%configure --with-media=Letter
%make_build


%install
mkdir -p %{buildroot}%{_datadir}/locale/{de,es,fi,fr,nl,sl}/LC_MESSAGES
%make_install
rm -f %{buildroot}%{_datadir}/info/dir

%find_lang %name

(cd %{buildroot};find .%{_datadir}/enscript/* \! -type d) | \
	sed -e 's,^\.,,' | sed -e 's,*font.map,%%config &,' > share.list
(cd %{buildroot};find .%{_datadir}/enscript/* -type d) | \
	sed -e 's,^\.,,' | sed -e 's,^,%dir ,' >> share.list

( cd %{buildroot}
  ln .%{_prefix}/bin/enscript .%{_prefix}/bin/nenscript
)

%find_lang %{name} %{name}.lang

for all in README THANKS; do
	iconv -f ISO88591 -t UTF8 < $all > $all.new
	touch -r $all $all.new
	mv $all.new $all
done

%files -f %{name}.lang -f share.list
%doc AUTHORS ChangeLog COPYING docs/FAQ.html NEWS README README.ESCAPES THANKS TODO
%{_bindir}/*
%{_mandir}/man1/*
%dir %{_datadir}/enscript
%{_infodir}/%{name}*
%config(noreplace) %{_sysconfdir}/enscript.cfg

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.6-38
- Import
