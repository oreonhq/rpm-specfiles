%global source0_hash 0a31cf1265dcee90bbc42456ad60bb363afc7fac6697fffb0fd49bba92a165d2

Name:           perl-Test-Spec
Version:        0.54
Release:        24%{?dist}
Summary:        Write tests in a declarative specification style
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Spec
Source0:        https://cpan.metacpan.org/authors/id/A/AK/AKZHAN/Test-Spec-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Package::Stash) >= 0.23
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util) >= 1.11
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Deep) >= 0.103
BuildRequires:  perl(Test::Deep::NoTest)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Tie::StdHash)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Devel::GlobalPhase)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(overload)
BuildRequires:  perl(TAP::Parser)
Requires:       perl(Package::Stash) >= 0.23
Requires:       perl(Scalar::Util) >= 1.11
Requires:       perl(Test::Deep) >= 0.103
Requires:       perl(Test::More) >= 0.88

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Scalar::Util\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::More\\)$

%description
This is a declarative specification-style testing system for behavior-driven
development (BDD) in Perl. The tests (a.k.a. examples) are named with strings
instead of subroutine names, so your fingers will suffer less fatigue from
underscore-itis, with the side benefit that the test reports are more legible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Spec-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
