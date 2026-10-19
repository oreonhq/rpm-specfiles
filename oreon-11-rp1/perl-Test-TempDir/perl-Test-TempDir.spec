%global source0_hash e2722b6534af0819f0f96a68436054ef0cbbc93e5f0b8f25e0e5497a9e478362
Name:           perl-Test-TempDir
Version:        0.11
Release:        1%{?dist}
Summary:        Temporary files support for testing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-TempDir
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-TempDir-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::NFSLock)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Directory::Scratch)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::NFSLock)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::CheckDeps)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::use::ok)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl-generators
# /oreon:deps
%description
Test::TempDir provides temporary directory creation with testing in mind.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-TempDir-%{version}

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
