%global source1_hash 52f36c6645f909c27a7b1d419563bca9c49e52a16434ba24ad1b1e8c23742002
%global source0_hash 7e4a7bf219998a844c0bcce0a176e49d0743cb4b505a0e195329bf2ec196ddd7
Name:           palp
Version:        2.21
Release:        1%{?dist}
Summary:        A Package for Analyzing Lattice Polytopes
License:        GPL-3.0-or-later
URL:            http://hep.itp.tuwien.ac.at/~kreuzer/CY/CYpalp.html
VCS:            git:https://gitlab.com/stringstuwien/PALP.git
Source0:        http://hep.itp.tuwien.ac.at/~kreuzer/CY/palp/palp-%{version}.tar.gz
Source1:        https://export.arxiv.org/pdf/1205.4147
Patch:          %{name}-unlink.patch
Patch:          %{name}-latte.patch
Patch:          %{name}-use-after-free.patch
%global _docdir_fmt %{name}
Requires:       coreutils
Requires:       gawk
Requires:       grep
Recommends:     latte-integrale
Recommends:     Singular
# oreon:deps
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  make
# /oreon:deps
%description
PALP contains routines for vertex and facet enumeration, computation of
incidences and symmetries, as well as completion of the set of lattice
points in the convex hull of a given set of points. In addition, there
are procedures specialized to reflexive polytopes such as the enumeration
of reflexive subpolytopes, and applications to toric geometry and string
theory, like the computation of Hodge data and fibration structures for
toric Calabi-Yau varieties.

%package doc
License:        GPL-3.0-or-later AND Knuth-CTAN AND OFL-1.1-RFN
Summary:        Documentation for palp
%description doc
Documentation for palp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

cp -p %{SOURCE1} 1205.4147v1.pdf
mkdir bin man
mv Global.h Global.h-template
for dim in 4 5 6 11; do
    echo Building PALP optimized for $dim dimensions
    sed "s/^#define[^a-zA-Z]*POLY_Dmax.*/#define POLY_Dmax $dim/" Global.h-template > Global.h
    %make_build
    for file in poly class cws nef mori; do
        mv ${file}.x bin/${file}-${dim}d.x
        help2man -N --version-string=%{version} -h -h bin/${file}-${dim}d.x \
            <<< e | sed '$d' | sed '$d' | sed '$d' > man/${file}-${dim}d.x.1
    done
    make cleanall
done
for file in poly class cws nef mori; do
    help2man -N --version-string=%{version} -h -h bin/${file}.x \
        <<< e | sed '$d' | sed '$d' | sed '$d' > man/${file}.x.1
done
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
pushd bin
    for exe in *.x; do
	install -m 755 $exe $RPM_BUILD_ROOT%{_bindir}/$exe
    done
popd
for file in poly class cws nef mori; do
    ln -sf ${file}-6d.x $RPM_BUILD_ROOT%{_bindir}/${file}.x
done
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -p man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n palp-doc -f %{oreon_filedir}/palp-doc.list

%changelog

%autochangelog
