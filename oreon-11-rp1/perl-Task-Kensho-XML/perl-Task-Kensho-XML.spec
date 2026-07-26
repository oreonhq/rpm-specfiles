%global source0_hash 078330a7173060536d065c0feb99d64f5f2b94a95f3d87d08cdbb7d003d83e89

Name:           perl-Task-Kensho-XML
Version:        0.41
Release:        13%{?dist}
Summary:        Glimpse at an Enlightened Perl (XML Development)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Task-Kensho-XML
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Task-Kensho-XML-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-Time
# perl(XML::Generator::PerlData) - not used by tests
# perl(XML::LibXML) - not used by tests
# perl(XML::LibXSLT) - not used by tests
# perl(XML::SAX) - not used by tests
# perl(XML::SAX::Writer) - not used by tests
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
Requires:       perl(XML::Generator::PerlData)
Requires:       perl(XML::LibXML)
Requires:       perl(XML::LibXSLT)
Requires:       perl(XML::SAX)
Requires:       perl(XML::SAX::Writer)

%description
Task::Kensho is a list of recommended modules for Enlightened Perl
development. CPAN is wonderful, but there are too many wheels and you have
to pick and choose amongst the various competing technologies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Task-Kensho-XML-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENCE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
