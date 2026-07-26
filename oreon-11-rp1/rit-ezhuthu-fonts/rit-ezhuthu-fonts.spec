%global source0_hash e4b6d7bd0f427ee32be11844a1cd5e17d583724e99075f4861a15036a62f4b6d

# SPDX-License-Identifier: MIT
Version:    1.5.2
Release:    4%{?dist}
URL:        https://gitlab.com/rit-fonts/%{fontfamily}

%global foundry         RIT
%global fontlicense     OFL-1.1-RFN
%global fontlicenses    fonts/LICENSE.txt
%global fontdocs        fonts/README.md fonts/Ezhuthu-character-set.pdf

%global fontfamily      ezhuthu
%global fontsummary     Open Type script style font for Malayalam traditional script

%global fonts           fonts/otf/*.otf
%global fontconfs       %{nil}

%global fontappstreams  fonts/in.org.rachana.ezhuthu.metainfo.xml

%global fontdescription %{expand:
Ezhuthu is a handwriting style font for Malayalam traditional script designed\
by Narayana Bhattathiri and developed by Rachana Institute of Typography.
}

 
# https://gitlab.com/rit-fonts/%%{fontsource}/-/jobs/artifacts/%%{version}/download?job=build-tag
Source0:    %{fontfamily}-%{version}.zip

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
