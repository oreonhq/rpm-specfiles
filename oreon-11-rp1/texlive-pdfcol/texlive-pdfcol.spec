%global source0_hash dd39b6c4a353726e10741c3adbc5483a32b7d3ab87bf29186893935e977b706d248783f9750a39bb0c547d8c796a1ac37cc77d333beb4bd7694c3a91a05dea89
%global source1_hash 63b5fb6d32f9224cad3c7f4c6c6465c0ce0f0715e2677b6016c100731c034ff296d9ee168769216f9fcf5bf257008fe480487b6e5b03db43d9c8af2cd7ebc76e

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-pdfcol
Epoch:          12
Version:        svn64469
Release:        1%{?dist}
Summary:        Macros for maintaining colour stacks under pdfTeX
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfcol.r79618.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfcol.doc.r79618.tar.xz
BuildRequires:  tar
Provides:       texlive-pdfcol-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pdfcol-doc <= 11:%{version}
Provides:       tex(pdfcol.sty)

%description
Macros for maintaining colour stacks under pdfTeX.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

%build

%install
mkdir -p %{buildroot}%{_texmf_main}
tar -xf %{SOURCE0} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE1} -C %{buildroot}%{_texmf_main}
rm -rf %{buildroot}%{_texmf_main}/tlpkg

%files
%doc %{_texmf_main}/doc/latex/pdfcol/
%{_texmf_main}/tex/latex/pdfcol/

%changelog
%autochangelog
