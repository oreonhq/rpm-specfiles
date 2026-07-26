%global source0_hash 514a84180352b6bf367c1d2499819dfa82b60d8c45777432fa643a5ed7d80796

Name: catdoc
Version: 0.95
Release: %autorelease
Summary: A program which converts Microsoft office files to plain text
License: GPL-2.0-or-later
URL: https://www.wagner.pp.ru/~vitus/software/catdoc/
Source0: http://ftp.wagner.pp.ru/pub/catdoc/%{name}-%{version}.tar.gz
Patch0: makefilefix.patch
BuildRequires: gcc
BuildRequires: make
BuildRequires: tk
Recommends: %{name}-wordview

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
%if 0%{?fedora} > 41
Conflicts: %{name} <= 0.95-25
%endif
%if 0%{?fedora} == 41
Conflicts: %{name} <= 0.95-19
%endif

%description wordview
wordview is a program that displays Microsoft Word files in a graphical window
via Tk.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/catdoc
%{_bindir}/catppt
%{_bindir}/xls2csv
%{_mandir}/man1/catdoc.1.*
%{_mandir}/man1/catppt.1.*
%{_mandir}/man1/xls2csv.1.*
%{_datadir}/catdoc
%doc README NEWS

%files wordview
%{_bindir}/wordview
%{_mandir}/man1/wordview.1.*

%changelog
%autochangelog
