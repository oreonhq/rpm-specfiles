%global source0_hash c064b19e72da23a26ef18f336bcfed2cb2f5243cc055f1cfa0b35afc7e850e18

# Packaging template: multi-family fonts packaging.
#
# SPDX-License-Identifier: MIT
#
# This template documents spec declarations, used when packaging multiple font
# families, from a single dedicated source archive. The source rpm is named
# after the first (main) font family). Look up “fonts-3-sub” when the source
# rpm needs to be named some other way.
#
# It is part of the following set of packaging templates:
# “fonts-0-simple”: basic single-family fonts packaging
# “fonts-1-full”:   less common patterns for single-family fonts packaging
# “fonts-2-multi”:  multi-family fonts packaging
# “fonts-3-sub”:    packaging fonts, released as part of something else
#
Version: 20230918
Release: 1%{?dist}
URL:     http://vlgothic.dicey.org

# The following declarations will be aliased to [variable]0 and reused for all
# generated *-fonts packages unless overriden by a specific [variable][number]
# declaration.
%global foundry           VL  
%global fontlicense       mplus AND BSD-3-Clause
%global fontlicenses      LICENSE_J.mplus LICENSE_E.mplus LICENSE LICENSE.en
%global fontdocs          README README_J.mplus README.sazanami README_E.mplus
%global fontdocsex        %{fontlicenses}

# A text block that can be reused as part of the description of each generated
# subpackage.
%global common_description %{expand:
VLGothic provides Japanese TrueType fonts from the Vine Linux project.
Most of the glyphs are taken from the M+ and Sazanami Gothic fonts,
but some have also been improved by the project.
}

# Declaration for the subpackage containing the first font family. Also used as
# source rpm info. All the [variable]0 declarations are equivalent and aliased
# to [variable].

%global fontfamily0       VL Gothic
%global fontsummary0      Japanese TrueType font
%global fontpkgheader0    %{expand:
Obsoletes:  vlgothic-fonts < %{version}-%{release}
Provides:   vlgothic-fonts = %{version}-%{release}
}
%global fonts0            VL-Gothic-Regular.ttf
%global fontsex0          %{nil}
%global fontconfs0        %{SOURCE10}
%global fontconfsex0      %{nil}
%global fontdescription0  %{expand:
%{common_description}

This package provides the monospace VLGothic font.
}

%global fontfamily1       VL PGothic
%global fontsummary1      Proportional Japanese TrueType font
%global fontpkgheader1    %{expand:
Obsoletes:  vlgothic-p-fonts < %{version}-%{release}
Provides:   vlgothic-p-fonts = %{version}-%{release}
}
%global fonts1            VL-PGothic-Regular.ttf
%global fontsex1          %{nil}
%global fontconfs1        %{SOURCE11}
%global fontconfsex1      %{nil}
%global fontdescription1  %{expand:
%{common_description}

This package provides the VLGothic font with proportional glyphs for some
non-Japanese characters.
}

Source0:  https://vlgothic.dicey.org/releases/VLGothic-%{version}.tar.xz
Source10: 65-3-%{fontpkgname0}.conf
Source11: 65-2-%{fontpkgname1}.conf

# “fontpkg” will generate the font subpackage headers corresponding to the
# elements declared above.
# “fontpkg” accepts the following selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block.
%fontpkg -a

# “fontmetapkg” will generate a font meta(sub)package header for all the font
# subpackages generated in this spec. Optional arguments:
# – “-n [name]”      use [name] as metapackage name
# – “-s [variable]”  use the content of [variable] as metapackage summary
# – “-d [variable]”  use the content of [variable] as metapackage description
# – “-z [numbers]”   restrict metapackaging to [numbers] comma-separated list
#                    of font package suffixes
%fontmetapkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n VLGothic
iconv -f EUC-JP -t UTF-8 -o README.sazanami.tmp README.sazanami
touch -r README.sazanami README.sazanami.tmp
mv README.sazanami.tmp README.sazanami

%build
# “fontbuild” accepts the usual selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block.
%fontbuild -a

%install
# “fontinstall” accepts the usual selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block.
%fontinstall -a

%check
# “fontcheck” accepts the usual selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block.
%fontcheck -a

# “fontfiles” accepts the usual selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block
%fontfiles -a

%changelog
%autochangelog
