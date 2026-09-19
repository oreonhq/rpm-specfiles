%global source0_hash b376b90b270d0aa7819f83c0ca8419616a9deae4441fdee81e4527603a13608c

Name:           tangerine
Version:        0.22
Release:        28%{?dist}
Summary:        Perl dependency metadata tool
License:        MIT
URL:            https://metacpan.org/release/App-Tangerine
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CONTYK/App-Tangerine-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Find::Rule::Perl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Compare)
BuildRequires:  perl(MCE::Map)
BuildRequires:  perl(overload)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Tangerine) >= 0.15
# Tests only
BuildRequires:  perl(Test::More)
Requires:       perl(Tangerine) >= 0.15

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Tangerine\\)$

%description
A perl dependency metadata reporting tool built on top of Tangerine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-Tangerine-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc Changes CONTRIBUTING README.md
%{_bindir}/%{name}
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
