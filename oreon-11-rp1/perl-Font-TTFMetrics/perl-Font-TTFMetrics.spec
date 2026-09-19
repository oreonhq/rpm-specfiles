%global source0_hash 2cd27f322f5a9e7ca79325eb196b032c985a85807143df7eb02367f0c6672ec8

Name:           perl-Font-TTFMetrics
Version:        0.1
Release:        44%{?dist}
Summary:        Parser for the TTF file
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Font-TTFMetrics
Source0:        https://cpan.metacpan.org/modules/by-module/Font/Font-TTFMetrics-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
Font::TTFMetrics encapsulates the font metrics of a true type font file. A
true type font file contains several tables which need to be parsed before
any useful information could be gathered about the font. There is the
excellent module for parsing TTF font in CPAN by Martin Hosken, Font::TTF.
But in my opinion the use of Font::TTF requires intimate knowledge of TTF
font format. This module was written to support the use of TTF in Pastel 2D
graphics library in Perl. Three factors prompted me to write this module:
first, I required a fast module to access TTF file. Second, all the access
required was read-only. Last, I wanted a user friendly, higher level API to
access TTF file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Font-TTFMetrics-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*
chmod a-x $RPM_BUILD_ROOT/%{perl_vendorlib}/Font/TTFMetrics.pm

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
