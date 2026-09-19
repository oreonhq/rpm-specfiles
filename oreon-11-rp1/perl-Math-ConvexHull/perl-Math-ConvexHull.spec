%global source0_hash b9041f08d58792308f204455a67a265799e88b279e5c2f54e3f8dee9594c0852

Name:           perl-Math-ConvexHull
Version:        1.04
Release:        38%{?dist}
Summary:        Calculate convex hulls using Graham's scan (n*log(n))
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-ConvexHull
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Math-ConvexHull-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  dos2unix
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)

%description
Math::ConvexHull is a simple module that calculates convex hulls from a set
of points in 2D space. It is a straightforward implementation of the
algorithm known as Graham's scan which, with complexity of O(n*log(n)), is
the fastest known method of finding the convex hull of an arbitrary set of
points. There are some methods of eliminating points that cannot be part of
the convex hull. These may or may not be implemented in a future version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-ConvexHull-%{version}
dos2unix Changes

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
