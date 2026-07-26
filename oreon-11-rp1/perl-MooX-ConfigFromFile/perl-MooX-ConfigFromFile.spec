%global source0_hash 12fbfd7659d15992c5994d88e66622c1dc0abce903fc9531f9db59449f4d393d

Name:           perl-MooX-ConfigFromFile
Version:        0.009
Release:        29%{?dist}
Summary:        Moo eXtension for initializing objects from configuration file
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-ConfigFromFile
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/MooX-ConfigFromFile-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find::Rule) >= 0.30
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Hash::Merge)
# 1.003 from Moo in META.json which not used
BuildRequires:  perl(Moo::Role) >= 1.003
BuildRequires:  perl(MooX::File::ConfigDir) >= 0.002
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moo) >= 1.003
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Moose)
%if !%{defined perl_bootstrap}
# Break build-cycle: perl-MooX-Cmd → perl-MooX-Options
# → perl-MooX-ConfigFromFile → perl-MooX-Cmd
BuildRequires:  perl(MooX::Cmd) >= 0.012
BuildRequires:  perl(MooX::Cmd::Tester)
BuildRequires:  perl(MooX::Options) >= 4.001
%endif
Requires:       perl(File::Find::Rule) >= 0.30
Requires:       perl(Moo::Role) >= 1.003
Requires:       perl(MooX::File::ConfigDir) >= 0.002

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Find::Rule\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo::Role\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MooX::File::ConfigDir\\)$

%description
This module is intended to easy load initialization values for attributes
on object construction from an appropriate configuration file. The building is
done in MooX::ConfigFromFile::Rule - using MooX::ConfigFromFile ensures the
role is applied.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooX-ConfigFromFile-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license ARTISTIC-1.0 GPL-1 LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
