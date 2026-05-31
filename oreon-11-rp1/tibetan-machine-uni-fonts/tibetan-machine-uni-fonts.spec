%global source0_hash none

%global	fontname	tibetan-machine-uni
%global zipname		TibetanMachineUnicodeFont

Name:		%{fontname}-fonts
Version:	1.901
Release:	37%{?dist}
Summary:	Tibetan Machine Uni font for Tibetan, Dzongkha and Ladakhi

# .ttf file now states GPLv3+ with fonts exceptions
License:	GPL-3.0-or-later WITH Font-exception-2.0
URL:		http://www.thlib.org/tools/#wiki=/access/wiki/site/26a34146-33a6-48ce-001e-f16ce7908a6a/tibetan%20machine%20uni.html
Source0:        https://collab.itc.virginia.edu/access/content/group/26a34146-33a6-48ce-001e-f16ce7908a6a/Tibetan%20fonts/Tibetan%20Unicode%20Fonts/%{zipname}.zip
Source1:        %{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	dos2unix
Requires:	fontpackages-filesystem

%description
Tibetan Machine Uni is an TrueType OpenType, Unicode font released by THDL
project. The font supports Tibetan, Dzongkha and Ladakhi in dbu-can script
with full support for the Sanskrit combinations found in chos skad text.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{zipname}

%build
# Empty build section

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

dos2unix -o ReadMe.txt

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg *.ttf
%doc gpl.txt ReadMe.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.901-37
- Import
