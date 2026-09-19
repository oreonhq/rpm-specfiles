%global source0_hash 7001f69120df1f3b0f044cf2588fc636b0ba256fa82b2bf64b37d28e8ec79b4d

# SPDX-License-Identifier: MIT
Version:    2.3.1
Release:    4%{?dist}
URL:        https://gitlab.com/rit-fonts/Sundar

%global foundry RIT
%global fontlicense OFL-1.1-RFN
%global fontlicenses fonts/LICENSE.txt
%global fontdocs fonts/*.md

%global fontfamily RIT Sundar
%global fontsource Sundar
%global fontsummary    A traditional orthography display font for Malayalam script

%global fonts fonts/otf/*.otf
%global fontconfs %{nil}

%global fontappstreams fonts/in.org.rachana.rit-sundar.metainfo.xml

%global fontdescription %{expand:
‘RIT Sundar’ is a traditional orthography display font for Malayalam script.\
This font is created, named and released in memory of Sundar (Sundar Ramanatha\
Iyer; April 23, 1953 -- November 12, 2016).
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
