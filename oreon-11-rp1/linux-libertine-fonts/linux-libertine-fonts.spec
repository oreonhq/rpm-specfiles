%global source0_hash 3eb84d13e59d390a3f0b15f93bbb590de693dd5f29c4e8083317dbbadf6fb985

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
%global posttag 2012_07_02

Version: 5.3.0
Release: 33.%{posttag}%{?dist}
URL:     http://linuxlibertine.sf.net
BuildRequires: fonts-rpm-macros >= 1:2.0.5-9

# The following declarations will be aliased to [variable]0 and reused for all
# generated *-fonts packages unless overriden by a specific [variable][number]
# declaration.
%global foundry           linux-libertine
%global fontlicense       GPL-2.0-or-later WITH Font-exception-2.0 OR OFL-1.1
%global fontlicenses      OFL-1.1.txt GPL.txt LICENCE.txt
%global fontdocs          ToDo.txt Readme-TEX.txt README ChangeLog.txt Bugs.txt
%global fontdocsex        %{fontlicenses}

# A text block that can be reused as part of the description of each generated
# subpackage.
%global common_description %{expand:
The Linux Libertine Open Fonts are a TrueType font family for practical use in documents.  They were created to provide a free alternative to proprietary standard fonts.
}

# Declaration for the subpackage containing the first font family. Also used as
# source rpm info. All the [variable]0 declarations are equivalent and aliased
# to [variable].

%global fontfamily0       Linux Libertine
%global fontsummary0      Linux Libertine Open Fonts
%global fontpkgheader0    %{expand:
Obsoletes: linux-libertine-fonts-common < 5.3.0-25
Provides: linux-libertine-fonts-common = %{version}-%{release}
}
%global fonts0            LinLibertine_RZ.otf LinLibertine_RZI.otf LinLibertine_R.otf LinLibertine_RI.otf LinLibertine_RB.otf LinLibertine_RBI.otf LinLibertine_DR.otf LinLibertine_I.otf
%global fontsex0          %{nil}
%global fontconfs0        %{SOURCE10} %{SOURCE13}
%global fontconfsex0      %{nil}
%global fontdescription0  %{expand:
%{common_description}
This package contains Serif fonts.
}

%global fontfamily1       Linux Biolinum
%global fontsummary1      Sans-serif fonts from Linux Libertine Open Fonts
%global fontpkgheader1    %{expand:
Obsoletes: linux-libertine-fonts-common < 5.3.0-25
Provides: linux-libertine-fonts-common = %{version}-%{release}
}
%global fonts1            LinBiolinum_R.otf LinBiolinum_RI.otf LinBiolinum_RB.otf LinBiolinum_K.otf
%global fontsex1          %{nil}
%global fontconfs1        %{SOURCE11}
%global fontconfsex1      %{nil}
%global fontdescription1  %{expand:
%{common_description}
This package contains Sans fonts.
}

%global fontfamily2       Linux Libertine Mono
%global fontsummary2      Monospace font from Linux Libertine Open Fonts
%global fontpkgheader2    %{expand:
Obsoletes: linux-libertine-fonts < 5.3.0-25
Obsoletes: linux-libertine-fonts-common < 5.3.0-25
Provides: linux-libertine-fonts-common = %{version}-%{release}
}
%global fonts2            LinLibertine_M.otf
%global fontsex2          %{nil}
%global fontconfs2        %{SOURCE12}
%global fontconfsex2      %{nil}
%global fontdescription2  %{expand:
%{common_description}
This package contains Monospace font.
}

Source0:  http://download.sourceforge.net/sourceforge/linuxlibertine/LinLibertineOTF_%{version}_%{posttag}.tgz
Source10: 60-linux-libertine-fonts.conf
Source11: 61-linux-libertine-biolinum-fonts.conf
Source12: 61-linux-libertine-mono-fonts.conf
Source13: 29-linux-libertine-fonts-metrics-alias.conf

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

%setup -q -c

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
