%global source0_hash 3f13631b13b9604fb489e2989490c99f103743a837239bdafae9d6baf55f8f46

Name:           perl-UUID-URandom
Version:        0.001
Release:        23%{?dist}
Summary:        UUIDs based on /dev/urandom
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/UUID-URandom
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/UUID-URandom-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Crypt::URandom) >= 0.36
BuildRequires:  perl(Exporter) >= 5.57
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful

%description
This Perl module provides a portable, secure generator of RFC-4122 version 4
random UUIDs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n UUID-URandom-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
