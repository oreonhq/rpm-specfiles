%global source0_hash 8bc2f162bafc42645c489905ad72540f0d3c284b360c96299095183c30cc9789

# Perform optional tests
%bcond_without perl_JSON_PP_enables_optional_test

Name:		perl-JSON-PP
Epoch:		1
Version:	4.16
Release:	523%{?dist}
Summary:	JSON::XS compatible pure-Perl module
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/JSON-PP
Source0:	https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/JSON-PP-4.16.tar.gz

Patch0:		https://patch-diff.githubusercontent.com/raw/makamaka/JSON-PP/pull/93.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(lib)
# Module Runtime
BuildRequires:	perl(bytes)
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Math::BigFloat)
BuildRequires:	perl(Math::BigInt)
BuildRequires:	perl(overload)
BuildRequires:	perl(Scalar::Util) >= 1.08
BuildRequires:	perl(strict)
BuildRequires:	perl(utf8)
BuildRequires:	perl(warnings)
# Script Runtime
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Getopt::Long)
# Test Suite
BuildRequires:	perl(charnames)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Tie::Array)
BuildRequires:	perl(Tie::Hash)
BuildRequires:	perl(vars)
# Optional Tests
%if %{with perl_JSON_PP_enables_optional_test}
# Note: t/rt_122270_old_xs_boolean.t is testing for compatibility with old
# versions of JSON:XS and Types::Serialiser that we no longer use, so we
# don't include those modules as optional test dependencies
%if !%{defined perl_bootstrap}
# Disable non-core dependencies when bootstrapping a core module
BuildRequires:	perl(Tie::IxHash)
%endif
%endif
# Dependencies
Requires:	perl(Data::Dumper)
Requires:	perl(Encode)
Requires:	perl(Math::BigFloat)
Requires:	perl(Math::BigInt)
Requires:	perl(Scalar::Util) >= 1.08
Requires:	perl(utf8)
Conflicts:	perl-JSON < 2.50

%description
JSON::XS is the fastest and most proper JSON module on CPAN. It is written by
Marc Lehmann in C, so must be compiled and installed in the used environment.

JSON::PP is a pure-Perl module and is compatible with JSON::XS.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n JSON-PP-%{version}

# Silence Getopt::Long warning (fix already committed upstream)
# https://bugzilla.redhat.com/show_bug.cgi?id=2417867
# https://src.fedoraproject.org/rpms/perl-JSON-PP/pull-request/1
# https://github.com/makamaka/JSON-PP/issues/88
# https://github.com/makamaka/JSON-PP/pull/93
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{_bindir}/json_pp
%{perl_vendorlib}/JSON/
%{_mandir}/man1/json_pp.1*
%{_mandir}/man3/JSON::PP.3*
%{_mandir}/man3/JSON::PP::Boolean.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:4.16-523
- Import
