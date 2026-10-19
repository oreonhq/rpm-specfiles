%global source1_hash afff1a4ca66018fc88e0d03d9a218ce7c77451d2ac66f54fc3268a3a33d84905
%global source0_hash e1964d199b0726f431f9a1dc4ff7257bb3dba879b9fa221803e0aa7840dee0e0
Summary:        A Tool for manipulating BibTeX data bases
Name:		BibTool
Version:	2.68
Release:        1%{?dist}
Source0:        https://github.com/ge-ne/bibtool/releases/download/BibTool_2_68/BibTool-%{version}.tar.gz
Source1:	https://github.com/ge-ne/bibtool/releases/download/BibTool_2_68/BibTool-%{version}.tar.gz.asc
Source2:	gpgkey-E2A609830CE1675666671B86EA2168BE699213A2.gpg
URL:		http://www.gerd-neugebauer.de/software/TeX/BibTool/
Patch:		0001-old-font-commands-added.patch
Patch:		0001-support-for-make-check-fixed.patch
Patch:		0001-fix-incompatible-pointer-types.patch
Patch:		0001-build-BibTool-against-system-regex.patch
Patch:		0001-fix-duplicate-case-fix.patch
License:	GPL-2.0-or-later AND CC-BY-SA-3.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-interpreter
BuildRequires:  tex(latex)
BuildRequires:  tex(luatex85.sty)
BuildRequires:  tex-bibtex
BuildRequires:  tex-makeindex
# /oreon:deps
%description
BibTeX provides an easy to use means to integrate citations and
bibliographies into LaTeX documents. But the user is left alone with
the management of the BibTeX files. The program BibTool is intended to
fill this gap. BibTool allows the manipulation of BibTeX files which
goes beyond the possibilities --- and intentions --- of BibTeX.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name} -p 1
sed -i -e 's%^#!/usr/local/bin/tclsh%#! %{_bindir}/tclsh%' Tcl/bibtool.tcl
sed -i -e 's%^#!/usr/local/bin/perl%#! %{_bindir}/perl%' Perl/bibtool.pl
# configure will recreate the directory, but only with config.h within
rm -rf regex-0.12

%build

%configure --libdir=%{_datadir}
sed -i -e 's#@kpathsea_lib_static@##' makefile
%make_build CFLAGS="$RPM_OPT_FLAGS"
make doc
%check

make check
%install
make install INSTALLPREFIX=$RPM_BUILD_ROOT INSTALL='install -p -m 755'
make install-man INSTALLPREFIX=$RPM_BUILD_ROOT INSTALL='install -p -m 644'
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
