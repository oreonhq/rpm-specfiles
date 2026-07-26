%global source0_hash 184a09b5c4582bbf9dd4791c22f95815fdeb716e886d0cc167d19963061c0133

Name:           perl-Array-Base
Version:        0.006
Release:        27%{?dist}
Summary:        Array index offsetting
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Array-Base
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Array-Base-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(warnings)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Lexical::SealRequireHints) >= 0.008
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
Conflicts:      perl(B::Hooks::OP::Check) < 0.19

%{?perl_default_filter}

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

%check
./Build test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Array*
%{_mandir}/man3/*

%changelog
%autochangelog
