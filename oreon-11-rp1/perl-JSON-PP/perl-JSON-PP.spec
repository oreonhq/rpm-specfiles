%global source0_hash 9c7bcb238183c4240db5548b1910ce8428e0464d05e413df5893998e67bf602c
%bcond_without perl_JSON_PP_enables_optional_test
Name:		perl-JSON-PP
Epoch:		1
Version:	4.18
Release:        523%{?dist}
Summary:        JSON::XS compatible pure-Perl module
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/JSON-PP
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/JSON-PP-%{version}.tar.gz
BuildArch:	noarch
%if %{with perl_JSON_PP_enables_optional_test}
%if !%{defined perl_bootstrap}
%endif
%endif
Requires:	perl(Data::Dumper)
Requires:	perl(Encode)
Requires:	perl(Math::BigFloat)
Requires:	perl(Math::BigInt)
Requires:	perl(Scalar::Util) >= 1.08
Requires:	perl(utf8)
Conflicts:	perl-JSON < 2.50
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(bytes)
BuildRequires:  perl(charnames)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
JSON::XS is the fastest and most proper JSON module on CPAN. It is written by
Marc Lehmann in C, so must be compiled and installed in the used environment.

JSON::PP is a pure-Perl module and is compatible with JSON::XS.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n JSON-PP-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:4.16-523
- Import
