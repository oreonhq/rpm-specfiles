# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f06895c0206dada9f9e7f07ecaeb6a3651fd648f4820f49c1f76bfeaec2f2913

Name: perl-SGMLSpm
Version: 1.03ii
Release: 1%{?dist}
Summary: Perl library for processing SGML parser output
License: GPL-2.0-or-later
URL: https://sourceware.org/docbook-tools/
Source0: https://mirrors.kernel.org/sourceware/docbook-tools/new-trials/SOURCES/SGMLSpm-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
SGMLSpm is a Perl library and the sgmlspl program for processing the event
stream produced by an SGML parser.

%prep
%oreon_sha256
%autosetup -n SGMLSpm

%build

%install
make install_system \
    BINDIR=%{buildroot}%{_bindir} \
    PERL=%{__perl} \
    PERL5DIR=%{buildroot}%{perl_vendorlib} \
    MODULEDIR=%{buildroot}%{perl_vendorlib}/SGMLS \
    SPECDIR=%{buildroot}%{perl_vendorlib}

%check
perl -I. test-SGMLS.pl

%files
%license COPYING
%doc BUGS ChangeLog README TODO DOC/HTML
%{_bindir}/sgmlspl
%{perl_vendorlib}/SGMLS.pm
%{perl_vendorlib}/SGMLS/
%{perl_vendorlib}/skel.pl

%changelog
%autochangelog
