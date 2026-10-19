%global source0_hash 693f0f07ce25c6e0da6d8ff052068e4d529215e6fae39d3b085ae45aac8c95b7
Name:           perl-Test-Moose-More
Version:        0.050
Release:        1%{?dist}
Summary:        More tools for testing Moose packages
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Test-Moose-More
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/Test-Moose-More-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Test::More) >= 0.94
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::More\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::OptList)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Deprecated)
BuildRequires:  perl(Moose::Meta::Attribute)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter::Progressive)
BuildRequires:  perl(Syntax::Keyword::Junction)
BuildRequires:  perl(TAP::SimpleOutput)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::CheckDeps)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
