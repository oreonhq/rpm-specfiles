%global source0_hash 2d6bde2d2d03523f164f930e4fdec6025f3a94abe48a43706f543880a1a21ebe

Name: abook
Version: 0.6.2
Release: 1%{?dist}
# GPL-2.0-or-later, except:
# getopt.[ch]: LGPL-2.0-or-later
# getopt1.c: LGPL-2.0-or-later
License: GPL-2.0-or-later AND LGPL-2.0-or-later
URL: https://abook.sourceforge.io/
Summary: Text-based addressbook program for mutt
Source0: https://abook.sourceforge.net/devel/abook-%{version}.tar.gz
# preserve all fields by default
Patch0: %{name}-preserve.patch
# Fix detection of wcwidth()
Patch4: abook-wcwidth.patch
# backport upstream patches
Patch10: 0001-follow-symlinks-fix-bug-4.patch
Patch11: 0002-Remove-inline-keyword-from-header.patch
Patch12: 0003-optional-datafile-rewrite-omitted-if-no-change-happe.patch
Patch13: 0004-Search-nickname-alias-as-well.patch
Patch14: 0005-silenced-a-couple-of-GCC-stringop-overflow-warnings.patch
Patch15: 0006-allcsv-Remove-header-line-s-leading-which-confuse-re.patch
Patch16: 0007-fix-an-autoconf-problem-from-d89aeb1-lvformat-wasn-t.patch
Patch17: 0008-fix-built-in-vcard-parsing.-Use-item_fput-to-set-fie.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: readline-devel
Requires: webclient

%description
Abook is a small and powerful text-based addressbook program
designed for use with the mutt mail client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1
autoreconf -vif

%build
%configure
%make_build

%install
%make_install
# generate localized files list
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS BUGS ChangeLog FAQ README RELEASE_NOTES THANKS TODO sample.abookrc
%{_bindir}/abook
%{_mandir}/man1/abook.*
%{_mandir}/man5/abookrc.*

%changelog
%autochangelog
