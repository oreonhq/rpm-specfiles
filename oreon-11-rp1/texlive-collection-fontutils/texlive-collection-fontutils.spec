%global source0_hash 09aa821181ce68c6a8380fede39029e12c9b6df58976eccca6cdf0f567eb7354

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-fontutils
Epoch:          12
Version:        svn61207
Release:        4%{?dist}
Summary:        Graphics and font utilities

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-fontutils.r61207.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvipsconfig.r13293.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-accfonts
Requires:       texlive-afm2pl
Requires:       texlive-albatross
Requires:       texlive-collection-basic
Requires:       texlive-dosepsbin
Requires:       texlive-dvipsconfig
Requires:       texlive-epstopdf
Requires:       texlive-fontinst
Requires:       texlive-fontools
Requires:       texlive-fontware
Requires:       texlive-lcdftypetools
Requires:       texlive-luafindfont
Requires:       texlive-mf2pt1
Requires:       texlive-ps2eps
Requires:       texlive-ps2pk
Requires:       psutils
Requires:       t1utils
Requires:       texlive-ttfutils

%description
Programs for conversion between font formats, testing fonts, virtual fonts, .gf
and .pk manipulation, mft, fontinst, etc. Manipulating OpenType, TrueType, Type
1,and for manipulation of PostScript and other image formats.

%package -n texlive-dvipsconfig
Summary:        Collection of dvips PostScript headers
Version:        svn13293
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-dvipsconfig
This is a collection of dvips PostScript header and dvips config files. They
control certain features of the printer, including: A4, A3, usletter, simplex,
duplex / long edge, duplex / short edge, screen frequencies of images,
black/white invers, select transparency / paper for tektronix 550/560, manual
feeder, envelope feeder, and tray 1, 2 and 3, and printing a PostScript grid
underneath the page material--very useful for measuring and eliminating paper
feed errors!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Extract license files
tar -xf %{SOURCE1}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_texmf_main}

tar -xf %{SOURCE2} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-dvipsconfig
%license gpl2.txt
%{_texmf_main}/dvips/dvipsconfig/

%changelog
%autochangelog
