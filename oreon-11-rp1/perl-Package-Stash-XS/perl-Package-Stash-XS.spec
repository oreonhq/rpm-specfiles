%global source0_hash 26bad65c1959c57379b3e139dc776fbec5f702906617ef27cdc293ddf1239231

%if ! (0%{?rhel})
# Run optional test
%bcond_without perl_Package_Stash_XS_enables_optional_test
%else
%bcond_with perl_Package_Stash_XS_enables_optional_test
%endif

Name:		perl-Package-Stash-XS
Version:	0.30
Release:	13%{?dist}
Summary:	Faster and more correct implementation of the Package::Stash API
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Package-Stash-XS
Source0:        https://cpan.metacpan.org/modules/by-module/Package/Package-Stash-XS-%{version}.tar.gz



# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(B)
BuildRequires:	perl(base)
BuildRequires:	perl(blib)
BuildRequires:	perl(constant)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(lib)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Needs)
%if %{with perl_Package_Stash_XS_enables_optional_test}
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(Package::Anon)
BuildRequires:	perl(Variable::Magic)
%endif
# Dependencies
# (none)

# Don't "provide" private Perl libs
%{?perl_default_filter}

Provides:       perl(Package::Stash::XS)
%description
This is a back-end for Package::Stash, which provides the functionality in a
way that's less buggy and much faster. It will be used by default if it's
installed, and should be preferred in all environments with a compiler.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Package-Stash-XS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorarch}/auto/Package/
%{perl_vendorarch}/Package/
%{_mandir}/man3/Package::Stash::XS.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.30-13
- Prepare for Oreon 11 (RP1)
