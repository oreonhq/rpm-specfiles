%global source0_hash 514a84180352b6bf367c1d2499819dfa82b60d8c45777432fa643a5ed7d80796
Name: catdoc
Version: 0.95
Release:        1%{?dist}
Summary:        A program which converts Microsoft office files to plain text
License: GPL-2.0-or-later
URL: https://www.wagner.pp.ru/~vitus/software/catdoc/
Source0:        http://ftp.wagner.pp.ru/pub/catdoc/%{name}-%{version}.tar.gz
Patch0: makefilefix.patch
Recommends: %{name}-wordview
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tk
# /oreon:deps
%description
catdoc is program which reads one or more Microsoft word files
and outputs text, contained insinde them to standard output.
Therefore it does same work for.doc files, as unix cat
command for plain ASCII files.
It is now accompanied by xls2csv - program which converts
Excel spreadsheet into comma-separated value file,
and catppt - utility to extract textual information
from Powerpoint files

%package wordview
Summary: Display Microsoft Word files in a graphical window
Requires: tk
%description wordview
wordview is a program that displays Microsoft Word files in a graphical window
via Tk.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles catdoc-wordview usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n catdoc-wordview -f %{oreon_filedir}/catdoc-wordview.list

%changelog

%autochangelog
