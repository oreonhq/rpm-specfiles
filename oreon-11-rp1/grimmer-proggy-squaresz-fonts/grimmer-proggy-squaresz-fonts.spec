%global source0_hash 8d48ae4d413e851bb4bf7ae1b7ec5328dcabdfc2c48d79de4e48bd4b54be09f4

%global fontname grimmer-proggy-squaresz
%global fontconf 66-%{fontname}.conf

Name: %{fontname}-fonts
Version: 1.0
Release: 20%{?dist}
License: MIT
URL: http://upperbounds.net/
Source0: http://upperbounds.net/download/ProggySquareSZ.ttf.zip
Source1: 66-grimmer-proggy-squaresz.conf
Source2: %{fontname}.metainfo.xml

BuildArch: noarch
Summary: Proggy Square with slashed zero programming font
BuildRequires: fontpackages-devel
BuildRequires: libappstream-glib
Requires: fontpackages-filesystem

%description
The proggy fonts are a set of fixed-width screen fonts that are designed for
code listings. Proggy Square Slashed Zero is identical to Proggy Square but
has a slashed zero instead of a dot.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{name}-%{version}

%build
sed -i 's/\r//' Licence.txt

%install
mkdir -p %{buildroot}/%{_fontdir}

install -m 0644 ProggySquareSZ.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

appstream-util validate-relax --nonet \
               %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc Licence.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
