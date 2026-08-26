%global source0_hash ef0f2f55858364f3d45e94677ba66a90c22bd2095ef78ead503fdc0986e1fbbfb72fac25b2d096c699208f672da63070269bbeacb46255cefda611c8c010004e
%global source1_hash d3448577c6cabe34b2d3e0614c2cceddc1d049c7f111e29d8b63959969033d0213af2de6d9eaeac5d1a4413a65a24054d69f7947655cdc8ae31b3d27b25b740d

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/platex-tools.r72097.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/platex-tools.doc.r72097.tar.xz
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
