%global source0_hash 0f7d79f6d732569d934d4592dc06c2d3487173ece608208dc0886967bc6807d5

%global pkgname Storm

Name:           perl-Storm
Version:        0.240
Release:        35%{?dist}
Summary:        Object-relational mapping
License:        Artistic-2.0
URL:            https://metacpan.org/release/Storm
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHALLOCK/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime::Format::MySQL)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::SemiAffordanceAccessor)
BuildRequires:  perl(MooseX::StrictConstructor)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
# Tests
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(Test::More)

%description
Storm is a Moose based library for storing and retrieving objects over a
DBI connection.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README Storm.komodoproject
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
