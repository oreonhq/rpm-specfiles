%global source0_hash 078330a7173060536d065c0feb99d64f5f2b94a95f3d87d08cdbb7d003d83e89
Name:           perl-Task-Kensho-XML
Version:        0.41
Release:        1%{?dist}
Summary:        Glimpse at an Enlightened Perl (XML Development)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Task-Kensho-XML
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Task-Kensho-XML-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(XML::Generator::PerlData)
Requires:       perl(XML::LibXML)
Requires:       perl(XML::LibXSLT)
Requires:       perl(XML::SAX)
Requires:       perl(XML::SAX::Writer)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
