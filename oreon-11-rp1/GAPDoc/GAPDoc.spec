%global source0_hash eb760738ca43a2dc5d0a891f0308303e51943745157cc27b3dd8da9a45004681
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond bootstrap 0
%bcond test 0
%global gap_pkgname GAPDoc
%global gap_makedoc makedocrel.g
Name:           %{gap_pkgname}
Version:        1.6.10
Release:        1%{?dist}
Summary:        GAP documentation tool
License:        GPL-2.0-or-later
URL:            https://www.math.rwth-aachen.de/~Frank.Luebeck/GAPDoc/
VCS:            git:https://github.com/frankluebeck/GAPDoc.git
Source0:        https://www.math.rwth-aachen.de/~Frank.Luebeck/%{name}/%{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs .. --bare -c 'LoadPackage("GAPDoc");'
BuildOption(install): *.dtd lib styles tst version
BuildOption(check): tst/testall.g
Requires:       gap-core
Requires:       libxml2
%if %{without bootstrap}
Requires:       gap-pkg-io
%endif
%if %{with test}
%endif
Provides:       gap-pkg-gapdoc = %{version}-%{release}
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-io-doc
BuildRequires:  ghostscript
BuildRequires:  libxml2
BuildRequires:  tex(amssym.tex)
BuildRequires:  tex(color.sty)
BuildRequires:  tex(english.ldf)
BuildRequires:  tex(enumitem.sty)
BuildRequires:  tex(fancyvrb.sty)
BuildRequires:  tex(geometry.sty)
BuildRequires:  tex(grfext.sty)
BuildRequires:  tex(pslatex.sty)
BuildRequires:  tex(tex)
BuildRequires:  tex-latex-bin
BuildRequires:  texlive-cm-super
BuildRequires:  texlive-ec
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-psnfss
BuildRequires:  texlive-rsfs
BuildRequires:  texlive-symbol
BuildRequires:  texlive-times
# /oreon:deps
%description
This package describes a document format for writing GAP documentation.

The idea is to define a sufficiently abstract markup language for GAP
documentation which can be (relatively easily) converted into different output
formats.  We used XML to define such a language.

This package provides:
- Utilities to use the documentation which is written in GAPDoc format with
  the GAP help system.  If you don't want to write your own (package)
  documentation you can skip to the last point of this list.
- The description of a markup language for GAP documentation (which is defined
  using the XML standard).
- Three example documents using this language: The GAPDoc documentation
  itself, a short example which demonstrates all constructs defined in the
  GAPDoc language, and a very short example explained in the introduction of
  the main documentation.
- A mechanism for distributing documentation among several files, including
  source code files.
- GAP programs (written by the first named author) which produce from
  documentation written in the GAPDoc language several document formats:
  * text format with color markup for onscreen browsing.
  * LaTeX format and from this PDF- (and DVI)-versions with hyperlinks.
  * HTML (XHTML 1.0 strict) format for reading with a Web-browser (and many
    hooks for CSS layout).
- Utility GAP programs which are used for the above but can be of independent
  interest as well:
  * Unicode strings with translations to and from other encodings
  * further utilities for manipulating strings
  * tools for dealing with BibTeX data
  * another data format BibXMLext for bibliographical data including tools to
    manipulate/translate them
  * a tool ComposedDocument for composing documents which are distributed in
    many files

%package latex
Summary:        All LaTeX dependencies for GAPDoc
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
Requires:       ghostscript
Requires:       tex(amssym.tex)
Requires:       tex(color.sty)
Requires:       tex(english.ldf)
Requires:       tex(enumitem.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(geometry.sty)
Requires:       tex(grfext.sty)
Requires:       tex(pslatex.sty)
Requires:       tex(tex)
Requires:       tex-latex-bin
Requires:       texlive-cm-super
Requires:       texlive-ec
Requires:       texlive-helvetic
Requires:       texlive-psnfss
Requires:       texlive-rsfs
Requires:       texlive-symbol
Requires:       texlive-times
Suggests:       gap-pkg-io
%description latex
This package contains all of the LaTeX dependencies for GAPDoc.  GAP proper
requires that the GAP portions of GAPDoc be installed; it refuses to start
otherwise.  However, if GAPDoc is not actively used, then dragging in all of
the LaTeX dependencies is wasteful.  Install this package to pull in all of
the necessary LaTeX dependencies for building GAP package documentation.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND GPL-1.0-or-later
Summary:        GAPDoc documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%if %{without bootstrap}
Requires:       gap-pkg-io-doc
%endif
%description doc
This package contains documentation for GAPDoc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build -a

sed -i "s|$PWD/..|%{gap_libdir}|g" doc/*.html example/*.html
%install -a
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/{3k+1,example}
%gap_copy_docs -n %{gap_upname} -d 3k+1
%gap_copy_docs -n %{gap_upname} -d example
for fil in %{gapdoc_files}; do
  for dir in 3k+1 doc example; do
    path=%{buildroot}%{gap_libdir}/pkg/%{gap_upname}/$dir/$fil
    rm -f $path
    ln -s ../styles/$fil $path
  done
done
%oreon_autofiles GAPDoc-latex usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles GAPDoc-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with test}
gap --packagesdirs .. << EOF
LoadPackage( "Browse" );
GAP_EXIT_CODE( Test( "tst/test.tst" ) );
EOF
%endif
%files -f %{oreon_filedir}/main.list
%files -n GAPDoc-latex -f %{oreon_filedir}/GAPDoc-latex.list
%files -n GAPDoc-doc -f %{oreon_filedir}/GAPDoc-doc.list

%changelog

%autochangelog
