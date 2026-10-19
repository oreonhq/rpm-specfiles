%global source0_hash 7c8dd9e797bd0ec2600d300ecd49ee978119831c656b2d0bdeaecea04348a112
Name:           perl-Applify
Version:        0.23
Release:        12%{?dist}
Summary:        Write object oriented perl scripts with ease
License:        Artistic-2.0
URL:            https://metacpan.org/release/Applify/
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/Applify-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Getopt::Long)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
