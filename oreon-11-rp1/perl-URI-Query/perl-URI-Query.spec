%global source0_hash b4e62de79b468dcd7ee835e4dfd0035c83faf92e6c44b79bcdd9a50287fb8c18

# Perform an optional test
%bcond_without perl_URI_Query_enables_optional_test

Name:           perl-URI-Query
Version:        0.16
Release:        20%{?dist}
Summary:        Class providing URI query string manipulation
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/URI-Query
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GAVINC/URI-Query-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.5.30
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(vars)
# Tests:
# English not used
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(Test::More) >= 0.88
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
%if %{with perl_URI_Query_enables_optional_test}
# Optional tests:
BuildRequires:  perl(YAML)
%endif

%description
URI::Query provides simple URI query string manipulation, allowing you to
create and manipulate URI query strings from GET and POST requests in web
applications. This is primarily useful for creating links where you wish to
preserve some subset of the parameters to the current request, and potentially
add or replace others. Given a query string this is doable with regular
expressions, of course, but making sure you get the anchoring and escaping
right is tedious and error-prone - this module is simpler.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n URI-Query-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING RELEASE_TESTING
make test

%files
%license LICENSE
%doc ChangeLog README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
