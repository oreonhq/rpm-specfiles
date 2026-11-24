# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4b697d444259759ea02d2c442c9bffe5ffe14c9214084a01f743693a944cc293
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:          perl-Font-TTF
Version:       1.06
Release:       1%{?dist}
Summary:       Perl library for modifying TTF font files
License:       Artistic-2.0
URL:           https://metacpan.org/release/Font-TTF
Source0:       http://cpan.org/authors/id/B/BH/BHALLISSY/Font-TTF-%{version}.tar.gz
BuildArch:     noarch
BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Getopt::Std)
BuildRequires: perl(strict)
BuildRequires: perl(bytes)
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::File)
BuildRequires: perl(IO::String)
BuildRequires: perl(Symbol)
BuildRequires: perl(utf8)
BuildRequires: perl(vars)
BuildRequires: perl(File::Compare)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Simple)

%description
Perl module for TrueType font hacking. Supports reading, processing and writing
of the following tables: GDEF, GPOS, GSUB, LTSH, OS/2, PCLT, bsln, cmap, cvt,
fdsc, feat, fpgm, glyf, hdmx, head, hhea, hmtx, kern, loca, maxp, mort, name,
post, prep, prop, vhea, vmtx and the reading and writing of all other table
types.

In short, you can do almost anything with a standard TrueType font with this
module.

%package XMLparse
Summary:       XML Font parser
Conflicts:     perl-Font-TTF < 1.06-6

%description XMLparse
This Perl module contains the support routines for parsing XML and generating
the TrueType font structures as a result.

The module has been separated from the rest of the perl-Font-TTF package in
order to reduce the dependency that this would bring, of the whole package on
XML::Parser. This way, people without the XML::Parser can still use the rest
of the package.

%prep
%oreon_sha256
%setup -q -n Font-TTF-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc README.TXT CONTRIBUTORS Changes TODO
%dir %{perl_vendorlib}/Font
%dir %{perl_vendorlib}/Font/TTF
%{perl_vendorlib}/ttfmod.pl
%{perl_vendorlib}/Font/TTF.pm
%{perl_vendorlib}/Font/TTF/*
%exclude %{perl_vendorlib}/Font/TTF/XMLparse.pm
%{_mandir}/man3/*.3*
%exclude %{_mandir}/man3/Font::TTF::XMLparse.3pm.*
%exclude %{perl_vendorlib}/Font/TTF/Win32.pm
%exclude %{_mandir}/man3/Font::TTF::Win32.3pm.*

%files XMLparse
%license LICENSE
%doc CONTRIBUTORS Changes
%dir %{perl_vendorlib}/Font
%dir %{perl_vendorlib}/Font/TTF
%{perl_vendorlib}/Font/TTF/XMLparse.pm
%{_mandir}/man3/Font::TTF::XMLparse.3pm.*

%changelog
%autochangelog
