%global source0_hash f13a688369c1cb58b0c4479502702a277ae62354566439e4bab72e925847f845
Name:           perl-MooseX-Meta-TypeConstraint-ForceCoercion
Version:        0.01
Release:        1%{?dist}
Summary:        Force coercion when validating type constraints
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Meta-TypeConstraint-ForceCoercion
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/MooseX-Meta-TypeConstraint-ForceCoercion-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl-generators
# /oreon:deps
%description
This class allows to wrap any Moose::Meta::TypeConstraint in a way that
will force coercion of the value when checking or validating a value
against it.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Meta-TypeConstraint-ForceCoercion-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
