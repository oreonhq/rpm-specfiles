# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Package_Stash_enables_optional_test
%else
%bcond_with perl_Package_Stash_enables_optional_test
%endif

Name:		perl-Package-Stash
Version:	0.40
Release:	11%{?dist}
Summary:	Routines for manipulating stashes
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Package-Stash
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Package-Stash-0.40.tar.gz
# oreon url source checksums begin
%global source0_sha256 5a9722c6d9cb29ee133e5f7b08a5362762a0b5633ff5170642a5b0686e95e066
%global source0_file Package-Stash-0.40.tar.gz
# oreon url source checksums end

BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Config)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::Mksymlists)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Text::ParseWords)
# Module Runtime
BuildRequires:	perl(B)
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Dist::CheckConflicts) >= 0.02
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Module::Implementation) >= 0.06
BuildRequires:	perl(Package::Stash::XS) >= 0.26
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(base)
BuildRequires:	perl(CPAN::Meta::Check) >= 0.011
BuildRequires:	perl(CPAN::Meta::Requirements)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Needs)
%if %{with perl_Package_Stash_enables_optional_test}
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(Module::Runtime::Conflicts)
BuildRequires:	perl(Package::Anon)
BuildRequires:	perl(Variable::Magic)
%endif
# Dependencies
# For performance and consistency
Requires:	perl(Package::Stash::XS) >= 0.26
# Not found by rpm auto-provides
Provides:	perl(Package::Stash::Conflicts) = 0

%description
Manipulating stashes (Perl's symbol tables) is occasionally necessary, but
incredibly messy, and easy to get wrong. This module hides all of that behind
a simple API.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Package-Stash-0.40.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5a9722c6d9cb29ee133e5f7b08a5362762a0b5633ff5170642a5b0686e95e066" || { echo "oreon: Source0 SHA256 mismatch for Package-Stash-0.40.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Package-Stash-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{_bindir}/package-stash-conflicts
%{perl_vendorlib}/Package/
%{_mandir}/man3/Package::Stash.3*
%{_mandir}/man3/Package::Stash::PP.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.40-11
- Prepare for Oreon 11 (RP1)
