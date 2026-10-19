%global source1_hash 3fc019a3c0fc4c106acd73d98797d45910bb1735b14885c5855d5353fa33f56d
%global source0_hash db024b5facab56ff342d2effecf8f780ce1c7f41be951679df71b204f0a36e51
Version: 0.0.1
Release:        1%{?dist}
URL:     https://github.com/yuru7/mint-mono/
%global foundry           TWR
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE
%global fontdocs          %{nil}
%global fontdocsex        %{fontlicenses}
%global common_description %{expand:
Mint Mono is designed for programming which is based on Intel One Mono
and Circle M+.
}
%global fontfamily0       Mint Mono
%global fontsummary0      Mint Mono, monospace typeface TrueType font
%global fontpkgheader0    %{expand:
}
%global fonts0            MintMono/MintMono-Regular.ttf MintMono/MintMono-Italic.ttf MintMono/MintMono-BoldItalic.ttf MintMono/MintMono-Bold.ttf
%global fontsex0          %{nil}
%global fontconfs0        %{SOURCE11}
%global fontconfsex0      %{nil}
%global fontdescription0  %{expand:
%{common_description}
This package contains Mint Mono which is a monospace typeface of TrueType font.
}
%global fontfamily1       Mint Mono 35
%global fontsummary1      Mint Mono 35, monospace typeface TrueType font
%global fontpkgheader1    %{expand:
}
%global fonts1            MintMono35/MintMono35-Regular.ttf MintMono35/MintMono35-Italic.ttf MintMono35/MintMono35-BoldItalic.ttf MintMono35/MintMono35-Bold.ttf
%global fontsex1          %{nil}
%global fontconfs1        %{SOURCE12}
%global fontconfsex1      %{nil}
%global fontdescription1  %{expand:
%{common_description}
This package contains Mint Mono 35 which is a monospace typeface of TrueType font.
}
Source0:        https://github.com/yuru7/mint-mono/releases/download/v%{version}/MintMono_v%{version}.zip
Source1:  https://raw.githubusercontent.com/yuru7/mint-mono/refs/heads/main/LICENSE
Source11: 69-twr-mint-mono-fonts.conf
Source12: 69-twr-mint-mono-35-fonts.conf
%fontpkg -a
%fontmetapkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

%setup -q -n MintMono_v0.0.1
cp %{SOURCE1} .

%build

%fontbuild -a
%install
%fontinstall -a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%fontcheck -a
%fontfiles -a
%files -f %{oreon_filedir}/main.list
%files -n google-go-fonts -f %{oreon_filedir}/google-go-fonts.list
%files -n adf-gillius-2-fonts -f %{oreon_filedir}/adf-gillius-2-fonts.list
%files -n google-go-smallcaps-fonts -f %{oreon_filedir}/google-go-smallcaps-fonts.list
%files -n lomt-mscorebc-fonts -f %{oreon_filedir}/lomt-mscorebc-fonts.list
%files -n lomt-mscoretabulature-fonts -f %{oreon_filedir}/lomt-mscoretabulature-fonts.list
%files -n lomt-musejazz-fonts -f %{oreon_filedir}/lomt-musejazz-fonts.list
%files -n lomt-musejazz-text-fonts -f %{oreon_filedir}/lomt-musejazz-text-fonts.list
%files -n lomt-gootville-fonts -f %{oreon_filedir}/lomt-gootville-fonts.list
%files -n lomt-gootville-text-fonts -f %{oreon_filedir}/lomt-gootville-text-fonts.list
%files -n adf-gillius-fonts-all -f %{oreon_filedir}/adf-gillius-fonts-all.list

%changelog

%autochangelog
