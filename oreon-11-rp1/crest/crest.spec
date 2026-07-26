%global source0_hash 390f0ac0aedafbd6bb75974fcffefe7e0232ad6c4ea0ab4f1a77e656a3ce263d

%global soname 6

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar o
%endif

Name:           crest
Version:        2.12
Release:        10%{?dist}
Summary:        Conformer-Rotamer Ensemble Sampling Tool: a driver for the xtb program
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://crest-lab.github.io/crest-docs/
Source0:        https://github.com/crest-lab/crest/archive/v%{version}/crest-%{version}.tar.gz

# Do not use "true" as a function name
Patch0:         https://github.com/crest-lab/crest/pull/397.patch

BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  %{blaslib}-devel
# To generate man pages
BuildRequires:  rubygem-asciidoctor

# xtb may be required to run tests
BuildRequires:  xtb
Requires:       xtb

# xtb is not available on s390x
ExcludeArch:    s390x

%description
CREST is an utility/driver program for the xtb program. Originally it
was designed as conformer sampling program, hence the abbreviation
Conformer-Rotamer Ensemble Sampling Tool, but now offers also some
utility functions for calculations with the GFNn-xTB
methods. Generally the program functions as an IO based OMP scheduler
(i.e., calculations are performed by the xtb program) and tool for the
creation and analysation of structure ensembles.

The key procedure implemented in CREST is a conformational search
workflow abbreviated as iMTD-GC. The iMTD-GC workflow generates
conformer/rotamer ensembles (CREs) by extensive metadynamic sampling
(MTD) based on, with an additional genetic z-matrix crossing (GC) step
at the end. Other standalone functionalities that are included in
CREST are parallel optimization and screening functions for GFNn–xTB,
the function to sort (e.g. for NMR equivalencies) externally created
ensembles, and some automated procedures for the protonation,
deprotonation and tautomerization of structures.

The main publication for the CREST program can be found at
Phys. Chem. Chem. Phys., 2020, 22, 7169-7192.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .notrue

%build
%meson -Dla_backend=custom -Dcustom_libraries=%{blaslib}%{blasvar}
%meson_build

%install
%meson_install

%check
%meson_test -t 2000

%files
%license COPYING COPYING.LESSER
%doc README.md
%{_bindir}/crest
%{_mandir}/man1/crest.1.*

%changelog
%autochangelog
