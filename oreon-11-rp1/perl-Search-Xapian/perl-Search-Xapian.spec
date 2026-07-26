%global source0_hash 204fbdc712d6711ffab668c1f4cfc007b639a9fb64ad7e19cb20fc10a910ba8b

Name:           perl-Search-Xapian
Version:        1.2.25.5
Release:        15%{?dist}
Summary:        Xapian perl bindings
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Search-Xapian
Source0:        https://cpan.metacpan.org/authors/id/O/OL/OLLY/Search-Xapian-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  xapian-core-devel
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Devel::Leak)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)

%{?perl_default_filter}

%description
This module wraps most methods of most Xapian classes. The missing classes
and methods should be added in the future. It also provides a simplified,
more 'perlish' interface to some common operations, as demonstrated above.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Search-Xapian-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorarch}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
