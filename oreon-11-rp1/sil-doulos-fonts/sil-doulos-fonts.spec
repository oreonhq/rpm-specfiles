%global source0_hash a7ad76326c126b2748297b987a634a56f7e42cd45bc3ff2c90a7909cbb164223

%define fontname sil-doulos
%define archivename DoulosSIL
%define docversion 4.100

Name:           %{fontname}-fonts
Version:        6.200
Release:        6%{?dist}
Summary:        Doulos SIL fonts

License:        OFL-1.1
URL:            http://scripts.sil.org/DoulosSILFont
Source0:        https://software.sil.org/downloads/r/doulos/%{archivename}-%{version}.zip
Source1:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

# Obsoleting and providing the old RPM name
Obsoletes:      doulos-fonts < 4.104-2

%description
Doulos SIL provides glyphs for a wide range of Latin and Cyrillic
characters. Doulos's design is similar to the design of the Times-like
fonts, but only has a single regular face. It is intended for use alongside
other Times-like fonts where a range of styles (italic, bold) are not
needed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{archivename}-%{version}
sed -i 's/\r$//' *.txt

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg *.ttf
%doc FONTLOG.txt OFL-FAQ.txt README.txt
%doc documentation/pdf/
%license OFL.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
