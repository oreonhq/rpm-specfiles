%global source0_hash 48ce292333c4f151aead6b087cc0f82139fb003d7785dc4ad8b1181c692067ca

Name:           perl-MooseX-Meta-TypeConstraint-Mooish
Version:        0.001
Release:        33%{?dist}
Summary:        Translate Moo-style constraints to Moose-style
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://metacpan.org/release/MooseX-Meta-TypeConstraint-Mooish
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/MooseX-Meta-TypeConstraint-Mooish-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::TypeConstraint)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(namespace::autoclean) >= 0.24
BuildRequires:  perl(Try::Tiny)
# Tests:
BuildRequires:  perl(aliased)
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::CheckDeps) >= 0.010
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose::More) >= 0.028
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Moose::Meta::TypeConstraint)

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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
