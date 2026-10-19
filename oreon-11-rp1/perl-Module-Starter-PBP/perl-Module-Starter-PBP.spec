%global source0_hash 6a7feb9b6df05462aea385395663c6602812d50b26e98734c5644ce78a8724ce
%global tarver v0.0.3
Name:           perl-Module-Starter-PBP
Version:        0.000003        
Release:        1%{?dist}
Summary:        Create a module as recommended in "Perl Best Practices"
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Starter-PBP
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Module-Starter-PBP-%{tarver}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::Command)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Starter::Simple)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements a simple approach to creating modules and their support
files, based on the Module::Starter approach. 

When used as a Module::Starter plugin, this module allows you to specify a
simple directory of templates which are filled in with module-specific
information, and thereafter form the basis of your new module.

The default templates that this module initially provides are based on the
recommendations in the book "Perl Best Practices".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Starter-PBP-%{tarver}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
chmod -R u+w %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
