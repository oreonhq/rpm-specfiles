%global source0_hash 7128746c6251c4dbeebe2509f035aa37993d2f2cd534ce145dbd5e136d63c75e
%global source1_hash 9876dd5838b4b6933e1a653a07dc775789963e84ac4c963f70f6e8b9e34fced7

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-platex-tools
Epoch:          12
Version:        svn72097
Release:        1%{?dist}
Summary:        pLaTeX utility tools
License:        BSD
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/platex-tools.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/platex-tools.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-platex-tools-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-platex-tools-doc <= 11:%{version}
Provides:       tex(plarray.sty)
Provides:       tex(pldocverb.sty)
Provides:       tex(plextarray.sty)
Provides:       tex(plextcolortbl.sty)
Provides:       tex(plextdelarray.sty)
Provides:       tex(pxatbegshi.sty)
Provides:       tex(pxeverysel.sty)
Provides:       tex(pxeveryshi.sty)
Provides:       tex(pxftnright.sty)
Provides:       tex(pxmulticol.sty)
Provides:       tex(pxxspace.sty)

%description
pLaTeX utility tools.

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
%doc %{_texmf_main}/doc/latex/platex-tools/
%{_texmf_main}/tex/latex/platex-tools/

%changelog
%autochangelog
