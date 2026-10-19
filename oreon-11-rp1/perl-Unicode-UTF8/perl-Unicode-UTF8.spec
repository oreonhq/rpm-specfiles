%global source0_hash ca9dfbebf57cbe470dc68136ac792d6c89a38e7de5c7d2084b5c90e8d1010105
%if ! (0%{?rhel}) || (0%{?oreon} >= 11)
%bcond_without perl_Unicode_UTF8_enables_optional_test
%else
%bcond_with perl_Unicode_UTF8_enables_optional_test
%endif
Summary:        Encoding and decoding of UTF-8 encoding form
Name:		perl-Unicode-UTF8
Version:	0.68
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Unicode-UTF8
Source0:        https://cpan.metacpan.org/modules/by-module/Unicode/Unicode-UTF8-%{version}.tar.gz
%if %{with perl_Unicode_UTF8_enables_optional_test}
%endif
Requires:	perl(Carp)
Requires:	perl(Exporter)
Requires:	perl(XSLoader) >= 0.02
%{?perl_default_filter}
Provides:       perl(Unicode::UTF8)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::AssertC99)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Taint::Runtime)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Variable::Magic)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides functions to encode and decode UTF-8 encoding form as
specified by Unicode and ISO/IEC 10646:2011.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Unicode-UTF8-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.68-1
- Import
