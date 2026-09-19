%global source0_hash f13a688369c1cb58b0c4479502702a277ae62354566439e4bab72e925847f845

Name:           perl-MooseX-Meta-TypeConstraint-ForceCoercion
Version:        0.01
Release:        44%{?dist}
Summary:        Force coercion when validating type constraints
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/MooseX-Meta-TypeConstraint-ForceCoercion
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/MooseX-Meta-TypeConstraint-ForceCoercion-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Moose)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

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

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Moose*
%{_mandir}/man3/Moose*

%changelog
%autochangelog
