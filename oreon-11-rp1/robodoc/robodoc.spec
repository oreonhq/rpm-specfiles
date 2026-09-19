%global source0_hash a1061f306ed9600a7551dbc72fcac1c7ae16f3f73d63554f2e854f5c5d3ff267

#	Perl files are only documentation examples.

%global __perl_provides		%{nil}
%global __perl_requires		%{nil}

Name:		robodoc
Version:	4.99.44
Release:	13%{?dist}
Summary:	Extract documentation from source code
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
Source0:	http://rfsber.home.xs4all.nl/Robo/archives/%{name}-%{version}.tar.gz
Patch1:		robodoc-4.99.43-silentwarnings.patch
URL:		http://rfsber.home.xs4all.nl/Robo/
BuildRequires: make
BuildRequires:	gcc
BuildRequires:	perl-generators

%description
  ROBODoc is a documentation tool (based on the AutoDocs program written
a long time ago by Commodore). It extracts specially formatted comment
headers from the source file and puts them in a separate file. ROBODoc
thus allows you to include the program documentation in the source
code and avoid having to maintain two separate documents.

  ROBODoc can format the documentation in HTML, ASCII, AmigaGuide,
LaTeX, or RTF format. It is even possible to include parts of the
source code with function names that point their the documentation. It
also can create index tables for all your variables, classes,
functions, etc.

  The best feature of ROBODoc is that it works with many languages:
Assembler, C, Perl, LISP, Occam, Tcl/Tk, Pascal, Fortran, shell
scripts, and COBOL, basically any language that supports
comments/remarks.

#-------------------------------------------------------------------------------
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#-------------------------------------------------------------------------------

%setup -q

%patch -P1 -p 1 -b .silentwarnings

#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

%configure docdir="%{_docdir}/robodoc"
make CFLAGS="${RPM_OPT_FLAGS}" %{?_smp_mflags}

#	Changelog is ISO8859. Convert it to UTF-8.

iconv -f ISO8859-1 -t UTF-8 -o ChangeLog.utf8 ChangeLog
touch -r ChangeLog ChangeLog.utf8
mv ChangeLog.utf8 ChangeLog

#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------

make DESTDIR="${RPM_BUILD_ROOT}" INSTALL="install -p" install

#	Get rid of the installed documentation

rm -rf "${RPM_BUILD_ROOT}%{_docdir}/robodoc"

#-------------------------------------------------------------------------------
%files
#-------------------------------------------------------------------------------

%doc AUTHORS Change* COPYING README Docs/manual.css Docs/manual.html
%doc Examples
%{_bindir}/*
%{_mandir}/man1/*

#-------------------------------------------------------------------------------
%changelog
%autochangelog
