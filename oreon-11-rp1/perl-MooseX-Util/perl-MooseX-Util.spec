%global source0_hash 974d5a174b458d6677d4e2ebe38ae9003fdfaf73667112ca6be493f7c75cb818

## Run optional test
#%%bcond_without perl_MooseX_Util_enables_optional_test

Name:           perl-MooseX-Util
Version:        0.006
Release:        26%{?dist}
Summary:        Moose::Util extensions
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://metacpan.org/release/MooseX-Util
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/MooseX-Util-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(MooseX::TraitFor::Meta::Class::BetterAnonClassNames) >= 0.002001
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
BuildRequires:  perl(Sub::Exporter::Progressive)
# Tests:
BuildRequires:  perl(aliased)
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Test::CheckDeps) >= 0.010
BuildRequires:  perl(Test::Moose::More) >= 0.016
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Requires)
#%%if %%{with perl_MooseX_Util_enables_optional_test} 
# Optional tests:
# Reindeer not yet packaged
# Reindeer::Role not yet packaged
#%%endif
Requires:       perl(Moose::Meta::Class)
Requires:       perl(MooseX::TraitFor::Meta::Class::BetterAnonClassNames) >= 0.002001

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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
