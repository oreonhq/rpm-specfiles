%global source0_hash 726fc6c9ae3519ae074b8ba8bc23ee95398e759911009ed3cb3554dcdf9068c54335c45cef03005677c95ee5864f78e786c996c6f7bb6c0622f6edf87db78784
%global source1_hash f20945cf5c1205422dd697b541eb8ab6b84f065a7193cf32366516907c7f851c07b579729bc45cc903fa086f12b15b405f427d5b045a9b19629853a7b2f758f9

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-bidi
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Bidirectional typesetting in plain TeX and LaTeX
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidi.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidi.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-bidi-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-bidi-doc <= 11:%{version}
Provides:       tex(adjmulticol-xetex-bidi.def)
Provides:       tex(algorithm2e-xetex-bidi.def)
Provides:       tex(amsart-xetex-bidi.def)
Provides:       tex(amsbook-xetex-bidi.def)
Provides:       tex(amsmath-xetex-bidi.def)
Provides:       tex(amstext-xetex-bidi.def)
Provides:       tex(amsthm-xetex-bidi.def)
Provides:       tex(array-xetex-bidi.def)
Provides:       tex(article-xetex-bidi.def)
Provides:       tex(artikel1-xetex-bidi.def)
Provides:       tex(artikel2-xetex-bidi.def)
Provides:       tex(artikel3-xetex-bidi.def)
Provides:       tex(arydshln-xetex-bidi.def)
Provides:       tex(beamer-xetex-bidi.def)
Provides:       tex(beamerbaseauxtemplates-xetex-bidi.def)
Provides:       tex(beamerbaseboxes-xetex-bidi.def)
Provides:       tex(beamerbasecolor-xetex-bidi.def)
Provides:       tex(beamerbasecompatibility-xetex-bidi.def)
Provides:       tex(beamerbaseframecomponents-xetex-bidi.def)
Provides:       tex(beamerbaseframesize-xetex-bidi.def)
Provides:       tex(beamerbaselocalstructure-xetex-bidi.def)
Provides:       tex(beamerbasemisc-xetex-bidi.def)
Provides:       tex(beamerbasenavigation-xetex-bidi.def)
Provides:       tex(beamerbaseoverlay-xetex-bidi.def)
Provides:       tex(beamerinnerthemecircles-xetex-bidi.def)
Provides:       tex(beamerinnerthemedefault-xetex-bidi.def)
Provides:       tex(beamerinnerthemefocus-xetex-bidi.def)
Provides:       tex(beamerinnerthemeinmargin-xetex-bidi.def)
Provides:       tex(beamerinnerthememetropolis-xetex-bidi.def)
Provides:       tex(beamerinnerthemerectangles-xetex-bidi.def)
Provides:       tex(beamerinnerthemerounded-xetex-bidi.def)
Provides:       tex(beamerouterthemedefault-xetex-bidi.def)
Provides:       tex(beamerouterthemefocus-xetex-bidi.def)
Provides:       tex(beamerouterthemeinfolines-xetex-bidi.def)
Provides:       tex(beamerouterthememetropolis-xetex-bidi.def)
Provides:       tex(beamerouterthememiniframes-xetex-bidi.def)
Provides:       tex(beamerouterthemeshadow-xetex-bidi.def)
Provides:       tex(beamerouterthemesidebar-xetex-bidi.def)
Provides:       tex(beamerouterthemesmoothbars-xetex-bidi.def)
Provides:       tex(beamerouterthemesmoothtree-xetex-bidi.def)
Provides:       tex(beamerouterthemesplit-xetex-bidi.def)
Provides:       tex(beamerouterthemetree-xetex-bidi.def)
Provides:       tex(beamerthemeHannover-xetex-bidi.def)
Provides:       tex(beamerthemeSingapore-xetex-bidi.def)
Provides:       tex(bidi-media9.sty)
Provides:       tex(bidi-perpage.sty)
Provides:       tex(bidi.sty)
Provides:       tex(bidi.tex)
Provides:       tex(bidi2in1.sty)
Provides:       tex(bidicode.sty)
Provides:       tex(bidiftnxtra.sty)
Provides:       tex(bidimoderncv.cls)
Provides:       tex(bidipoem.sty)
Provides:       tex(biditools.sty)
Provides:       tex(biditufte-book.cls)
Provides:       tex(biditufte-handout.cls)
Provides:       tex(bidituftefloat.sty)
Provides:       tex(bidituftegeneralstructure.sty)
Provides:       tex(bidituftehyperref.sty)
Provides:       tex(bidituftesidenote.sty)
Provides:       tex(bidituftetitle.sty)
Provides:       tex(bidituftetoc.sty)
Provides:       tex(boek-xetex-bidi.def)
Provides:       tex(boek3-xetex-bidi.def)
Provides:       tex(book-xetex-bidi.def)
Provides:       tex(bookest-xetex-bidi.def)
Provides:       tex(breqn-xetex-bidi.def)
Provides:       tex(cals-xetex-bidi.def)
Provides:       tex(caption-xetex-bidi.def)
Provides:       tex(caption3-xetex-bidi.def)
Provides:       tex(color-xetex-bidi.def)
Provides:       tex(colortbl-xetex-bidi.def)
Provides:       tex(combine-xetex-bidi.def)
Provides:       tex(crop-xetex-bidi.def)
Provides:       tex(cuted-xetex-bidi.def)
Provides:       tex(cutwin-xetex-bidi.def)
Provides:       tex(cvthemebidicasual.sty)
Provides:       tex(cvthemebidiclassic.sty)
Provides:       tex(dblfnote-xetex-bidi.def)
Provides:       tex(diagbox-xetex-bidi.def)
Provides:       tex(draftwatermark-xetex-bidi.def)
Provides:       tex(empheq-xetex-bidi.def)
Provides:       tex(eso-pic-xetex-bidi.def)
Provides:       tex(extarticle-xetex-bidi.def)
Provides:       tex(extbook-xetex-bidi.def)
Provides:       tex(extletter-xetex-bidi.def)
Provides:       tex(extrafootnotefeatures-xetex-bidi.def)
Provides:       tex(extreport-xetex-bidi.def)
Provides:       tex(fancybox-xetex-bidi.def)
Provides:       tex(fancyhdr-xetex-bidi.def)
Provides:       tex(fix2col-xetex-bidi.def)
Provides:       tex(fleqn-xetex-bidi.def)
Provides:       tex(float-xetex-bidi.def)
Provides:       tex(floatrow-xetex-bidi.def)
Provides:       tex(flowfram-xetex-bidi.def)
Provides:       tex(fnpct-xetex-bidi.def)
Provides:       tex(footnote-xetex-bidi.def)
Provides:       tex(footnotebackref-xetex-bidi.def)
Provides:       tex(framed-xetex-bidi.def)
Provides:       tex(ftnright-xetex-bidi.def)
Provides:       tex(geometry-xetex-bidi.def)
Provides:       tex(graphicx-xetex-bidi.def)
Provides:       tex(hgeneric-testphase-xetex-bidi.def)
Provides:       tex(hvfloat-xetex-bidi.def)
Provides:       tex(hyperref-xetex-bidi.def)
Provides:       tex(imsproc-xetex-bidi.def)
Provides:       tex(latex-xetex-bidi.def)
Provides:       tex(leqno-xetex-bidi.def)
Provides:       tex(letter-xetex-bidi.def)
Provides:       tex(lettrine-xetex-bidi.def)
Provides:       tex(lineno-xetex-bidi.def)
Provides:       tex(listings-xetex-bidi.def)
Provides:       tex(longtable-xetex-bidi.def)
Provides:       tex(lscape-xetex-bidi.def)
Provides:       tex(mathtools-xetex-bidi.def)
Provides:       tex(mdframed-xetex-bidi.def)
Provides:       tex(media9-xetex-bidi.def)
Provides:       tex(memoir-xetex-bidi.def)
Provides:       tex(midfloat-xetex-bidi.def)
Provides:       tex(minitoc-xetex-bidi.def)
Provides:       tex(multicol-xetex-bidi.def)
Provides:       tex(multienum-xetex-bidi.def)
Provides:       tex(natbib-xetex-bidi.def)
Provides:       tex(newfloat-xetex-bidi.def)
Provides:       tex(nicematrix-xetex-bidi.def)
Provides:       tex(ntheorem-hyper-xetex-bidi.def)
Provides:       tex(ntheorem-xetex-bidi.def)
Provides:       tex(overpic-xetex-bidi.def)
Provides:       tex(pdfbase-xetex-bidi.def)
Provides:       tex(pdflscape-xetex-bidi.def)
Provides:       tex(pgfcorescopes.code-xetex-bidi.def)
Provides:       tex(pgfsys-xetex-bidi.def)
Provides:       tex(picinpar-xetex-bidi.def)
Provides:       tex(plain-xetex-bidi.def)
Provides:       tex(pstricks-xetex-bidi.def)
Provides:       tex(quotchap-xetex-bidi.def)
Provides:       tex(ragged2e-xetex-bidi.def)
Provides:       tex(rapport1-xetex-bidi.def)
Provides:       tex(rapport3-xetex-bidi.def)
Provides:       tex(refrep-xetex-bidi.def)
Provides:       tex(report-xetex-bidi.def)
Provides:       tex(rotating-xetex-bidi.def)
Provides:       tex(scrartcl-xetex-bidi.def)
Provides:       tex(scrbook-xetex-bidi.def)
Provides:       tex(scrreprt-xetex-bidi.def)
Provides:       tex(sidecap-xetex-bidi.def)
Provides:       tex(soul-xetex-bidi.def)
Provides:       tex(stabular-xetex-bidi.def)
Provides:       tex(subfigure-xetex-bidi.def)
Provides:       tex(tabls-xetex-bidi.def)
Provides:       tex(tabularx-xetex-bidi.def)
Provides:       tex(tabulary-xetex-bidi.def)
Provides:       tex(tc-xetex-xetex-bidi.def)
Provides:       tex(tcolorbox-xetex-bidi.def)
Provides:       tex(thmbox-xetex-bidi.def)
Provides:       tex(titlesec-xetex-bidi.def)
Provides:       tex(titletoc-xetex-bidi.def)
Provides:       tex(tocbasic-xetex-bidi.def)
Provides:       tex(tocbibind-xetex-bidi.def)
Provides:       tex(tocloft-xetex-bidi.def)
Provides:       tex(tocstyle-xetex-bidi.def)
Provides:       tex(todonotes-xetex-bidi.def)
Provides:       tex(wrapfig-xetex-bidi.def)
Provides:       tex(xcolor-xetex-bidi.def)
Provides:       tex(xltxtra-xetex-bidi.def)

%description
Bidirectional typesetting in plain TeX and LaTeX.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h_expected="%{source1_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

%build

%install
mkdir -p %{buildroot}%{_texmf_main}
tar -xf %{SOURCE0} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE1} -C %{buildroot}%{_texmf_main}
rm -rf %{buildroot}%{_texmf_main}/tlpkg

%files
%doc %{_texmf_main}/doc/latex/bidi/
%{_texmf_main}/tex/latex/bidi/

%changelog
%autochangelog
