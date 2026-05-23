# AucTeX includes preview-latex which allows previewing directly in the Emacs
# buffer. This makes use of preview.sty, a LaTeX class, which is also included
# with AucTex. preview-latex can either use a privately installed copy of
# preview.sty, or it can use one installed in the system texmf tree. If the
# following is set to 1, an add-on LaTeX package will be created which installs
# into the system texmf tree, and preview-latex will use that. However, TeXLive
# already includes preview.sty and so this may not be desirable -- setting the
# following value to 0 means that preview-latex/AucTeX will use a privately
# installed copy of preview.sty.
%global separate_preview 1

Summary:        Enhanced TeX modes for Emacs
Name:           emacs-auctex
Version:        13.3
Release:        7%{?dist}

# The project as a whole is GPL-3.0-or-later.  Exceptions:
# - README and doc/intro.texi are FSFAP
# - doc/auctex* and doc/preview* are GFDL-1.3-no-invariants-or-later
License:        GPL-3.0-or-later AND FSFAP AND GFDL-1.3-no-invariants-or-later
URL:            https://www.gnu.org/software/auctex/
VCS:            git:https://git.savannah.gnu.org/cgit/auctex.git
Source:         http://ftp.gnu.org/pub/gnu/auctex/auctex-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  emacs-nw
BuildRequires:  ghostscript
BuildRequires:  make
BuildRequires:  texlive-collection-latexrecommended
BuildRequires:  texlive-dvips
BuildRequires:  texinfo-tex

Requires:       dvipng
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}
Requires:       ghostscript
Requires:       texlive-dvips
Requires:       texlive-collection-latexrecommended

%if %{separate_preview}
Requires:       tex-preview = %{version}-%{release}
%endif

%description
AUCTeX is an extensible package that supports writing and formatting TeX files
for most variants of Emacs.

AUCTeX supports many different TeX macro packages, including AMS-TeX, LaTeX,
Texinfo and basic support for ConTeXt.  Documentation can be found under
/usr/share/doc, e.g. the reference card (tex-ref.pdf) and the FAQ.  The AUCTeX
manual is available in Emacs info (C-h i d m AUCTeX RET).  On the AUCTeX home
page, we provide manuals in various formats.

AUCTeX includes preview-latex support which makes LaTeX a tightly integrated
component of your editing workflow by visualizing selected source chunks (such
as single formulas or graphics) directly as images in the source buffer.

This package is for GNU Emacs.

%package doc
# The content is GFDL-1.3-no-invariants-or-later.  The remaining licenses cover
# the various fonts embedded in PDFs.
# CM: Knuth-CTAN
License:        GFDL-1.3-no-invariants-or-later AND Knuth-CTAN
Summary:        Documentation in various formats for AUCTeX

%description doc
Documentation for the AUCTeX package for emacs in various formats, including
HTML and PDF.

%if %{separate_preview}
%package -n tex-preview
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
License:        GPL-3.0-or-later AND Knuth-CTAN
Summary:        Preview style files for LaTeX
Requires:       texlive-collection-latexrecommended
Provides:       tex(preview.sty) = %{version}-%{release}
# This is the latest build we accidentally provided from texlive
Obsoletes:      texlive-preview <= 7:svn44883
Provides:       texlive-preview = 7:svn44884

%description -n tex-preview
The preview package for LaTeX allows for the processing of selected parts of a
LaTeX input file.  This package extracts indicated pieces from a source file
(typically displayed equations, figures and graphics) and typesets with their
base point at the (1in,1in) magic location, shipping out the individual pieces
on separate pages without any page markup.  You can produce either DVI or PDF
files, and options exist that will set the page size separately for each page.
In that manner, further processing (as with Ghostscript or dvipng) will be
able to work in a single pass.

The main purpose of this package is the extraction of certain environments
(most notably displayed formulas) from LaTeX sources as graphics.  This works
with DVI files postprocessed by either Dvips and Ghostscript or dvipng, but it
also works when you are using PDFTeX for generating PDF files (usually also
postprocessed by Ghostscript).

The tex-preview package is generated from the AUCTeX package for Emacs.
%endif

%prep
%autosetup -n auctex-%{version}

%conf
# Fix some encodings
iconv -f ISO-8859-1 -t UTF8 RELEASE > RELEASE.utf8 && \
touch -r RELEASE RELEASE.utf8 && \
mv RELEASE.utf8 RELEASE

%build
%if %{separate_preview}
%configure --with-emacs \
           --with-texmf-dir=%{_texmf_main} \
%else
%configure --with-emacs \
           --without-texmf-dir
%endif

%make_build

# Build documentation in various formats
pushd doc
make extradist
popd

%install
mkdir -p %{buildroot}%{_emacs_sitestartdir}
%make_install
rm -rf %{buildroot}%{_var}

# Remove /usr/share/doc/auctex directory from buildroot since we don't want doc
# files installed here
rm -rf %{buildroot}%{_docdir}/auctex

# Create these .nosearch files to keep the directories from the elisp search path
touch %{buildroot}%{_emacs_sitelispdir}/auctex/.nosearch
touch %{buildroot}%{_emacs_sitelispdir}/auctex/style/.nosearch

%files
%doc RELEASE README TODO FAQ CHANGES
%doc %{_infodir}/*.info*
%license COPYING
%exclude %{_infodir}/dir
%{_emacs_sitestartdir}/*
%dir %{_emacs_sitelispdir}/auctex
%dir %{_emacs_sitelispdir}/auctex/style
%{_emacs_sitelispdir}/auctex/*.el
%{_emacs_sitelispdir}/auctex/*.elc
%{_emacs_sitelispdir}/auctex/style/*.el
%{_emacs_sitelispdir}/auctex/style/*.elc
%{_emacs_sitelispdir}/auctex/.nosearch
%{_emacs_sitelispdir}/auctex/style/.nosearch
%{_emacs_sitelispdir}/auctex/images
%{_emacs_sitelispdir}/tex-site.el
%if !%{separate_preview}
%{_emacs_sitelispdir}/auctex/latex
%{_emacs_sitelispdir}/auctex/doc
%endif

%if %{separate_preview}
%files -n tex-preview
%license COPYING
%{_texmf_main}/tex/latex/preview
%{_texmf_main}/doc/latex/styles
%endif

%files doc
%doc doc/*.{dvi,ps,pdf}
%doc doc/html

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.3-7
- Prepare for Oreon 11 (RP1)
