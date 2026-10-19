%global source0_hash b59bb607bc9831b8224410946c33b12b82b252c662803835197821c2fb18f9e2
%global gap_pkgname edim
%global gap_upname  EDIM
%global gap_makedoc makedocrel.g
Name:           gap-pkg-%{gap_pkgname}
Version:        1.3.8
Release:        1%{?dist}
Summary:        Elementary divisors of integer matrices
License:        GPL-2.0-or-later
URL:            https://www.math.rwth-aachen.de/~Frank.Luebeck/EDIM/
VCS:            git:https://github.com/frankluebeck/EDIM.git
Source0:        https://www.math.rwth-aachen.de/~Frank.Luebeck/%{gap_upname}/%{gap_upname}-%{version}.tar.bz2
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): bin lib tst VERSION
BuildOption(check): tst/testall.g
Requires:       gap-core%{?_isa}
# oreon:deps
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
The main purpose of the EDIM package is to publish an implementation of an
algorithm (found by the package author) for computing prime parts of the
elementary divisors of integer matrices (i.e., the diagonal entries of the
Smith normal form).

The programs are developed and already successfully used for large matrices
(up to rank >12000) with moderate entries and many non-trivial elementary
divisors which are products of some small primes.  But they should be useful
for other types of matrices as well.

Among the other functions of the package are:
- an inversion algorithm for large rational matrices (using a p-adic method)
- a program for finding the largest elementary divisor of an integral matrix
  (particularly interesting when this is much smaller than the determinant)
  and
- implementations of some normal form algorithms described by Havas, Majewski,
  Matthews, Sterling (using LLL- or modular techniques).

%package doc
License:        GPL-2.0-or-later AND MPL-1.1 AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        EDIM documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%conf
# Fix encodings
for fil in doc/edim.bib doc/edim.bbl; do
  iconv -f iso8859-1 -t utf-8 $fil > $fil.utf8
  touch -r $fil $fil.utf8
  mv -f $fil.utf8 $fil
done

%build -p

./configure %{gap_archdir}
%make_build
sed -i.orig '/IsBound/ipathtoroot := "%{gap_libdir}";' makedocrel.g
%build -a

mv makedocrel.g.orig makedocrel.g
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-edim-doc -f %{oreon_filedir}/gap-pkg-edim-doc.list

%changelog

%autochangelog
