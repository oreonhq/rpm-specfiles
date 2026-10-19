%global source0_hash fdd63f32fc88d7dc035024a9fb30fc2f2cf70747a3c2dae2f168bf89fb48af06
%global gap_pkgname factint
%global gap_upname  FactInt
%global giturl      https://github.com/gap-packages/FactInt
Name:           gap-pkg-%{gap_pkgname}
Version:        1.7.0
Release:        1%{?dist}
Summary:        Advanced methods for factoring integers
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/FactInt/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): lib tables tst
BuildOption(check): tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
# /oreon:deps
%description
FactInt provides implementations of the following methods for factoring
integers:
- Pollard's p-1
- Williams' p+1
- Elliptic Curves Method (ECM)
- Continued Fraction Algorithm (CFRAC)
- Multiple Polynomial Quadratic Sieve (MPQS)
FactInt also makes use of Richard P. Brent's tables of known factors of
integers of the form bk+/-1 for "small" b.

The ECM method is suited best for finding factors which are neither too small
(i.e. have less than about 12 decimal digits) nor too close to the square root
of the number to be factored.  The MPQS method is designed for factoring
products of two primes of comparable orders of magnitude.  CFRAC is the
historical predecessor of the MPQS method.  Pollard's p-1 and Williams' p+1
are useful for finding factors p such that all prime factors of p-1
(respectively p+1) are "small", e.g. smaller than 1000000.  All factoring
methods implemented in this package are probabilistic.  In particular the time
needed by the ECM method depends largely on luck.

FactInt provides a general-purpose factorization routine which uses an
appropriate combination of the methods mentioned above, the Pollard Rho
routine which is implemented in the GAP Library and a variety of tricks for
special cases to obtain a good average performance for "arbitrary" integers.
At the user's option, FactInt provides detailed information about the progress
of the factorization process.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        FactInt documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-factint-doc -f %{oreon_filedir}/gap-pkg-factint-doc.list

%changelog

%autochangelog
