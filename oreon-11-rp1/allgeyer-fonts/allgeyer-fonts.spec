%global source0_hash 539f8db123bb1cb82b1ecd26ab5d75b6932c452a27145241cc754c5db8c40998
%global fontname allgeyer
%global common_desc \
Robert Allgeyer's MusiQwik and MusiSync are a set of original True Type fonts \
that depict musical notation. Each music font may be used within a word \
processing document without the need for special music publishing software, or\
embedded in PDF files.
Name:		%{fontname}-fonts
Summary:        Musical Notation True Type Fonts
Version:	5.002
Release:        1%{?dist}
License:	LicenseRef-Callaway-OFL
Source0:        musiqwik_musisync_y6.zip
Source1:       %{fontname}.metainfo.xml
Source2:       %{fontname}-musisync.metainfo.xml
Source3:       %{fontname}-musiqwik.metainfo.xml
URL:		http://www.icogitate.com/~ergosum/fonts/musicfonts.htm
BuildArch:	noarch
Requires:	%{name}-common = %{version}-%{release}
# oreon:deps
BuildRequires:  fontpackages-devel
# /oreon:deps
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
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-musisync.metainfo.xml
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-musiqwik.metainfo.xml
%oreon_autofiles allgeyer-fonts-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles allgeyer-musisync-fonts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles allgeyer-musiqwik-fonts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n allgeyer-fonts-common -f %{oreon_filedir}/allgeyer-fonts-common.list
%files -n allgeyer-musisync-fonts -f %{oreon_filedir}/allgeyer-musisync-fonts.list
%files -n allgeyer-musiqwik-fonts -f %{oreon_filedir}/allgeyer-musiqwik-fonts.list

%changelog

%autochangelog
