%global source0_hash 7899b42253e6be0ec70a633af05d5b1e387d30979cf1358bb405fe665f02cf89

Name:           perl-TAP-SimpleOutput
Version:        0.009
Release:        27%{?dist}
Summary:        Simple closure-driven TAP generator
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://metacpan.org/release/TAP-SimpleOutput
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/TAP-SimpleOutput-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
# Perl::Version checked by t/00-check-deps.t
BuildRequires:  perl(Perl::Version)
BuildRequires:  perl(Sub::Exporter::Progressive)
# Test::More 0.98 not used at tests
# Tests:
BuildRequires:  perl(blib) >= 1.01
# CPAN::Meta not useful
# CPAN::Meta::Prereq not useful
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::CheckDeps) >= 0.010
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(utf8)
Requires:       perl(Perl::Version)
Requires:       perl(Test::More) >= 0.98

%description
We provide one function, counters(), that returns a number of simple closures
designed to help output TAP easily and correctly, with a minimum of fuss.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n TAP-SimpleOutput-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
