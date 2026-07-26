%global source0_hash 14349eeca530b1a9e96092787b49167587044bea07938d4ab4a08fb5ab2209c8

# This file is licensed under the terms of GNU GPLv2+
Name:           perl-smartmatch
Version:        0.05
Release:        40%{?dist}
Summary:        Pluggable smart matching back-ends
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/smartmatch
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOY/smartmatch-%{version}-TRIAL.tar.gz
# Restore compatibility with Perl 5.26.0,
# <https://github.com/tokuhirom/B-Tap/issues/4>
Patch0:         smartmatch-0.05-TRIAL-Fix-building-on-Perl-5.25.1.patch
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(B::Hooks::OP::Check) >= 0.14
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(parent)
# Tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
BuildRequires:  perl(Test::Script) >= 1.05

%{?perl_default_filter}

%description
This module allows you to override the behavior of the smart match operator
("~~"). "use smartmatch $matcher" hooks into the compiler to replace the
smartmatch opcode with a call to a custom subroutine, specified either as
a coderef or as a string, which will have "smartmatch::engine::" prepended to
it and used as the name of a package in which to find a subroutine named
"match".  The subroutine will be called with two arguments, the values on the
left and right sides of the smart match operator, and should return the
result.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n smartmatch-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/smartmatch*
%{_mandir}/man3/*

%changelog
%autochangelog
