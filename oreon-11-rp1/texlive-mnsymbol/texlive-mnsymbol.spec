%global source0_hash 7bdaf593dda367c23342fc4d3c551c736a50ceeb5d28eed99feb9779afd91038
%global source1_hash 23d20766a3118d6c513c55432304046d5431076116191b67f6e3c5b9232725ff

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-mnsymbol
Epoch:          12
Version:        svn18651
Release:        1%{?dist}
Summary:        Mathematical symbol font for Adobe MinionPro
License:        OFL-1.1
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mnsymbol.r18651.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mnsymbol.doc.r18651.tar.xz
BuildRequires:  tar
Provides:       texlive-mnsymbol-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-mnsymbol-doc <= 11:%{version}
Provides:       tex(MnSymbol.sty)

%description
Mathematical symbol font for Adobe MinionPro.

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
%doc %{_texmf_main}/doc/latex/mnsymbol/
%{_texmf_main}/fonts/enc/dvips/mnsymbol/
%{_texmf_main}/fonts/map/dvips/mnsymbol/
%{_texmf_main}/fonts/map/vtex/mnsymbol/
%{_texmf_main}/fonts/opentype/public/mnsymbol/
%{_texmf_main}/fonts/source/public/mnsymbol/
%{_texmf_main}/fonts/tfm/public/mnsymbol/
%{_texmf_main}/fonts/type1/public/mnsymbol/
%{_texmf_main}/tex/latex/mnsymbol/

%changelog
%autochangelog
