%global source0_hash 184a09b5c4582bbf9dd4791c22f95815fdeb716e886d0cc167d19963061c0133
Name:           perl-Array-Base
Version:        0.006
Release:        27%{?dist}
Summary:        Array index offsetting
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Array-Base
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Array-Base-%{version}.tar.gz
Conflicts:      perl(B::Hooks::OP::Check) < 0.19
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Lexical::SealRequireHints)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements automatic offsetting of array indices. In normal
Perl, the first element of an array has index 0, the second element has
index 1, and so on. This module allows array indexes to start at some
other value. Most commonly it is used to give the first element of an
array the index 1 (and the second 2, and so on), to imitate the indexing
behavior of FORTRAN and many other languages. It is usually considered
poor style to do this.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Array-Base-%{version}

%build

perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
