%global source0_hash 71c1cafbf4912524d4e304652c22f7cf2825fe1b5f877f94a551d6e15b2eb4e8

%global fontname grimmer-proggy-tinysz
%global fontconf 66-%{fontname}.conf

Name: %{fontname}-fonts
Version: 1.0
Release: 35%{?dist}
License: MIT
URL: http://upperbounds.net/
Source0: http://upperbounds.net/download/ProggyTinySZ.ttf.zip
Source1: 66-grimmer-proggy-tinysz.conf
Source2: %{fontname}.metainfo.xml

BuildArch: noarch
Summary: Proggy Tiny with slashed zero programming font
BuildRequires: fontpackages-devel
BuildRequires: libappstream-glib
Requires: fontpackages-filesystem

%description
The proggy fonts are a set of fixed-width screen fonts that are designed for
code listings. Proggy Tiny Slashed Zero is identical to Proggy Tiny but has a
slashed zero instead of a dot.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{name}-%{version}

%build
sed -i 's/\r//' Licence.txt

%install
mkdir -p %{buildroot}/%{_fontdir}

install -m 0644 ProggyTinySZ.ttf %{buildroot}%{_fontdir}

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
