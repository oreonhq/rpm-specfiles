%global source0_hash e34e729f9509cf85acc52caadf68e96db90457b7164ba45719967d53e7a20dcc

# SPDX-License-Identifier: MIT
Version:        20141121
Release:        24%{?dist}
URL:            http://www.paratype.com/public/

%global foundry         paratype
%global fontlicense     OFL-1.1-RFN
%global fontlicenses    PTSSM_OFL.txt

%global fontfamily      PT Mono
%global fontsummary     A pan-Cyrillic monospace typeface
%global fonts           *.ttf
%global fontconfs       %{SOURCE10}
%global fontconf 57-%{fontname}

%global fontdescription %{expand:\
Font PT Mono™ is the last addition to the pan-Cyrillic font superfamily \
including PT Sans and PT Serif developed for the project “Public Types \
of Russian Federation”. \
\
PT Mono was developed for the special needs — for use in forms, tables, \
work sheets etc. Equal widths of characters are very helpful in setting \
complex documents, with such font you may easily calculate size of entry \
fields, column widths in tables and so on. One of the most important area \
of use is Web sites of “electronic governments” where visitors have to fill \
different request forms. PT Mono consists of Regular and Bold styles. \
\
PT Mono was designed by Alexandra Korolkova with participation of \
Isabella Chaeva and with financial support of Google.
}

Source0:        http://www.fontstock.com/public/PTMonoOFL.zip
Source10:       %{fontpkgname}.conf
Source11:       %{fontpkgname}.metainfo.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
sed -i "s|\r||g" *.txt

%build
%fontbuild

%install
%fontinstall
# Add AppStream metadata
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontpkgname}.metainfo.xml

%check
%fontcheck

%fontfiles
%{_datadir}/appdata/%{fontpkgname}.metainfo.xml

%changelog
%autochangelog
