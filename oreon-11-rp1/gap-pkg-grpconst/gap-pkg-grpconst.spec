%global source0_hash 683bf2e3245b3a83bdb189ccb20327eaec7ca4ac116ea9d45a39167be73dd9eb
%global gap_pkgname grpconst
%global giturl      https://github.com/gap-packages/grpconst
Name:           gap-pkg-%{gap_pkgname}
Version:        2.7.0
Release:        1%{?dist}
Summary:        Constructing groups of a given order
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/grpconst/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap htm tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-autpgrp
Requires:       gap-pkg-irredsol
Requires:       gap-pkg-smallgrp
# oreon:deps
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autpgrp
BuildRequires:  gap-pkg-irredsol
BuildRequires:  gap-pkg-smallgrp
BuildRequires:  tth
# /oreon:deps
%description
This package contains GAP implementations of three different approaches to
constructing up to isomorphism all groups of a given order.

The FrattiniExtensionMethod constructs all soluble groups of a given order.
On request it gives only those that are (or are not) nilpotent or
supersolvable or that do (or do not) have normal Sylow subgroups for some
given set of primes.  The program's output may be expressed in a compact coded
form, if desired.

The CyclicSplitExtensionMethod constructs all (necessarily soluble) groups
whose given orders are of the form p^n*q for different primes p and q and
which have at least one normal Sylow subgroup.  The method, which relies upon
having available a list of all groups of order p^n, is often faster than the
Frattini extension method for the groups to which it applies.

The UpwardsExtensions method takes as its input a permutation group G and
positive integer s and returns a list of permutation groups, one for each
extension of G by a soluble group of order a divisor of s.  Usually it is used
for nonsoluble G only, since for soluble groups the above methods are more
efficient.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        GrpConst documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%build

ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc}
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-grpconst-doc -f %{oreon_filedir}/gap-pkg-grpconst-doc.list

%changelog

%autochangelog
