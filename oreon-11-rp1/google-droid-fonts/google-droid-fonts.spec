%global source0_hash 54a78bdf2986fcfa3d2c234fa48d6d4c535ef5fe803906df708df11f570f2ce2

# SPDX-License-Identifier: MIT
BuildArch: noarch

# No sane versionning upstream, use git clone timestamp
Version: 20200215
Release: 24%{?dist}
License: Apache-2.0
URL:     https://android.googlesource.com/

%global source_name       google-droid-fonts

%global foundry           Google
%global fontlicenses      NOTICE
%global fontdocs          *.txt

%global common_description %{expand:
The Droid font family was designed in the fall of 2006 by Ascender’s Steve
Matteson, as a commission from Google to create a set of system fonts for its
Android platform. The goal was to provide optimal quality and comfort on a
mobile handset when rendered in application menus, web browsers and for other
screen text.

The family was later extended in collaboration with other designers such as
Pascal Zoghbi of 29ArabicLetters.}

%global fontfamily1       Droid Sans
%global fontsummary1      Droid Sans, a humanist sans-serif font family
%global fontpkgheader1   %{expand:
Obsoletes: google-droid-kufi-fonts < %{version}-%{release}
Suggests: font(notosans)
}
%global fonts1            DroidSans*ttf DroidKufi*ttf
%global fontsex1          DroidSansMono*ttf DroidSansFallback.ttf DroidSansHebrew.ttf
%global fontconfs1      %{SOURCE11} %{SOURCE14} %{SOURCE16} %{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24}
%global fontdescription1  %{expand:
%{common_description}

Droid Sans is a humanist sans serif font family designed for user interfaces and electronic communication.

The Arabic block was initially designed by Steve Matteson of Ascender under the
Droid Kufi name, with consulting by Pascal Zoghbi of 29ArabicLetters to
finalize the font family.}

%global fontfamily2       Droid Sans Mono
%global fontsummary2      Droid Sans Mono, a humanist mono-space sans-serif font family
%global fontpkgheader2    %{expand:
Suggests: font(notosansmono)
}
%global fonts2            DroidSansMono*ttf
%global fontconfs2      %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

Droid Sans Mono is a humanist mono-space sans serif font family designed for
user interfaces and electronic communication.}

%global fontfamily3       Droid Serif
%global fontsummary3      Droid Serif, a contemporary serif font family
%global fontpkgheader3    %{expand:
Suggests: font(notoserif)
}
%global fonts3            DroidSerif*ttf DroidNaskh*ttf
%global fontsex3          DroidNaskhUI-Regular.ttf DroidNaskh-Regular-Shift.ttf
%global fontconfs3      %{SOURCE13} %{SOURCE15}
%global fontdescription3  %{expand:
%{common_description}

Droid Serif is a contemporary serif typeface family designed for comfortable
reading on screen. Droid Serif is slightly condensed to maximize the amount of
text displayed on small screens. Vertical stress and open forms contribute to
its readability while its proportion and overall design complement its
companion Droid Sans.

The Arabic block was designed by Pascal Zoghbi of 29ArabicLetters under the
Droid Naskh name.}

%global archivename google-droid-fonts-%{version}
%global googledroid google-droid
%global googledroidsans %{googledroid}-sans


Source0:  %{archivename}.tar.xz
# Brutal script used to pull sources from upstream git
# Needs at least 2 Gib of space in /var/tmp
Source1:  getdroid.sh
Source11: 66-google-droid-sans-fonts.conf
Source12: 60-google-droid-sans-mono-fonts.conf
Source13: 66-google-droid-serif-fonts.conf
Source14: 69-google-droid-arabic-kufi-fonts.conf
Source15: 69-google-droid-arabic-naskh-fonts.conf
Source16: 69-google-droid-sans-armenian-fonts.conf
Source17: 69-google-droid-sans-devanagari-fonts.conf
Source18: 69-google-droid-sans-ethiopic-fonts.conf
Source19: 69-google-droid-sans-georgian-fonts.conf
Source20: 69-google-droid-sans-hebrew-fonts.conf
Source21: 69-google-droid-sans-japanese-fonts.conf
Source22: 69-google-droid-sans-tamil-fonts.conf
Source23: 69-google-droid-sans-thai-fonts.conf
Source24: 69-google-droid-sans-fallback-fonts.conf

Name:     google-droid-fonts
Summary:  A set of general-purpose font families released by Google as part of Android
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{archivename}

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20200215-24
- Import
