%global source0_hash 866c4a9b547a81c79a27afee84dcd72af7e17affdbc0a6ac89eccc774a07b7be
Name:           perl-MooseX-TraitFor-Meta-Class-BetterAnonClassNames
Version:        0.002003
Release:        1%{?dist}
Summary:        Metaclass trait to attempt to demystify generated anonymous class names
License:        LicenseRef-Callaway-LGPLv2
URL:            https://metacpan.org/release/MooseX-TraitFor-Meta-Class-BetterAnonClassNames
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/MooseX-TraitFor-Meta-Class-BetterAnonClassNames-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Test::CheckDeps)
BuildRequires:  perl(Test::Moose::More)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(autobox::Core)
BuildRequires:  perl(blib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Moose meta class role helps with creating anonymous classes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-TraitFor-Meta-Class-BetterAnonClassNames-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=6.76
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
