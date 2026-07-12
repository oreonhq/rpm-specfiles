%global source0_hash 5bc22cf536ebfd2564c5bdaf42f0d8a4cee3d1930fc8b44b7d4a42038622add1

Name:		perl-Class-Load-XS
Version:	0.10
Release:	30%{?dist}
Summary:	XS implementation of parts of Class::Load
License:	Artistic-2.0
URL:		https://metacpan.org/release/Class-Load-XS
Source0:	https://cpan.metacpan.org/modules/by-module/Class/Class-Load-XS-%{version}.tar.gz
# ===================================================================
# Module build requirements
# ===================================================================
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# ===================================================================
# Module requirements
# ===================================================================
BuildRequires:	perl(Class::Load) >= 0.20
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# ===================================================================
# Regular test suite requirements
# ===================================================================
BuildRequires:	perl(constant)
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(lib)
BuildRequires:	perl(Module::Implementation) >= 0.04
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Needs)
BuildRequires:	perl(Test::Without::Module)
BuildRequires:	perl(version)
# ===================================================================
# Runtime requirements
# ===================================================================
# (none)

%{?perl_default_filter}

Provides:       perl(Class::Load::XS)
Provides:       perl(Class::Load::XS)
%description
This module provides an XS implementation for portions of Class::Load.
See Class::Load for API details.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Class-Load-XS-%{version}

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
%{perl_vendorarch}/auto/Class/
%{perl_vendorarch}/Class/
%{_mandir}/man3/Class::Load::XS.3*

%changelog
%autochangelog
