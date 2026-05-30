%global source0_hash a58c57d95242a17cfe3adf40c764b15b1b1354ed689b684315c093e5b531538f
%global source4_hash c9c6be08ba13ea176464a2a872c386418ee8366ff1d7c6965536800d15de001a

# SPDX-License-Identifier: MIT

%global commit0 b3e3051a088047d19fd4d49b1c3ac42fb8c3aaf8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global fontname google-noto-emoji

# The font build process need to download the code from the internet,
# skip to build the font.
%global buildfont 0

BuildRequires:  gcc
BuildRequires:  fontpackages-devel
%if %buildfont
BuildRequires:  fonttools
BuildRequires:  python3-fonttools
BuildRequires:  nototools
BuildRequires:  python3-nototools
BuildRequires:  python3-devel
BuildRequires:  GraphicsMagick
BuildRequires:  pngquant
BuildRequires:  zopfli
BuildRequires:  cairo-devel
%endif
BuildRequires:  make

Version: 20250623
Release: 4%{?dist}
URL:     https://github.com/googlefonts/noto-emoji

%global foundry           Google
# In noto-emoji-fonts source
## noto-emoji code is in ASL 2.0 license
## Emoji fonts are under OFL license
### third_party color-emoji code is in BSD license
### third_party region-flags code is in Public Domain license
# In nototools source
## nototools code is in ASL 2.0 license
### third_party ucd code is in Unicode license
%global fontlicense       OFL-1.1 AND Apache-2.0
%global fontlicenses      LICENSE OFL.txt
%global fontdocs          AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md README.txt

%global fontfamily0       Noto Emoji
%global fontsummary0      Google “Noto Emoji” Black-and-White emoji font
%global fonts0            NotoEmoji-Regular.ttf
%global fontdescription0  %{expand:
This package provides the Google “Noto Emoji” Black-and-White emoji font.
}

%global fontfamily1       Noto Color Emoji
%global fontsummary1      Google “Noto Color Emoji” colored emoji font
%global fontpkgheader1    %{expand:
Obsoletes:      google-noto-emoji-color-fonts < 20220916-6
Provides:       google-noto-emoji-color-fonts = %{version}-%{release}
}
%global fonts1            Noto-COLRv1.ttf
%global fontdescription1  %{expand:
This package provides the Google “Noto Color Emoji” colored emoji font.
}

%global fontfamily2       Noto Emoji VF
%global fontsummary2      Google “Noto Emoji” Black-and-White emoji variable font
%global fonts2            NotoEmoji-VariableFont_wght.ttf
%global fontdescription2  %{expand:
This package provides the Google “Noto Emoji” Black-and-White emoji variable font.
}

Source0:        https://github.com/googlefonts/noto-emoji/archive/%{commit0}.tar.gz#/noto-emoji-%{shortcommit0}.tar.gz
Source4:        Noto_Emoji.zip


%fontpkg -a


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -a 4 -n noto-emoji-%{commit0}

rm -rf third_party/pngquant

cp -p static/NotoEmoji-Regular.ttf .

%build

%if %buildfont
# Work around UTF-8
export LANG=C.UTF-8

%make_build OPT_CFLAGS="$RPM_OPT_FLAGS" BYPASS_SEQUENCE_CHECK='True'
%else
cp -p fonts/Noto-COLRv1.ttf .
%endif

%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20250623-4
- Import
