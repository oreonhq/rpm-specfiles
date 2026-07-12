%global source0_hash 15d0285e628a721138bcb1c36dea934379a89fdbc450fd79148e4e37a77241ba

Name:		perl-Package-Anon
Version:	0.05
Release:	44%{?dist}
Summary:	Anonymous packages
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Package-Anon
Source0:	https://cpan.metacpan.org/modules/by-module/Package/Package-Anon-%{version}.tar.gz
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(:VERSION) >= 5.14
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.30
# Module
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test suite
BuildRequires:	perl(FindBin)
BuildRequires:	perl(lib)
BuildRequires:	perl(overload)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::More)
# Release tests
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Test::EOL)
BuildRequires:	perl(Test::NoTabs)
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
BuildRequires:	perl(Test::Pod) >= 1.41

# Avoid private object provides
%{?perl_default_filter}

Provides:       perl(Package::Anon)
%description
This module allows for anonymous packages that are independent of the main
namespace and only available through an object instance, not by name.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Package-Anon-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test RELEASE_TESTING=1

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/Package/
%{perl_vendorarch}/Package/
%{_mandir}/man3/Package::Anon.3*

%changelog
%autochangelog
