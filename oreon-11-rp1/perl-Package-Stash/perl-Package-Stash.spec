%global source0_hash 5a9722c6d9cb29ee133e5f7b08a5362762a0b5633ff5170642a5b0686e95e066
%bcond_with perl_Package_Stash_enables_optional_test
Name:		perl-Package-Stash
Version:	0.40
Release:        1%{?dist}
Summary:        Routines for manipulating stashes
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Package-Stash
Source0:        https://cpan.metacpan.org/modules/by-module/Package/Package-Stash-%{version}.tar.gz
BuildArch:	noarch
%if %{with perl_Package_Stash_enables_optional_test}
%endif
Requires:	perl(Package::Stash::XS) >= 0.26
Provides:	perl(Package::Stash::Conflicts) = 0
Provides:       perl(Package::Stash)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(CPAN::Meta::Check)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Dist::CheckConflicts)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Mksymlists)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Module::Implementation)
BuildRequires:  perl(Package::Stash::XS)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Manipulating stashes (Perl's symbol tables) is occasionally necessary, but
incredibly messy, and easy to get wrong. This module hides all of that behind
a simple API.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Package-Stash-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.40-11
- Prepare for Oreon 11 (RP1)
