%global source0_hash 2d6bde2d2d03523f164f930e4fdec6025f3a94abe48a43706f543880a1a21ebe
Name: abook
Version: 0.6.2
Release:        1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.0-or-later
URL: https://abook.sourceforge.io/
Summary:        Text-based addressbook program for mutt
Source0:        https://abook.sourceforge.net/devel/abook-%{version}.tar.gz
Patch0: %{name}-preserve.patch
Patch4: abook-wcwidth.patch
Patch10: 0001-follow-symlinks-fix-bug-4.patch
Patch11: 0002-Remove-inline-keyword-from-header.patch
Patch12: 0003-optional-datafile-rewrite-omitted-if-no-change-happe.patch
Patch13: 0004-Search-nickname-alias-as-well.patch
Patch14: 0005-silenced-a-couple-of-GCC-stringop-overflow-warnings.patch
Patch15: 0006-allcsv-Remove-header-line-s-leading-which-confuse-re.patch
Patch16: 0007-fix-an-autoconf-problem-from-d89aeb1-lvformat-wasn-t.patch
Patch17: 0008-fix-built-in-vcard-parsing.-Use-item_fput-to-set-fie.patch
Requires: webclient
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
# /oreon:deps
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
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
