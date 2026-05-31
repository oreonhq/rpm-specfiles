%global source0_hash c4d10a1b665db893adc0c0aaee7ecd81b2b47c877d5cea0b40216707cbf327e4
%global source1_hash fa9ca4d13871dd122f61258a80d01751d603b4d3ee14095d65453b4e846e17d7
%global source2_hash f0ecb95e832a6adfde3e0cc7ec24b6b4e3471b3fc658125c8e57f981cb495689

# SPDX-License-Identifier: MIT
%if 0%{?rhel} > 10 || (0%{?oreon} >= 11)
%bcond build_from_src 0
%else
%bcond build_from_src 1
%endif

BuildArch: noarch

%global forgeurl    https://github.com/dejavu-fonts/dejavu-fonts
Version: 2.37
%global tag         %{lua:t=string.gsub(rpm.expand("version %{version}"), "[%p%s]+", "_");print(t)}
%forgemeta

%if %{with build_from_src}
%global source_name dejavu-fonts
BuildRequires: fontforge
BuildRequires: perl-interpreter
BuildRequires: perl(Font::TTF)
BuildRequires: unicode-ucd
BuildRequires: make
%else
%global source_name dejavu-fonts-ttf
%global forgesetupargs -n %{source_name}-%{version}
%endif

Release: 29%{?dist}
# original bitstream glyphs are Bitstream Vera
# glyphs modifications by dejavu project are Public Domain
# glyphs imported from Arev fonts are under BitStream Vera compatible license
License: Bitstream-Vera AND LicenseRef-Public-Domain
URL:     https://dejavu-fonts.github.io/

%global common_description %{expand:
The DejaVu font set is based on the “Bitstream Vera” fonts, release 1.10. Its
purpose is to provide a wider range of characters, while maintaining the
original style, using an open collaborative development process.}

%global foundry           DejaVu
%global fontlicenses      LICENSE
%global fontdocs          AUTHORS BUGS NEWS README.md

%global fontfamily1       DejaVu Sans
%global fontsummary1      DejaVu Sans, a variable-width sans-serif font family
%global fontpkgheader1    %{expand:
Obsoletes: dejavu-fonts-common < %{version}-%{release}
Obsoletes: compat-f32-dejavu-sans-fonts < %{version}-%{release}Suggests:  font(dejavusansmono)
}
%if %{with build_from_src}
%global fonts1            DejaVuSans.ttf DejaVuSans-*.ttf DejaVuSansCondensed*.ttf
%else
%global fonts1            ttf/DejaVuSans.ttf ttf/DejaVuSans-*.ttf ttf/DejaVuSansCondensed*.ttf
%endif

%global fontconfs1        fontconfig/20*-dejavu-sans.conf
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

This package consists of the DejaVu sans-serif variable-width font faces, in
their unabridged version.
}

%global fontfamily2       DejaVu Serif
%global fontsummary2      DejaVu Serif, a variable-width serif font family
%global fontpkgheader2    %{expand:
Obsoletes: dejavu-math-tex-gyre-fonts < %{version}-%{release}
Obsoletes: compat-f32-dejavu-serif-fonts < %{version}-%{release}}
%if %{with build_from_src}
%global fonts2            DejaVuSerif.ttf DejaVuSerif-*.ttf DejaVuSerifCondensed*.ttf DejaVuMathTeXGyre.ttf
%else
%global fonts2            ttf/DejaVuSerif.ttf ttf/DejaVuSerif-*.ttf ttf/DejaVuSerifCondensed*.ttf ttf/DejaVuMathTeXGyre.ttf
%endif
%global fontconfs2        fontconfig/20*-dejavu-serif.conf
%global fontconfngs2      %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

This package consists of the DejaVu serif variable-width font faces, in their
unabridged version.

It includes the Mathematics extension, that was contributed to the project by
B. Jackowski, P. Strzelczyk and P. Pianowski, on behalf of TeX user groups.}

%global fontfamily3       DejaVu Sans Mono
%global fontsummary3      DejaVu Sans Mono, a mono-space sans-serif font family
%global fontpkgheader3    %{expand:
Obsoletes: compat-f32-dejavu-sans-mono-fonts < %{version}-%{release}}
%if %{with build_from_src}
%global fonts3            DejaVuSansMono*.ttf
%else
%global fonts3            ttf/DejaVuSansMono*.ttf
%endif
%global fontconfs3        fontconfig/20*-dejavu-sans-mono.conf
%global fontconfngs3      %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

This package consists of the DejaVu sans-serif mono-space font faces, in their
unabridged version.}

%global fontfamily4       DejaVu LGC Sans
%global fontsummary4      A variable-width Latin-Greek-Cyrillic sans-serif font family
%global fontpkgheader4    %{expand:
Suggests:  font(dejavusans)
}
%if %{with build_from_src}
%global fonts4            DejaVuLGCSans.ttf DejaVuLGCSans-*.ttf DejaVuLGCSansCondensed*.ttf
%global fontconfs4        fontconfig/20*-dejavu-lgc-sans.conf
%else
%global fonts4            dejavu-lgc-fonts-ttf-2.37/ttf/DejaVuLGCSans.ttf dejavu-lgc-fonts-ttf-2.37/ttf/DejaVuLGCSans-*.ttf dejavu-lgc-fonts-ttf-2.37/ttf/DejaVuLGCSansCondensed*.ttf
%global fontconfs4        dejavu-lgc-fonts-ttf-2.37/fontconfig/20*-dejavu-lgc-sans.conf
%endif
%global fontconfngs4      %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}

