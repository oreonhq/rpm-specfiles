%global source0_hash e4998c177cd6fe97e0ed4340b7b3f832c67e2ecf1ff72f699920f2542da628e0
Name:           perl-UDDI-Lite
Version:        0.718
Release:        1%{?dist}
Summary:        Library for UDDI clients in Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/UDDI-Lite
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/UDDI-Lite-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(SOAP::Lite) >= 0.716
%global __requires_exclude %{?__requires_exclude?__requires_exclude|}^perl\\(SOAP::Lite\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(SOAP::Test)
BuildRequires:  perl(Test)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
