%global source0_hash 288bc45908263245548f91482ab1248868dd9dee447f9ca26cad79613e3b94f5

Name:           perl-Math-ConvexHull-MonotoneChain
Version:        0.01
Release:        45%{?dist}
Summary:        Monotone chain algorithm for finding a convex hull in 2D
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-ConvexHull-MonotoneChain
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Math-ConvexHull-MonotoneChain-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More) >= 0.88

# Filters (not)shared c libs
%{?perl_default_filter}

%description
This is somewhat experimental still.

This (XS) module optionally exports a single function C<convex_hull>
which calculates the convex hull of the input points and returns it.
The algorithm is C<O(n log n)> due to having to sort the input list,
but should be somewhat faster than a plain Graham's scan (also C<O(n log n)>)
in practice since it avoids polar coordinates.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-ConvexHull-MonotoneChain-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Math*
%{_mandir}/man3/*

%changelog
%autochangelog
