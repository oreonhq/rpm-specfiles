%global source0_hash ca9dfbebf57cbe470dc68136ac792d6c89a38e7de5c7d2084b5c90e8d1010105

# Run optional test
%if ! (0%{?rhel}) || (0%{?oreon} >= 11)
%bcond_without perl_Unicode_UTF8_enables_optional_test
%else
%bcond_with perl_Unicode_UTF8_enables_optional_test
%endif

Summary:	Encoding and decoding of UTF-8 encoding form
Name:		perl-Unicode-UTF8
Version:	0.68
Release:	1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Unicode-UTF8
Source0:        https://cpan.metacpan.org/modules/by-module/Unicode/Unicode-UTF8-%{version}.tar.gz



# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Devel::AssertC99)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader) >= 0.02
# Test Suite
BuildRequires:	perl(Encode) >= 1.9801
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(lib)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::Fatal) >= 0.006
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(utf8)
%if %{with perl_Unicode_UTF8_enables_optional_test}
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(Taint::Runtime) >= 0.03
BuildRequires:	perl(Test::LeakTrace) >= 0.10
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Variable::Magic)
%endif
# Dependencies
Requires:	perl(Carp)
Requires:	perl(Exporter)
Requires:	perl(XSLoader) >= 0.02

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
This module provides functions to encode and decode UTF-8 encoding form as
specified by Unicode and ISO/IEC 10646:2011.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Unicode-UTF8-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/Unicode/
%{perl_vendorarch}/auto/Unicode/
%{_mandir}/man3/Unicode::UTF8.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.68-1
- Import
