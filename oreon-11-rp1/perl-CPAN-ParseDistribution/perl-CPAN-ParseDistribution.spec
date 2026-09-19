%global source0_hash 6c0178e613865ca7d48e868f4459bfb9e5e6f5c10f3a475b0df78aa1dead6a7f

Name:           perl-CPAN-ParseDistribution
Version:        1.54
Release:        27%{?dist}
Summary:        Index a file from the BackPAN
License:        GPL-2.0-only OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-ParseDistribution
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/CPAN-ParseDistribution-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::CheckOS)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Parallel::ForkManager) >= 1.03
BuildRequires:  perl(Safe)
BuildRequires:  perl(vars)
BuildRequires:  perl(YAML) >= 0.6
# Tests only
BuildRequires:  perl(Config)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
Requires:       perl(Parallel::ForkManager) >= 1.03
Requires:       perl(YAML) >= 0.6

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Parallel::ForkManager\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(YAML\\)$

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

%check
make test

%files
%license ARTISTIC.txt GPL2.txt
%doc CHANGELOG README TODO
%{perl_vendorlib}/CPAN*
%{_bindir}/dumpcpandist
%{_mandir}/man1/dumpcpandist*
%{_mandir}/man3/CPAN::ParseDistribution*

%changelog
%autochangelog
