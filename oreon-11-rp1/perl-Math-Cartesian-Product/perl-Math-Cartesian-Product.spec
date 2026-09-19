%global source0_hash d0bf24e56aaebe47c9db6d09c257bc3bf5af2d0d69f060fe33c180a9c7199f32

Name:           perl-Math-Cartesian-Product
Version:        1.009
Release:        25%{?dist}
Summary:        Generate the Cartesian product of zero or more lists
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-Cartesian-Product
Source0:        https://cpan.metacpan.org/authors/id/P/PR/PRBRENAN/Math-Cartesian-Product-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.42
# Run-time:
BuildRequires:  perl(:VERSION) >= 5
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
This Perl module implements general Cartesian product of zero or more lists.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Cartesian-Product-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
