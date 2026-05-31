%global source0_hash 2a5bfd926c4fe5f77e6137da2c31ac2545282ae5fec6e9af0fdd403555a90ff4

%bcond perl_Unicode_EastAsianWidth_enables_Module_Package %{undefined rhel}

Name:		perl-Unicode-EastAsianWidth
Version:	12.0
Release:	20%{?dist}
Summary:	East Asian Width properties
License:	CC0-1.0
URL:		https://metacpan.org/release/Unicode-EastAsianWidth
Source0:        https://cpan.metacpan.org/authors/id/A/AU/AUDREYT/Unicode-EastAsianWidth-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(lib)
%if %{with perl_Unicode_EastAsianWidth_enables_Module_Package}
BuildRequires:	perl(Module::Package)
BuildRequires:	perl(Module::Package::Au)
%else
BuildRequires:	perl(inc::Module::Install)
%endif
BuildRequires:	perl(strict)
BuildRequires:	perl(Test)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
This module provide user-defined Unicode properties that deal with width
status of East Asian characters, as specified in
<http://www.unicode.org/unicode/reports/tr11/>.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Unicode-EastAsianWidth-%{version}
rm -rf inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
%if %{without perl_Unicode_EastAsianWidth_enables_Module_Package}
perl -i -ne 'print m{Au:dry} ? "use inc::Module::Install;" : $_' Makefile.PL
cat >> Makefile.PL <<_EOF
name 'Unicode-EastAsianWidth';
all_from 'lib/Unicode/EastAsianWidth.pm';
WriteAll;
_EOF
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Unicode/
%{_mandir}/man3/Unicode::EastAsianWidth.3pm*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12.0-20
- Prepare for Oreon 11 (RP1)
