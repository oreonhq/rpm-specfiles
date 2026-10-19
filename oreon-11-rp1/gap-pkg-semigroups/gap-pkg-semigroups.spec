%global source0_hash 4a0d2ef30a01e5fa890fb877a58577dbcb1c7d9d977d6b91042eedfaf920008a
%global gap_pkgname semigroups
%global giturl      https://github.com/semigroups/Semigroups
%bcond bigtest 0
Name:           gap-pkg-%{gap_pkgname}
Version:        5.7.0
Release:        1%{?dist}
Summary:        GAP methods for semigroups
License:        GPL-3.0-or-later
URL:            https://semigroups.github.io/Semigroups/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): bin data gap tst .LIBSEMIGROUPS_VERSION
BuildOption(check): tst/testall.g
%ifarch %{arm64}
%endif
Requires:       gap-pkg-datastructures%{?_isa}
Requires:       gap-pkg-digraphs%{?_isa}
Requires:       gap-pkg-genss
Requires:       gap-pkg-images
Requires:       gap-pkg-io%{?_isa}
Requires:       gap-pkg-orb%{?_isa}
Suggests:       gap-pkg-grape%{?_isa}
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-datastructures
BuildRequires:  gap-pkg-digraphs-doc
BuildRequires:  gap-pkg-ferret
BuildRequires:  gap-pkg-genss
BuildRequires:  gap-pkg-grape
BuildRequires:  gap-pkg-images-doc
BuildRequires:  gap-pkg-io-doc
BuildRequires:  gap-pkg-orb
BuildRequires:  gap-pkg-smallsemi-doc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libsemigroups)
BuildRequires:  tex(a4.sty)
BuildRequires:  tex(a4wide.sty)
# /oreon:deps
%description
This is a GAP package containing methods for semigroups, monoids, and inverse
semigroups, principally of transformations, partial permutations,
bipartitions, subsemigroups of regular Rees 0-matrix semigroups, free inverse
semigroups, free bands, and semigroups of matrices over finite fields.

Semigroups contains more efficient methods than those available in the GAP
library (and in many cases more efficient than any other software) for
creating semigroups, monoids, and inverse semigroup, calculating their Green's
structure, ideals, size, elements, group of units, small generating sets,
testing membership, finding the inverses of a regular element, factorizing
elements over the generators, and many more.  It is also possible to test if a
semigroup satisfies a particular property, such as if it is regular, simple,
inverse, completely regular, and a variety of further properties.

There are methods for finding congruences of certain types of semigroups, the
normalizer of a semigroup in a permutation group, the maximal subsemigroups of
a finite semigroup, and smaller degree partial permutation representations of
inverse semigroups.  There are functions for producing pictures of the Green's
structure of a semigroup, and for drawing bipartitions.

%package doc
License:        GPL-3.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        Semigraphs documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc
Requires:       gap-pkg-digraphs-doc
Requires:       gap-pkg-images-doc
Requires:       gap-pkg-io-doc
Requires:       gap-pkg-smallsemi-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

%autosetup -n %{gap_upname}-%{version} -p1

%conf
# Do not use the bundled libsemigroups
rm -fr libsemigroups

# Do not override our build flags
sed -i 's/ -O3//' GNUmakefile.in

# Do not add an rpath
sed -i '/rpath/s/\(LIBSEMIGROUPS_RPATH=\).*/\1/' configure

# Work around -Wl,--as-needed appearing too late on the command line
sed -i 's/GAP_CXX :=.*/& -Wl,--as-needed/' Makefile.gappkg

# Specify a minimum libsemigroups version
echo 3.5.3 > .LIBSEMIGROUPS_VERSION

%build -p

export CPPFLAGS='-I%{_includedir}/eigen3'
%configure \
    --disable-silent-rules \
%ifarch %{arm64}
    --enable-hpcombi \
%else
    --disable-hpcombi \
%endif
    --with-external-libsemigroups \
    --with-gaproot=%{gap_archdir}
%make_build
%check

cd tst
gap -l '%{buildroot}%{gap_archdir};' << EOF
LoadPackage("semigroups");
GAP_EXIT_CODE(Test("testinstall.tst", rec( compareFunction := "uptowhitespace" )));
EOF
%if %{with bigtest}
gap -l '%{buildroot}%{gap_archdir};' teststandard.g
%endif
cd -
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-semigroups-doc -f %{oreon_filedir}/gap-pkg-semigroups-doc.list

%changelog

%autochangelog
