%global source0_hash bec0e1d5301a57727e4e3a9f56590d5daa65e81be3027ecbc4141c04fa871818

Name:           perl-Data-Random
Version:        0.14
Release:        2%{?dist}
Summary:        Perl module to generate random data
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Data-Random
Source0:        https://cpan.metacpan.org/authors/id/B/BA/BAREFOOT/Data-Random-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML::Tiny)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(GD)
BuildRequires:  perl(Time::Piece)
# Tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

%{?perl_default_filter}

%description
A module used to generate random data. Useful mostly for test programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Random-%{version}

chmod 644 lib/Data/Random.pm lib/Data/Random/WordList.pm

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
AUTHOR_TESTING=1 %{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
