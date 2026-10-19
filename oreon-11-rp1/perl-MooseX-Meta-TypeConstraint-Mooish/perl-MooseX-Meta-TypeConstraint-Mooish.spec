%global source0_hash 48ce292333c4f151aead6b087cc0f82139fb003d7785dc4ad8b1181c692067ca
Name:           perl-MooseX-Meta-TypeConstraint-Mooish
Version:        0.001
Release:        1%{?dist}
Summary:        Translate Moo-style constraints to Moose-style
License:        LicenseRef-Callaway-LGPLv2
URL:            https://metacpan.org/release/MooseX-Meta-TypeConstraint-Mooish
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/MooseX-Meta-TypeConstraint-Mooish-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Moose::Meta::TypeConstraint)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::TypeConstraint)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Test::CheckDeps)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose::More)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(aliased)
BuildRequires:  perl(blib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Moose type constraints are expected to return true if the value passes the
constraint, and false otherwise; Moo constraints, on the other hand, die
if validation fails. This meta-class allows for Moo-style constraints. It will
wrap them and translate their Moo into a dialect Moose understands.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Meta-TypeConstraint-Mooish-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
