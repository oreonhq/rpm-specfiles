%global source0_hash 111ca813c25375c25984c9d396e48e78d4093e61fffbb1f76ac4de680ef1efbb

Name:           perl-Getopt-Usaginator
Version:        0.0012
Release:        42%{?dist}
Summary:        Conjure up a usage function for your applications
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Getopt-Usaginator
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROKR/Getopt-Usaginator-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Package::Pkg) >= 0.0014
# Tests only
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Most)

%description
Getopt::Usaginator is a tool for creating a handy usage subroutine for
commandline applications. It does not do any option parsing, but is best paired
with Getopt::Long or any of the other myriad of option parsers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Getopt-Usaginator-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
