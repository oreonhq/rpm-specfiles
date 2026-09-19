%global source0_hash 7c8dd9e797bd0ec2600d300ecd49ee978119831c656b2d0bdeaecea04348a112

Name:           perl-Applify
Version:        0.23
Release:        12%{?dist}
Summary:        Write object oriented perl scripts with ease
License:        Artistic-2.0

URL:            https://metacpan.org/release/Applify/
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/Applify-%{version}.tar.gz

BuildArch:      noarch
# build dependencies
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime dependencies
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test dependencies
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
Requires:       perl(Getopt::Long)

%description
This module should keep all the noise away and let you write scripts very
easily. These scripts can even be unit tested even though they are defined
directly in the script file and not in a module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Applify-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes example
%{perl_vendorlib}/Applify*
%{_mandir}/man3/Applify*

%changelog
%autochangelog
