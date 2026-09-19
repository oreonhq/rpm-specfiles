%global source0_hash 66cacd03dda6b25d447f93a97c3ea5af281f294b6a6b69591ba2819c49816a80

# SPDX-License-Identifier: MIT
Version: 3.2.2
Release: 4%{?dist}
URL:     https://gitlab.com/rit-fonts/rit-%{fontfamily}

%global foundry         RIT
%global fontlicense     OFL-1.1-RFN AND MIT
%global fontlicenses    fonts/LICENSE.txt
%global fontdocs        fonts/*.md

%global fontfamily      keraleeyam
%global fontsummary     Display style traditional script font for Malayalam

%global fonts           fonts/otf/*.otf
%global fontconfs       fonts/75-rit-keraleeyam-fonts.conf

%global fontappstreams  fonts/in.org.rachana.%{fontfamily}.metainfo.xml

%global fontdescription   %{expand:
Keraleeyam is a thick sans-serif display style font in condensed form.
It is widely used for designing book covers and titles.
Conjuncts, especially vertical conjuncts are designed for better balance
among upper and lower characters.
}

Source0:  %{url}/-/jobs/artifacts/%{version}/download?job=build-tag#/rit-%{fontfamily}-%{version}.zip

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
