%global source0_hash 27dc3087fd067d321aff3e859056773aca748510b18b8b058276f6fa57e7f16c

%global commit0 ac1703e9d7feebbf5443a986e08332b1e1c5afcf
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global foundry twitter
%global fontname twemoji
%global Fontname Twemoji

Name:           %{foundry}-%{fontname}-fonts
Version:        14.0.2
Release:        10%{?dist}
Summary:        Twitter Emoji for everyone

# In noto-emoji-fonts source
## noto-emoji code is in ASL 2.0 license
## Emoji fonts are under OFL license
### third_party color-emoji code is in BSD license
### third_party region-flags code is in Public Domain license
# In twemoji source
## Artwork is Creative Commons Attribution 4.0 International
## Non-artwork is MIT
# Automatically converted from old format: OFL and ASL 2.0 and CC-BY and MIT - review is highly recommended.
License:        LicenseRef-Callaway-OFL AND Apache-2.0 AND LicenseRef-Callaway-CC-BY AND LicenseRef-Callaway-MIT
URL:            https://twemoji.twitter.com/
Source0:        https://github.com/googlei18n/noto-emoji/archive/%{commit0}.tar.gz#/noto-emoji-%{shortcommit0}.tar.gz
Source2:        com.%{foundry}.%{fontname}.metainfo.xml
Source4:        https://github.com/%{foundry}/%{fontname}/archive/v%{version}.tar.gz#/%{fontname}-%{version}.tar.gz

Patch0:         noto-emoji-use-system-pngquant.patch
Patch1:         noto-emoji-build-all-flags.patch
Patch2:         noto-emoji-use-gm.patch

BuildArch:      noarch
BuildRequires: make
BuildRequires:  GraphicsMagick
BuildRequires:  cairo-devel
BuildRequires:  fontpackages-devel
BuildRequires:  fonttools
BuildRequires:  libappstream-glib
BuildRequires:  nototools
BuildRequires:  pngquant
BuildRequires:  python3-devel
BuildRequires:  python3dist(fonttools)
BuildRequires:  zopfli

Requires:       fontpackages-filesystem

%description
A color emoji font with a flat visual style, designed and used by Twitter.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n noto-emoji-%{commit0}
rm -rf third_party/pngquant
mv LICENSE LICENSE-BUILD

tar -xf %{SOURCE4}
sed 's/Noto Color Emoji/Twemoji/; s/NotoColorEmoji/Twemoji/; s/Copyright .* Google Inc\./Twitter, Inc and other contributors./; s/ Version .*/ %{version}/; s/.*is a trademark.*//; s/Google, Inc\./Twitter, Inc and other contributors/; s,http://www.google.com/get/noto/,https://github.com/twitter/twemoji/,; s/.*is licensed under.*/      Creative Commons Attribution 4.0 International/; s,http://scripts.sil.org/OFL,http://creativecommons.org/licenses/by/4.0/,' NotoColorEmoji.tmpl.ttx.tmpl > Twemoji.tmpl.ttx.tmpl
pushd %{fontname}-%{version}/assets/72x72/
for png in *.png; do
    mv $png emoji_u${png//-/_}
done
popd

%build
make %{?_smp_mflags} OPT_CFLAGS="$RPM_OPT_FLAGS" EMOJI=%{Fontname} EMOJI_SRC_DIR=%{fontname}-%{version}/assets/72x72 FLAGS= BODY_DIMENSIONS=76x72

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{Fontname}.ttf %{buildroot}%{_fontdir}

mkdir -p %{buildroot}%{_datadir}/metainfo
install -m 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/metainfo

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.%{foundry}.%{fontname}.metainfo.xml

%_font_pkg %{Fontname}.ttf
%license LICENSE-BUILD
%license %{fontname}-%{version}/LICENSE
%license %{fontname}-%{version}/LICENSE-GRAPHICS
%doc %{fontname}-%{version}/CONTRIBUTING.md
%doc %{fontname}-%{version}/README.md
%{_datadir}/metainfo/com.%{foundry}.%{fontname}.metainfo.xml

%changelog
%autochangelog
