%global source0_hash 741d31c8608500d4039f67b21d098b148c487b56f4bd90388cdd04f10bc7953b

Name:           perl-String-Base
Version:        0.003
Release:        28%{?dist}
Summary:        String index offsetting
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/String-Base
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/String-Base-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
# Run-Time:
BuildRequires:  perl(Lexical::SealRequireHints) >= 0.006
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
Conflicts:      perl(B::Hooks::OP::Check) < 0.19

%{?perl_default_filter}

%description
This module implements automatic offsetting of string indices. In normal
Perl, the first character of a string has index 0, the second character has
index 1, and so on. This module allows string indexes to start at some
other value. Most commonly it is used to give the first character of a
string the index 1 (and the second 2, and so on), to imitate the indexing
behavior of FORTRAN and many other languages. It is usually considered
poor style to do this.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n String-Base-%{version}

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/String*
%{_mandir}/man3/*

%changelog
%autochangelog
