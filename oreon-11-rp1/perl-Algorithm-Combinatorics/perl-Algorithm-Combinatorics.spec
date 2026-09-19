%global source0_hash 8378da39ecdb37d5cc89cc130a3b1353fd75d56c7690905673473fe4c25cd132

Name:           perl-Algorithm-Combinatorics
Version:        0.27
Release:        37%{?dist}
Summary:        Efficient generation of combinatorial sequences
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Algorithm-Combinatorics
Source0:        https://cpan.metacpan.org/modules/by-module/Algorithm/Algorithm-Combinatorics-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)

%description
Algorithm::Combinatorics is an efficient generator of combinatorial
sequences. Algorithms are selected from the literature. Iterators do
not use recursion, nor stacks, and are written in C.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Algorithm-Combinatorics-%{version}

%build
%{__perl} Makefile.PL NO_PACKLIST=1 INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README benchmarks
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Algorithm*
%{_mandir}/man3/*

%changelog
%autochangelog
