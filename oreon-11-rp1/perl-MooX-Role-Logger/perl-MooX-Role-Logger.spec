%global source0_hash d82325bb63f66ac82241f05ea4237ee33206bdd27415cbb6a889be6d5d6d800c

Name:           perl-MooX-Role-Logger
Version:        0.005
Release:        19%{?dist}
Summary:        Universal logging via Log::Any
License:        Apache-2.0

URL:            https://metacpan.org/release/MooX-Role-Logger
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/MooX-Role-Logger-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Test)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(warnings)

%description
This role provides universal logging via Log::Any. The class using this role
doesn't need to know or care about the details of log configuration,
implementation or destination.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n MooX-Role-Logger-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/MooX::Role::Logger*.*
%{_mandir}/man3/MooseX::Role::Logger*.*

%changelog
%autochangelog
