%global source0_hash 8703e324939ebd70d76afd350e56800f5ea2c053a040a5f5218b2a1a4300bd48
Summary:        Image Blending with Multiresolution Splines
Name: enblend
Version: 4.2
Release:        1%{?dist}
License: GPL-2.0-or-later
Source0:        http://downloads.sourceforge.net/enblend/enblend-enfuse-%{version}.tar.gz
Patch0: enblend-limits.patch
URL: http://enblend.sourceforge.net/
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  OpenEXR-devel
BuildRequires:  boost-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  gnuplot
BuildRequires:  graphviz
BuildRequires:  gsl-devel
BuildRequires:  help2man
BuildRequires:  lcms2-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-tools
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  perl(English)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl-Readonly
BuildRequires:  plotutils-devel
BuildRequires:  tex(amsmath.sty)
BuildRequires:  tex(bold-extra.sty)
BuildRequires:  tex(color.sty)
BuildRequires:  tex(enumitem.sty)
BuildRequires:  tex(fixltx2e.sty)
BuildRequires:  tex(footnote.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(hyphenat.sty)
BuildRequires:  tex(ifpdf.sty)
BuildRequires:  tex(index.sty)
BuildRequires:  tex(latexsym.sty)
BuildRequires:  tex(listings.sty)
BuildRequires:  tex(microtype.sty)
BuildRequires:  tex(nag.sty)
BuildRequires:  tex(ragged2e.sty)
BuildRequires:  tex(shorttoc.sty)
BuildRequires:  tex(suffix.sty)
BuildRequires:  tex(trivfloat.sty)
BuildRequires:  tex(url.sty)
BuildRequires:  tex(xstring.sty)
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  texlive-comment
BuildRequires:  texlive-epstopdf-bin
BuildRequires:  texlive-floatrow
BuildRequires:  texlive-latex-fonts
BuildRequires:  texlive-texloganalyser
BuildRequires:  texlive-thumbpdf
BuildRequires:  tidy
BuildRequires:  vigra-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n enblend-doc -f %{oreon_filedir}/enblend-doc.list

%changelog

%autochangelog
