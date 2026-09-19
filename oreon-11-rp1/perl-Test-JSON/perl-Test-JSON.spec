%global source0_hash 07c08ab2fcc12850d1ad54fcf6afe9ad1a25a098310c3e7142af1d3cb821d7b3

Name:           perl-Test-JSON
Summary:        Test JSON data
Version:        0.11
Release:        44%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/O/OV/OVID/Test-JSON-%{version}.tar.gz 
URL:            https://metacpan.org/release/Test-JSON

BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(JSON::Any) >= 1.2
BuildRequires:  perl(Test::Differences) >= 0.47
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Simple) >= 0.62
BuildRequires:  perl(Test::Tester) >= 0.107

Requires:       perl(JSON::Any) >= 1.2
Requires:       perl(Test::Differences) >= 0.47
Requires:       perl(Test::Tester) >= 0.107

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
JavaScript Object Notation (JSON) is a lightweight data interchange format.
Test::JSON makes it easy to verify that you have built valid JSON and that
it matches your expected output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-JSON-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Test*
%{_mandir}/man3/Test*.3*

%changelog
%autochangelog
