%global source0_hash 068d272086514dd1e842b6a40b1bedbafee63900e5b08890ef6700039defad6f

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Sub_Identify_enables_optional_test
%else
%bcond_with perl_Sub_Identify_enables_optional_test
%endif

Name:		perl-Sub-Identify
Version:	0.14
Release:	32%{?dist}
Summary:	Retrieve names of code references
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Sub-Identify
Source0:        https://cpan.metacpan.org/authors/id/R/RG/RGARCIA/Sub-Identify-%{version}.tar.gz
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-interpreter
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(Config)
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(B)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(XSLoader)
# Test Suite
# feature required with perl ≥ 5.020
%if 0%{?fedora} > 21 || 0%{?rhel} > 7
BuildRequires:	perl(feature)
%endif
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(warnings)
%if %{with perl_Sub_Identify_enables_optional_test}
# Optional tests
BuildRequires:	perl(Test::Pod) >= 1.14
%endif
# Runtime
Requires:	perl(B)
Requires:	perl(XSLoader)

# Don't provide private perl libs
%{?perl_default_filter}

%description
Sub::Identify allows you to retrieve the real name of code references. For
this, it uses Perl's introspection mechanism, provided by the B module.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Sub-Identify-%{version}

# Fix script interpreters
perl -MConfig -pi -e 's|^#!perl|$Config{startperl}|' t/*

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
%doc Changes README.mdown TODO.mdown t/
%{perl_vendorarch}/auto/Sub/
%{perl_vendorarch}/Sub/
%{_mandir}/man3/Sub::Identify.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14-32
- Prepare for Oreon 11 (RP1)
