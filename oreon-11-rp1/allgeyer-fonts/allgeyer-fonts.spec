%global source0_hash 539f8db123bb1cb82b1ecd26ab5d75b6932c452a27145241cc754c5db8c40998

%global fontname allgeyer

%global common_desc \
Robert Allgeyer's MusiQwik and MusiSync are a set of original True Type fonts \
that depict musical notation. Each music font may be used within a word \
processing document without the need for special music publishing software, or\
embedded in PDF files.

Name:		%{fontname}-fonts
Summary: 	Musical Notation True Type Fonts
Version:	5.002
Release:	36%{?dist}
# Automatically converted from old format: OFL - review is highly recommended.
License:	LicenseRef-Callaway-OFL
# The source was originally downloaded from:
# http://www.icogitate.com/~ergosum/fonts/musiqwik_musisync_y6.zip
# But the website is gone now.
Source0:	musiqwik_musisync_y6.zip
Source1:       %{fontname}.metainfo.xml
Source2:       %{fontname}-musisync.metainfo.xml
Source3:       %{fontname}-musiqwik.metainfo.xml

# This website is gone. :(
URL:		http://www.icogitate.com/~ergosum/fonts/musicfonts.htm
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	%{name}-common = %{version}-%{release}

%description
%common_desc

%package common
Summary:	Common files for MusiSync and MusiQwik fonts (documentation...)
Requires:	fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other Allgeyer font packages.

%package -n %{fontname}-musisync-fonts
Summary:	A musical notation font family that provides general musical decorations
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-musisync-fonts
%common_desc

This font family provides a collection of general musical decorations.

%_font_pkg -n musisync MusiSync*.ttf
%{_datadir}/appdata/%{fontname}-musisync.metainfo.xml

%package -n %{fontname}-musiqwik-fonts
Summary:	A musical notation font family intended for writing lines of actual music
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-musiqwik-fonts
%common_desc

This font family is intended for writing lines of actual music.

%_font_pkg -n musiqwik MusiQwik*.ttf
%{_datadir}/appdata/%{fontname}-musiqwik.metainfo.xml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{name}

# correct end-of-line encoding
for i in OFL-FAQ.txt FONTLOG.txt SOURCE.txt README_MusiQwik_MusiSync.txt LICENSE_OFL.txt; do
	sed -i 's/\r//' $i
done

# Convert to UTF-8
iconv -f iso-8859-1 -t utf-8 -o README_MusiQwik_MusiSync.txt{.utf8,}
mv README_MusiQwik_MusiSync.txt{.utf8,}

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-musisync.metainfo.xml
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-musiqwik.metainfo.xml

%files common
%doc FONTLOG.txt LICENSE_OFL.txt MusiQwik_character_map.htm musiqwik_demo.png 
%doc MusiSync_character_map.htm musisync_demo.png MusiSync-README.htm OFL-FAQ.txt 
%doc README_MusiQwik_MusiSync.txt SOURCE.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
