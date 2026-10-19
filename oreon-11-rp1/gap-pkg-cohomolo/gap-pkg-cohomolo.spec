%global source0_hash 9f68a987685affd3510a21c4a7d2b1260a6a98f237c5ac76531e4980616532a8
%global gap_pkgname cohomolo
%global giturl      https://github.com/gap-packages/cohomolo
Name:           gap-pkg-%{gap_pkgname}
Version:        1.7.1
Release:        1%{?dist}
Summary:        Cohomology groups of finite groups on finite modules
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/cohomolo/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
Patch:          %{name}-shebang.patch
Patch:          %{name}-lto.patch
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin gap htm testdata tst
BuildOption(check): tst/testall.g
Requires:       gap-core%{?_isa}
# oreon:deps
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tth
# /oreon:deps
%description
This package may be used to perform certain cohomological calculations on a
finite permutation group G.  The following properties of G can be computed:

1. The p-part Mul_p of the Schur multiplier Mul of G, and a presentation of a
   covering extension of Mul_p by G, for a specified prime p;

2. The dimensions of the first and second cohomology groups of G acting on a
   finite dimensional KG-module M, where K is a field of prime order; and

3. Presentations of split and nonsplit extensions of M by G.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Cohomolo documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{gap_upname}-%{version}

%conf
# Fix paths
sed -i 's,\.\./\.\./\.\./,%{gap_libdir}/,' doc/make_doc

%build

%global build_type_safety_c 0
%set_build_flags
export CC='gcc -std=gnu89'
./configure %{gap_archdir}
%make_build
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm ../../doc
%install -a
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/standalone
cp -a standalone/{data.d,info.d} \
   %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/standalone
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-cohomolo-doc -f %{oreon_filedir}/gap-pkg-cohomolo-doc.list

%changelog

%autochangelog
