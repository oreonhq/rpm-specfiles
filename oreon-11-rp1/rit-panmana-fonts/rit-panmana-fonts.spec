%global source0_hash 31d0322192f72f410b695025c7c4a7b4d1ac01773b88ba5e0c5ddbac005b94ec

# SPDX-License-Identifier: MIT
Version:    1.4.2
Release:    4%{?dist}
URL:        https://gitlab.com/rit-fonts/%{fontfamily}

%global foundry         RIT
%global fontlicense     OFL-1.1-RFN
%global fontlicenses    fonts/LICENSE.txt
%global fontdocs        fonts/*.md

%global fontfamily      panmana
%global fontsource      Panmana
%global fontsummary     Open Type body text font for Malayalam traditional script

%global fonts           fonts/otf/*.otf
%global fontconfs       %{nil}

%global fontappstreams  fonts/in.org.rachana.panmana.metainfo.xml

%global fontdescription %{expand:
Panmana is a body text font for Malayalam traditional script designed\
by KH Hussain and developed by Rachana Institute of Typography.\
The font is named after and dedicated to Prof. Panmana Ramachandran Nair.
}

# https://gitlab.com/rit-fonts/%%{fontsource}/-/jobs/artifacts/%%{version}/download?job=build-tag
Source0:    %{fontsource}-%{version}.zip

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
