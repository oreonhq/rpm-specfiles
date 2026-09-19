%global source0_hash fc0fecacb001543997842639bb7d0273adff791f97012ca4eb353584ea6a7a94

# SPDX-License-Identifier: MIT
Version:    1.6.2
Release:    4%{?dist}
URL:        https://gitlab.com/rit-fonts/tnjoy

%global foundry         RIT
%global fontlicense     OFL-1.1-RFN
%global fontlicenses    fonts/LICENSE.txt
%global fontdocs        fonts/README.md

%global fontfamily      TN Joy
%global fontsource      tnjoy
%global fontsummary     A traditional orthography font for Malayalam script

%global fonts           fonts/otf/*.otf
%global fontconfs       fonts/67-tn-joy-fonts.conf

%global fontappstreams  fonts/in.org.rachana.tn-joy.metainfo.xml

%global fontdescription %{expand:
TN Joy is a traditional orthography font for Malayalam script designed by\
K.H. Hussain & P.K. Ashok Kumar and developed by Rachana Institute of Typography.\
This font is named after and dedicated to the activist T.N. Joy.
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