This package consists of the DejaVu sans-serif variable-width font faces, with
Unicode coverage restricted to Latin, Greek and Cyrillic.}

%global fontfamily5       DejaVu LGC Serif
%global fontsummary5      A variable-width Latin-Greek-Cyrillic serif font family
%global fontpkgheader5    %{expand:
Suggests:  font(dejavuserif)
}
%if %{with build_from_src}
%global fonts5            DejaVuLGCSerif.ttf DejaVuLGCSerif-*.ttf DejaVuLGCSerifCondensed*.ttf
%global fontconfs5        fontconfig/20*-dejavu-lgc-serif.conf
%else
%global fonts5            dejavu-lgc-fonts-ttf-2.37/ttf/DejaVuLGCSerif.ttf dejavu-lgc-fonts-ttf-2.37/ttf/DejaVuLGCSerif-*.ttf dejavu-lgc-fonts-ttf-2.37/ttf/DejaVuLGCSerifCondensed*.ttf
%global fontconfs5        dejavu-lgc-fonts-ttf-2.37/fontconfig/20*-dejavu-lgc-serif.conf
%endif
%global fontconfngs5      %{SOURCE15}
%global fontdescription5  %{expand:
%{common_description}

This package consists of the DejaVu serif variable-width font faces, with
Unicode coverage restricted to Latin, Greek and Cyrillic.}

%global fontfamily6       DejaVu LGC Sans Mono
%global fontsummary6      A variable-width Latin-Greek-Cyrillic mono-space font family
%global fontpkgheader6    %{expand:
Suggests:  font(dejavusansmono)
}
%if %{with build_from_src}
%global fonts6            DejaVuLGCSansMono*.ttf
%global fontconfs6        fontconfig/20*-dejavu-lgc-sans-mono.conf
%else
%global fonts6            dejavu-lgc-fonts-ttf-2.37/ttf/DejaVuLGCSansMono*.ttf
%global fontconfs6        dejavu-lgc-fonts-ttf-2.37/fontconfig/20*-dejavu-lgc-sans-mono.conf
%endif
%global fontconfngs6      %{SOURCE16}
%global fontdescription6  %{expand:
%{common_description}

This package consists of the DejaVu sans-serif mono-space font faces, with
Unicode coverage restricted to Latin, Greek and Cyrillic.}

Source0:  %{forgeurl}/archive/version_2_37/dejavu-fonts-version_2_37.tar.gz
Source1:  %{forgeurl}/releases/download/%{tag}/dejavu-fonts-ttf-%{version}.tar.bz2
Source2:  %{forgeurl}/releases/download/%{tag}/dejavu-lgc-fonts-ttf-%{version}.tar.bz2
Source11: 57-dejavu-sans-fonts.xml
Source12: 57-dejavu-serif-fonts.xml
Source13: 57-dejavu-sans-mono-fonts.xml
Source14: 58-dejavu-lgc-sans-fonts.xml
Source15: 58-dejavu-lgc-serif-fonts.xml
Source16: 58-dejavu-lgc-sans-mono-fonts.xml
Patch0:   dejavu-fonts-ttf-urn-dtd.patch
Patch1:   dejavu-lgc-fonts-ttf-urn-dtd.patch
Patch2:   dejavu-fonts-urn-dtd.patch

Name:     dejavu-fonts
Summary:  The DejaVu font families
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg -z 1,2,3

%global lgcmetasummary All the font packages, generated from %{source_name}, Latin-Greek-Cyrillic subset
%global lgcmetadescription %{expand:
This meta-package installs all the font packages, generated from the %{source_name}
source package, in a version restricted to coverage of Latin, Greek and
Cyrillic.
}

%fontmetapkg -n dejavu-lgc-fonts-all -s lgcmetasummary -d lgcmetadescription -z 4,5,6

%package   doc
Summary:   Optional documentation files of %{source_name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{source_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
%if %{with build_from_src}
%setup -n %{name}-%{tag}
%patch -P2 -p1
%else
%setup -c -T -b1 -a2 %{forgesetupargs}
%patch -P0 -p1
%patch -P1 -p1
%endif

%build
%if %{with build_from_src}
make %{?_smp_mflags} VERSION=%{version} FC-LANG="" \
     BLOCKS=/usr/share/unicode/ucd/Blocks.txt \
     UNICODEDATA=/usr/share/unicode/ucd/UnicodeData.txt \
     BUILDDIR=.
xz -9 *.txt
%endif
%fontbuild -a

%install
%fontinstall -a

%check
%if %{with build_from_src}
make check
%endif
%fontcheck -a

%fontfiles -a

%files doc
%defattr(644, root, root, 0755)
%license LICENSE
%if %{with build_from_src}
%doc *.txt.xz
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.37-29
- Import
