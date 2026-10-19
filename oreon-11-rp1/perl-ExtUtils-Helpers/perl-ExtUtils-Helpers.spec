%global source0_hash c8574875cce073e7dc5345a7b06d502e52044d68894f9160203fcaab379514fe
Name:		perl-ExtUtils-Helpers
Version:	0.028
Release:        1%{?dist}
Summary:        Various portability utilities for module builders
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/ExtUtils-Helpers
Source0:        https://cpan.metacpan.org/modules/by-module/ExtUtils/ExtUtils-Helpers-%{version}.tar.gz
BuildArch:	noarch
Provides:       perl(ExtUtils::Helpers)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides various portable helper functions for module building
modules.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n ExtUtils-Helpers-%{version}

# Don't include VMS and Windows helpers, which may pull in unwelcome dependencies
rm -f lib/ExtUtils/Helpers/{VMS,Windows}.pm
perl -ni -e 'print unless /^lib\/ExtUtils\/Helpers\/(VMS|Windows)\.pm$/;' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.028-4
- Prepare for Oreon 11 (RP1)
