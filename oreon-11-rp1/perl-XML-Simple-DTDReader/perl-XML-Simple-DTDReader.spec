%global source0_hash 00335c6817f7a76c034183b4fc25effae7f00ba0d8ac86ab418f60d2cce4d224

Name:           perl-XML-Simple-DTDReader
Version:        0.04
Release:        49%{?dist}
Summary:        Simple XML file reading based on their DTDs
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Simple-DTDReader
Source0:        https://cpan.metacpan.org/modules/by-module/XML/XML-Simple-DTDReader-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XML::Parser) >= 2.28
# Tests
BuildRequires:  perl(Test::More)
Requires:       perl(XML::Parser) >= 2.28

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(XML::Parser\\)$

%description
XML::Simple::DTDReader aims to be a XML::Simple drop-in replacement, but
with several aspects of the module controlled by the XML's DTD.
Specifically, array folding and array forcing are inferred from the DTD.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Simple-DTDReader-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
