%global source0_hash d6cde3dda751597ad741f634f143a3eb521b957fd1a23ceefba78a2716422d8e

Name:           R-ape
Version:        %R_rpm_version 5.8-1
Release:        %autorelease
Summary:        Analyses of Phylogenetics and Evolution

License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildRequires:  R-devel

%description
Functions for reading, writing, plotting, and manipulating phylogenetic
trees, analyses of comparative data in a phylogenetic framework, ancestral
character analyses, analyses of diversification and macroevolution,
computing distances from DNA sequences, reading and writing nucleotide
sequences as well as importing from BioConductor, and several tools such as
Mantel's test, generalized skyline plots, graphical exploration of
phylogenetic data (alex, trex, kronoviz), estimation of absolute
evolutionary rates and clock-like trees using mean path lengths and
penalized likelihood, dating trees with non-contemporaneous sequences,
translating DNA into AA sequences, and assessing sequence alignments.
Phylogeny estimation can be done with the NJ, BIONJ, ME, MVR, SDM, and
triangle methods, and several methods handling incomplete distance matrices
(NJ*, BIONJ*, MVR*, and the corresponding triangle method). Some functions call
external applications (PhyML, Clustal, T-Coffee, Muscle) whose results are
returned into R.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
