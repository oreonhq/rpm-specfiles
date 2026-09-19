%global source0_hash 29e9e2133951046c78f205f1b3e8df62c90e114f0e08fa06b817766a0f808b12

Name:           perl-Tie-Simple
Version:        1.04
Release:        29%{?dist}
Summary:        Variable ties made easier: much, much, much easier
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tie-Simple
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HANENKAMP/Tie-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
# Tests
BuildRequires:  perl(Test::More)

%description
This module adds the ability to quickly create new types of tie objects
without creating a complete class. It does so in such a way as to try and
make the programmers life easier when it comes to single-use ties that I
find myself wanting to use from time-to-time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tie-Simple-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
