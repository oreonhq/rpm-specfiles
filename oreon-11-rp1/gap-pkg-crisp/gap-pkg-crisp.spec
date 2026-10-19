%global source0_hash 3360e17c1611a2ab1654d982aade5566a1c048c795675e321cbf15d06248d569
%global gap_pkgname crisp
%global giturl      https://github.com/bh11/crisp
Name:           gap-pkg-%{gap_pkgname}
Version:        1.4.8
Release:        1%{?dist}
Summary:        Computing subgroups of finite soluble groups
License:        BSD-2-Clause
URL:            http://www.icm.tu-bs.de/~bhoeflin/crisp/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/CrISP-%{version}/%{gap_pkgname}-%{version}.tar.bz2
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): htm lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  tth
# /oreon:deps
%description
CRISP (Computing with Radicals, Injectors, Schunck classes and Projectors)
provides algorithms for computing subgroups of finite soluble groups related
to group classes.  In particular, it allows computing F-radicals and
F-injectors for Fitting classes (and Fitting sets) F, F-residuals for
formations F, and X-projectors for Schunck classes X.  In order to carry out
these computations, the group classes F and X must be given by an algorithm
which decides membership in the group class.

Moreover, CRISP contains algorithms for the computation of normal subgroups
invariant under a prescribed set of automorphisms and belonging to a given
group class.  This includes an improved method to compute the set of all
normal subgroups of a finite soluble group, its characteristic subgroups, and
the socle and p-socles for given primes p.

%package doc
License:        BSD-2-Clause AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND LicenseRef-Rsfs AND GPL-1.0-or-later
Summary:        CRISP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%build

ln -s %{gap_libdir}/doc ../../doc
pushd doc
pdftex manual
makeindex -s manual.mst manual
pdftex manual
pdftex manual
popd
rm -fr htm
mkdir htm
perl %{gap_libdir}/etc/convert.pl -n CRISP -c -i -t doc htm
rm ../../doc
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-crisp-doc -f %{oreon_filedir}/gap-pkg-crisp-doc.list

%changelog

%autochangelog
