%global source0_hash a85803e68ab10deca49db67e47d7216480b151d2cfbc3ed32a9a0c0d22b558b7
%global source1_hash f51ba195fbb947681ea06a967aeae461df727d6417526afa4d215c3a54e679a4

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-pstricks
Epoch:          12
Version:        svn78101
Release:        1%{?dist}
Summary:        PostScript macros for TeX
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pstricks.r78101.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pstricks.doc.r78101.tar.xz
BuildRequires:  tar
Provides:       texlive-pstricks-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pstricks-doc <= 11:%{version}
Provides:       tex(pst-all.sty)
Provides:       tex(pst-key.sty)
Provides:       tex(pstcol.sty)
Provides:       tex(pstricks-pdf.sty)
Provides:       tex(pstricks.sty)
Provides:       tex(README.cfg)
Provides:       tex(distiller.cfg)
Provides:       tex(dvips.cfg)
Provides:       tex(dvipsone.cfg)
Provides:       tex(gastex.cfg)
Provides:       tex(pstricks-tex.def)
Provides:       tex(pstricks-xetex.def)
Provides:       tex(textures.cfg)
Provides:       tex(vtex.cfg)
Provides:       tex(xdvipdfmx.cfg)
Provides:       tex(pst-code-arc.tex)
Provides:       tex(pst-code-box.tex)
Provides:       tex(pst-code-circle_ellipse.tex)
Provides:       tex(pst-code-grid.tex)
Provides:       tex(pst-code-pspicture.tex)
Provides:       tex(pst-code-put.tex)
Provides:       tex(pst-code-ref_rot.tex)
Provides:       tex(pst-fp.tex)
Provides:       tex(pst-key.tex)
Provides:       tex(pstricks-arrows.tex)
Provides:       tex(pstricks-color.tex)
Provides:       tex(pstricks-dots.tex)
Provides:       tex(pstricks-plain.tex)
Provides:       tex(pstricks.tex)
Provides:       tex(pstricks97.tex)

%description
PostScript macros for TeX.

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
%doc %{_texmf_main}/doc/generic/pstricks/
%{_texmf_main}/dvips/pstricks/
%{_texmf_main}/tex/generic/pstricks/
%{_texmf_main}/tex/latex/pstricks/

%changelog
%autochangelog
