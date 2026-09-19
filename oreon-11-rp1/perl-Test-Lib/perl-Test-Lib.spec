%global source0_hash d84b48d92567cba3d0afb1e8175aab836bfa8a838e19ac9080cabc2e3f9dc9f5

Name:           perl-Test-Lib
Version:        0.003
Release:        12%{?dist}
Summary:        Use libraries from a t/lib directory
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Test-Lib
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Test-Lib-%{version}.tar.gz

BuildArch:      noarch
# build dependencies
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime dependencies
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test dependencies
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
Searches upward from the calling module for a directory t with a lib
directory inside it, and adds it to the module search path. Looks upward up
to 5 directories. This is intended to be used in test modules either
directly in t or in a sub-directory to find their included testing libraries
located in t/lib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Lib-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/Test*
%{_mandir}/man3/Test*

%changelog
%autochangelog
