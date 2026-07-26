%global source0_hash e4998c177cd6fe97e0ed4340b7b3f832c67e2ecf1ff72f699920f2542da628e0

Name:           perl-UDDI-Lite
Version:        0.718
Release:        34%{?dist}
Summary:        Library for UDDI clients in Perl
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/UDDI-Lite
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/UDDI-Lite-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(overload)
BuildRequires:  perl(SOAP::Lite) >= 0.716
BuildRequires:  perl(SOAP::Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(SOAP::Lite) >= 0.716

%global __requires_exclude %{?__requires_exclude?__requires_exclude|}^perl\\(SOAP::Lite\\)$

%description
UDDI::Lite for Perl is a collection of Perl modules which provides a simple
and lightweight interface to the Universal Description, Discovery and
Integration (UDDI) server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n UDDI-Lite-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
