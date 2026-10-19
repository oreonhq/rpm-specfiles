%global source20_hash a2010f343487d3f7618affe54f789f5487602331c0a8d03f49e9a7c547cf0499
%global source3_hash 03db404756bae74dfc93d5ca43157f2e84843490690df2283ecbb3dd80bec45b
%global source2_hash 6e22f60f2fd35d6c923707c5814bc3b52cb90d484f95c4911b24f8ee584c37f8
%global source1_hash 7f15174efb7ad0b64842c47fa881689f673d22ff1139693315cbbcdebf5619d5
%global source0_hash 38342a30a54deb723dbfa551e24a89ad2c92419445b8c22842f5e44038084d72
Name: daniel-wikholm-segment16-fonts
Summary:        Collection of fonts mimicking 16-segment digital displays
License: CC0-1.0
URL: https://www.wfonts.com/font/segment16a
Version: 20171229
Release:        1%{?dist}
%global foundry  Daniel Wikholm
%global fontdocs  Segment16.txt
%global fontlicense  CC0
%global fontlicenses  cc0.txt
%global fam() %{expand:Segment16%1}
%global summ() %{expand:Segment16%1, a font mimicking 16-segment digital displays}
%global fontfamily1  %{fam A}
%global fontsummary1  %{summ A}
%global fonts1  *16A*.ttf
%global fontconfs1  %{SOURCE11}
%global fontdescription1  %{expand:Segment16A, B and C are three font families, each containing a regular,
bold, italic and bold italic version, based on sixteen segment displays.
In Segment 16A, the diagonal segments extend both to the center
and the outer corners of the character, which might resemble
some, mainly older, LCD sixteen segment alphanumeric displays.}
%global fontfamily2  %{fam B}
%global fontsummary2  %{summ B}
%global fonts2  *16B*.ttf
%global fontconfs2  %{SOURCE12}
%global fontdescription2  %{expand:Segment16A, B and C are three font families, each containing a regular,
bold, italic and bold italic version, based on sixteen segment displays.
In Segment 16B, the diagonal segments extend to the center, but stop inside
the outer segments. This may resemble some newer LCD or LED displays.}
%global fontfamily3  %{fam C}
%global fontsummary3  %{summ C}
%global fonts3  *16C*.ttf
%global fontconfs3  %{SOURCE13}
%global fontdescription3  %{expand:Segment16A, B and C are three font families, each containing a regular,
bold, italic and bold italic version, based on sixteen segment displays.
In Segment 16C, the diagonal segments are not extending to the center.
This may resemble some smaller LED or VFD type displays.}
Source1: https://www.wfonts.com/download/data/2017/12/30/segment16a/segment16a.zip
Source2: https://www.wfonts.com/download/data/2017/12/30/segment16b/segment16b.zip
Source3: https://www.wfonts.com/download/data/2017/12/30/segment16c/segment16c.zip
Source11: 60-%{fontpkgname1}.xml
Source12: 60-%{fontpkgname2}.xml
Source13: 60-%{fontpkgname3}.xml
Source20: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt
BuildArch: noarch
# oreon:deps

# /oreon:deps
%description
Daniel Wikholm's Segment16 is a collection of fonts
mimicking the look of 16-segments digital displays.

%fontpkg -a

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c %{name}-%{version} -T
unzip -n %{SOURCE1}
unzip -n %{SOURCE2}
unzip -n %{SOURCE3}

cp %{SOURCE20} ./cc0.txt

%build

%fontbuild -a
%install
%fontinstall -a
%oreon_autofiles main

%check

%fontcheck -a
%fontfiles -a
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
