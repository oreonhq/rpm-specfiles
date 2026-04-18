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


# Same blob as Fedora f43 SRPM (lookaside). Upstream has no stable HTTP for this snapshot.
Source0:  https://src.fedoraproject.org/lookaside/pkgs/rpms/google-droid-fonts/google-droid-fonts-%{version}.tar.xz/sha512/4ab5462819fbef043e4cc7df565a11da21e0f6afaee002576d52decbf43449053919a0787a1a06ce7187d5308afcf3c044cedf87ed2a6bb28ce18d981928d346/google-droid-fonts-%{version}.tar.xz
# Brutal script used to pull sources from upstream git
# Needs at least 2 Gib of space in /var/tmp
Source1:  getdroid.sh
# Literal names so dist-git source checks match committed files (macros in Source filenames break that step)
Source11: 66-google-droid-sans-fonts.conf
Source12:  60-google-droid-sans-mono-fonts.conf
Source13:  66-google-droid-serif-fonts.conf
Source14: 69-%{googledroid}-arabic-kufi-fonts.conf
Source15: 69-%{googledroid}-arabic-naskh-fonts.conf
Source16: 69-%{googledroidsans}-armenian-fonts.conf
Source17: 69-%{googledroidsans}-devanagari-fonts.conf
Source18: 69-%{googledroidsans}-ethiopic-fonts.conf
Source19: 69-%{googledroidsans}-georgian-fonts.conf
Source20: 69-%{googledroidsans}-hebrew-fonts.conf
Source21: 69-%{googledroidsans}-japanese-fonts.conf
Source22: 69-%{googledroidsans}-tamil-fonts.conf
Source23: 69-%{googledroidsans}-thai-fonts.conf
Source24: 69-%{googledroidsans}-fallback-fonts.conf

Name:     google-droid-fonts
Summary:  A set of general-purpose font families released by Google as part of Android
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%prep
%setup -q -n %{archivename}

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20200215-24
- Prepare for Oreon 11 (RP1)
