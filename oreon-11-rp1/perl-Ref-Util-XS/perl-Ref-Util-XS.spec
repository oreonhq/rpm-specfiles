%global source0_hash fb64c5a823787f6600257918febd9fbc6f0305936fc3287b81a30c099b65633c

# Run optional tests
%if ! (0%{?rhel})
%bcond_without perl_Ref_Util_XS_enables_optional_test
%else
%bcond_with perl_Ref_Util_XS_enables_optional_test
%endif

Name:		perl-Ref-Util-XS
Version:	0.117
Release:	28%{?dist}
Summary:	Utility functions for checking references
License:	MIT
URL:		https://metacpan.org/release/Ref-Util-XS
Source0:        https://cpan.metacpan.org/modules/by-module/Ref/Ref-Util-XS-%{version}.tar.gz



# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(constant)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 0.94
%if %{with perl_Ref_Util_XS_enables_optional_test}
# Optional Tests
BuildRequires:	perl(B::Concise)
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(Readonly)
%endif
# Dependencies
# (none)

# Avoid provides for private objects
%{?perl_default_filter}

%description
Ref::Util::XS introduces several functions to help identify references in a
faster and smarter way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Ref-Util-XS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
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
%doc Changes README
%{perl_vendorarch}/auto/Ref/
%{perl_vendorarch}/Ref/
%{_mandir}/man3/Ref::Util::XS.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.117-28
- Prepare for Oreon 11 (RP1)
