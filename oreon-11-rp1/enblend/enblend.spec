%global source0_hash 8703e324939ebd70d76afd350e56800f5ea2c053a040a5f5218b2a1a4300bd48

Summary: Image Blending with Multiresolution Splines
Name: enblend
Version: 4.2
Release: 35%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source0: http://downloads.sourceforge.net/enblend/enblend-enfuse-%{version}.tar.gz
Patch0: enblend-limits.patch
URL: http://enblend.sourceforge.net/
BuildRequires:  gcc-c++
BuildRequires: libtiff-devel boost-devel lcms2-devel plotutils-devel
BuildRequires: freeglut-devel glew-devel libjpeg-devel libpng-devel OpenEXR-devel
BuildRequires: libXmu-devel libXi-devel
BuildRequires: vigra-devel >= 1.9.0
BuildRequires: gsl-devel

# commenting-out 'hevea' disables pdf documentation
#BuildRequires: hevea
BuildRequires: gnuplot graphviz tidy help2man ImageMagick librsvg2-tools texinfo texinfo-tex
BuildRequires: tex(amsmath.sty) tex(bold-extra.sty) tex(color.sty) tex(enumitem.sty) tex(fixltx2e.sty)
BuildRequires: tex(footnote.sty) tex(graphicx.sty) tex(hyperref.sty) tex(hyphenat.sty) tex(ifpdf.sty)
BuildRequires: tex(index.sty) tex(latexsym.sty) tex(listings.sty) tex(microtype.sty) tex(nag.sty)
BuildRequires: tex(ragged2e.sty) tex(shorttoc.sty) tex(suffix.sty) tex(trivfloat.sty) tex(url.sty) tex(xstring.sty)
BuildRequires: texlive-floatrow texlive-comment texlive-epstopdf-bin texlive-latex-fonts texlive-thumbpdf texlive-texloganalyser
BuildRequires: perl-Readonly
BuildRequires: perl(English) perl(Sys::Hostname) perl(File::Basename) perl(Getopt::Long) perl(IO::File)
BuildRequires: make

%description
Enblend is a tool for compositing images, given a set of images that overlap in
some irregular way, Enblend overlays them in such a way that the seam between
the images is invisible, or at least very difficult to see.  Enfuse combines
multiple images of the same subject into a single image with good exposure and
good focus.  Enblend and Enfuse do not line up the images for you, use a tool
like Hugin to do that.

%package doc
Summary: Usage Documentation for enblend and enfuse
License: GFDL

%description doc
PDF usage documentation for the enblend and enfuse command line tools

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n enblend-enfuse-%{version}
%patch -P0 -p1

%build
export CPPFLAGS="-std=gnu++14 -I/usr/include/gperftools"
%configure --with-boost-filesystem --with-tcmalloc --enable-opencl --enable-openmp
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS COPYING NEWS README

%{_bindir}/enblend
%{_bindir}/enfuse
%{_mandir}/man1/*

%files doc
%doc COPYING
#doc COPYING doc/enblend.pdf doc/enfuse.pdf
#{_docdir}/enblend-enfuse/examples/enfuse/*

%changelog
%autochangelog
