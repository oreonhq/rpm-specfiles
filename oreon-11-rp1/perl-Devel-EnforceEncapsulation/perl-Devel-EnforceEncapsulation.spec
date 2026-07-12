%global source0_hash ffacf98fbe3c6289125068f7b7d7b54a956d049279a4bb3ddb0860095409a0b0

Name:		perl-Devel-EnforceEncapsulation
Version:	0.51
Release:	34%{?dist}
Summary:	Find access violations to blessed objects
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Devel-EnforceEncapsulation
Source0:	https://cpan.metacpan.org/modules/by-module/Devel/Devel-EnforceEncapsulation-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(English)
BuildRequires:	perl(overload)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(base)
BuildRequires:	perl(Test::More)
# Optional Tests
BuildRequires:	perl(Pod::Coverage) >= 0.17
BuildRequires:	perl(Test::Pod) >= 1.14
BuildRequires:	perl(Test::Pod::Coverage) >= 1.04
# Dependencies
# (none)

Provides:       perl(Devel::EnforceEncapsulation)
%description
Encapsulation is the practice of creating subroutines to access the properties
of a class instead of accessing those properties directly. The advantage of
good encapsulation is that the author is permitted to change the internal
implementation of a class without breaking its usage.

Object-oriented programming in Perl is most commonly implemented via blessed
hashes. This practice makes it easy for users of a class to violate
encapsulation by simply accessing the hash values directly. Although less
common, the same applies to classes implemented via blessed arrays, scalars,
filehandles, etc.

This module is a hack to block those direct accesses. If you try to access a
hash value of an object from its own class, or a superclass or subclass, all
goes well. If you try to access a hash value from any other package, an
exception is thrown. The same applies to the scalar value of a blessed scalar,
entry in a blessed array, etc.

To be clear: this class is NOT intended for strict enforcement of
encapsulation. If you want bullet-proof encapsulation, use inside-out objects
or the like. Instead, this module is intended to be a development or debugging
aid in catching places where direct access is used against classes implemented
as blessed hashes.

To repeat: the encapsulation enforced here is a hack and is easily
circumvented. Please use this module for good (finding bugs), not evil (making
life harder for downstream developers).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Devel-EnforceEncapsulation-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test AUTHOR_TEST=1 AUTHOR_TEST_CDOLAN=1

%files
%license LICENSE
%doc CHANGES README
%{perl_vendorlib}/Devel/
%{_mandir}/man3/Devel::EnforceEncapsulation.3*

%changelog
%autochangelog
