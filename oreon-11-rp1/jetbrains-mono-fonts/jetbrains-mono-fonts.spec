%global source0_hash d8dab5ff24fc9e345d6c7987f2746cf8df4f870561ea89c14630b8d1729fd727

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/JetBrains/JetBrainsMono
Version:            2.304
%forgemeta

Release: 10%{?dist}
URL:     https://jetbrains.com/mono/

%global foundry           JetBrains
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.md

%global common_description %{expand:
The JetBrains Mono project publishes developer-oriented font families.

Their forms are simple and free from unnecessary details. Rendered in small
sizes, the text looks crisper. The easier the forms, the faster the eye
perceives them and the less effort the brain needs to process them.

The shape of ovals approaches that of rectangular symbols. This makes the whole
pattern of the text more clear-сut. The outer sides of ovals ensure there are
no additional obstacles for your eyes as they scan the text vertically.

Characters remain standard in width, but the height of the lowercase is
maximized. This approach keeps code lines to the length that developers expect,
and it helps improve rendering since each letter occupies more pixels.

They use a 9° italic angle; this maintains the optimal contrast to minimize
distraction and eye strain. The usual angle is about 11°–12°.}

%global fontfamily0       JetBrains Mono
%global fontsummary0      A mono-space font family containing coding ligatures
%global fontpkgheader0    %{expand:
Suggests:  font(jetbrainsmononl)
}
%global fonts0            fonts/otf/*.otf
%global fontconfngs0      %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}

The first font family published by the project, JetBrains Mono, includes coding
ligatures. They will enhance the rendering of source code but may be
problematic for other use cases.}

%global fontfamily1       JetBrains Mono NL
%global fontsummary1      A mono-space coding font family
%global fonts1            fonts/ttf/*MonoNL*.ttf
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

The second font family published by the project, JetBrains Mono NL, is general
purpose and free of coding ligatures.}

Source0:  %{forgesource}
Source10: 60-%{fontpkgname0}.xml
Source11: 58-%{fontpkgname1}.xml

%fontpkg -a

%fontmetapkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
