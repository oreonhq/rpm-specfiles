%global source0_hash 8e2c000fcbc6d641b0e6ff95e13c846da3ff31097801e86702124a206888f5ac

Summary:    MS Word to ASCII/Postscript converter
Name:       antiword
Version:    0.37
Release:    44%{?dist}
Source0:    http://www.winfield.demon.nl/linux/%{name}-%{version}.tar.gz
Source1:    antiword.sh
URL:        http://www.winfield.demon.nl/
Patch0:     antiword-0.32-fix-flags.patch
Patch1:     http://seclists.org/oss-sec/2014/q4/att-870/antiword-bGetPPS-Prevent-buffer-overflow-of-atPPSlist-_szName.diff
Patch2:     50_antiword-manpage-hyphen-to-minus.patch
Patch3:     docx.patch
Patch4:     remove-cjb.net-references.patch
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
BuildRequires: gcc
BuildRequires: make

%description
Antiword is a free MS-Word reader for Linux, BeOS and RISC OS. It converts
the documents from Word 6, 7, 97 and 2000 to ASCII and Postscript. Antiword
tries to keep the layout of the document intact.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%{__chmod} a+r * Resources/* Docs/*

%build
OPT="$RPM_OPT_FLAGS" make all %{?_smp_mflags}

%install
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 755 antiword $RPM_BUILD_ROOT%{_bindir}/antiword.bin
%{__install} -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/antiword
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__cp} -a Resources/* $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__mkdir_p} $RPM_BUILD_ROOT%{_mandir}/man1
%{__cp} Docs/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
%{__chmod} 644 kantiword
iconv -f iso-8859-1 -t utf-8 Docs/antiword.php > Docs/antiword.php.utf8
iconv -f iso-8859-1 -t utf-8 Docs/Netscape > Docs/Netscape.utf8
%{__mv} Docs/antiword.php.utf8 Docs/antiword.php
%{__mv} Docs/Netscape.utf8 Docs/Netscape

%files
%license Docs/COPYING
%doc Docs/FAQ Docs/ReadMe Docs/Netscape Docs/ChangeLog
%doc Docs/Exmh Docs/Mozilla Docs/QandA Docs/Mutt Docs/antiword.php
%doc Docs/Emacs Docs/History kantiword
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/%{name}

%changelog
%autochangelog
