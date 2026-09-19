%global source0_hash bfd309f283ac8cb9bf00af8c7c3a10bf25abfd642861c2022efaff0a4a52c276

Name:           perl-Math-Libm
Version:        1.00
Release:        47%{?dist}
Summary:        Perl extension for the C math library, libm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-Libm
Source0:        https://cpan.metacpan.org/authors/id/D/DS/DSLEWART/Math-Libm-%{version}.tar.gz
Source1:        Math-Libm-license.txt
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

%description
This module is a translation of the C math.h file. It exports the following
selected constants and functions:

M_1_PI M_2_PI M_2_SQRTPI M_E M_LN10 M_LN2 M_LOG10E M_LOG2E M_PI M_PI_2 M_PI_4
M_SQRT1_2 M_SQRT2 acos acosh asin asinh atan atanh cbrt ceil cosh erf erfc
expm1 floor hypot j0 j1 jn lgamma_r log10 log1p pow rint sinh tan tanh y0 y1 yn

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Libm-%{version}
install -m 0644 %{SOURCE1} license.txt

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license license.txt
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Math*
%{_mandir}/man3/*

%changelog
%autochangelog
