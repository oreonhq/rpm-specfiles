%global source0_hash f8d41145e8f865c85b4b0823f194cdf3ae228bbec7dcf828432dcd2f6d1c03ac

Name:           perl-MooX-File-ConfigDir
Version:        0.008
Release:        16%{?dist}
Summary:        Moo eXtension for File::ConfigDir
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-File-ConfigDir
Source0:        https://cpan.metacpan.org/modules/by-module/MooX/MooX-File-ConfigDir-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ConfigDir) >= 0.018
BuildRequires:  perl(FindBin)
BuildRequires:  perl(local::lib)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role) >= 1.003000
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.9
BuildRequires:  perl(warnings)
Requires:       perl(File::ConfigDir) >= 0.018
Requires:       perl(Moo::Role) >= 1.003000

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(File::ConfigDir\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Moo::Role\\)$

%description
This module is a helper for easily find configuration file locations.
Whether to use this information for find a suitable place for installing
them or looking around for finding any piece of settings, heavily depends
on the requirements.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooX-File-ConfigDir-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%license ARTISTIC-1.0 GPL-1 LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
