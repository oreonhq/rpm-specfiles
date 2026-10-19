%global source0_hash 974d5a174b458d6677d4e2ebe38ae9003fdfaf73667112ca6be493f7c75cb818
Name:           perl-MooseX-Util
Version:        0.006
Release:        26%{?dist}
Summary:        Moose::Util extensions
License:        LicenseRef-Callaway-LGPLv2
URL:            https://metacpan.org/release/MooseX-Util
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/MooseX-Util-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Moose::Meta::Class)
Requires:       perl(MooseX::TraitFor::Meta::Class::BetterAnonClassNames) >= 0.002001
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(MooseX::TraitFor::Meta::Class::BetterAnonClassNames)
BuildRequires:  perl(Sub::Exporter::Progressive)
BuildRequires:  perl(Test::CheckDeps)
BuildRequires:  perl(Test::Moose::More)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(aliased)
BuildRequires:  perl(blib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module handles all of the same functions that Moose::Util handles.
In fact, most of the functions are simply re-exports from Moose::Util.
However, we've re-implemented a number of the functions, for a variety of
reasons.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Util-%{version}

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
