%global source0_hash 693f0f07ce25c6e0da6d8ff052068e4d529215e6fae39d3b085ae45aac8c95b7

Name:           perl-Test-Moose-More
Version:        0.050
Release:        25%{?dist}
Summary:        More tools for testing Moose packages
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Test-Moose-More
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/Test-Moose-More-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::OptList)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter::Progressive)
BuildRequires:  perl(Syntax::Keyword::Junction)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.94
# Tests only:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Deprecated)
BuildRequires:  perl(Moose::Meta::Attribute)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(TAP::SimpleOutput) >= 0.009
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::CheckDeps) >= 0.010
Requires:       perl(Test::More) >= 0.94

# Removed under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::More\\)$

%description
This package contains a number of additional tests that can be employed
against Moose classes/roles. It is intended to replace Test::Moose.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Moose-More-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
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
