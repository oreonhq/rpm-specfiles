%global source0_hash 6d7539e0be273d789575544f00c8ba1aa857d22f41d2cb3f40fa8681dc6f3b8e

Name:           perl-Date-Tiny
Version:        1.07
Release:        29%{?dist}
Summary:        Date object with as little code as possible
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Date-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Date-Tiny-%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.47

%{?perl_default_filter}

%description
Date::Tiny is a member of the DateTime::Tiny suite of time modules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Date-Tiny-%{version}
/usr/bin/perl -pi -e 's/en-US-POSIX/en-US/' t/02_main.t

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
%license LICENSE
%{perl_vendorlib}/Date*
%{_mandir}/man3/Date*

%changelog
%autochangelog
