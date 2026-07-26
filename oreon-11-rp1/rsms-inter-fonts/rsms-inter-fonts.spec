%global source0_hash none

Version:        4.1
Release:        3%{?dist}
URL:            https://rsms.me/inter/

%global common_description %{expand:Inter is a typeface specially designed for user interfaces with focus on high
legibility of small-to-medium sized text on computer screens.

The family features a tall x-height to aid in readability of mixed-case and
lower-case text. Several OpenType features are provided as well, like contextual
alternates that adjusts punctuation depending on the shape of surrounding
glyphs, slashed zero for when you need to disambiguate "0" from "o", tabular
numbers, etc.}

%global foundry rsms
%global fontlicense OFL-1.1
%global fontlicenses LICENSE.txt
%global fontdocsex %{fontlicenses}

%global fontfamily0 Inter
%global fontsummary0 The Inter font family
%global fonts0 extras/ttf/*.ttf
%global fontconfs0 %{SOURCE10}
%global fontdescription0 %{expand:%{common_description}

This package contains the non-variable font version of the Inter font.}

%global fontfamily1 Inter-VF
%global fontsummary1 The Inter font family (variable)
%global fonts1 Inter*.ttf
%global fontconfs1 %{SOURCE11}
%global fontdescription1 %{expand:%{common_description}

This package contains the variable font version of the Inter font.}

Source0:        https://github.com/rsms/inter/releases/download/v%{version}/inter-%{version}.zip
Source10:       63-rsms-inter.conf
Source11:       63-rsms-inter-vf.conf

%fontpkg -a

%prep
%autosetup -c

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
