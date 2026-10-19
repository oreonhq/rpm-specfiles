%global source0_hash c729969d628f2914d8ae189b38653ee3831a8eed444987d5eaccb621b6fc2449
Name:           perl-Version-Requirements
Version:        0.101023
Release:        1%{?dist}
Summary:        Set of version requirements for a CPAN dist (DEPRECATED)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Version-Requirements
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Version-Requirements-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Version::Requirements is now DEPRECATED.

Use CPAN::Meta::Requirements, which is a drop-in replacement.

A Version::Requirements object models a set of version constraints like
those specified in the META.yml or META.json files in CPAN distributions.
It can be built up by adding more and more constraints, and it will reduce
them to the simplest representation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Version-Requirements-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
make test PERL_CORE=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
