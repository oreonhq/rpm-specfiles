%global source0_hash 6c0178e613865ca7d48e868f4459bfb9e5e6f5c10f3a475b0df78aa1dead6a7f
Name:           perl-CPAN-ParseDistribution
Version:        1.54
Release:        27%{?dist}
Summary:        Index a file from the BackPAN
License:        GPL-2.0-only OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-ParseDistribution
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/CPAN-ParseDistribution-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Parallel::ForkManager) >= 1.03
Requires:       perl(YAML) >= 0.6
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Parallel::ForkManager\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(YAML\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::CheckOS)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Parallel::ForkManager)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(YAML)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Given a file from the BackPAN, this will let you find out what versions of
what modules it contains, the distribution name and version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPAN-ParseDistribution-%{version}

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
