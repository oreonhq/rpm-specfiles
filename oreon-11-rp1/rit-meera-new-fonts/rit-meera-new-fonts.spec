%global source0_hash none

# SPDX-License-Identifier: MIT
Version:    1.6.2
Release:    5%{?dist}
URL:        https://gitlab.com/rit-fonts/%{fontsource}

Patch1:     %{name}-add-monospace-fallback.patch

%global foundry         RIT
%global fontlicense     OFL-1.1
%global fontlicenses    fonts/LICENSE.txt
%global fontdocs        fonts/*.md

%global fontfamily      Meera New
%global fontsource      MeeraNew
%global fontsummary     OpenType sans-serif font for Malayalam traditional script

%global fonts           fonts/otf/*.otf
%global fontconfs       fonts/65-meera-new-fonts.conf
%global fontappstreams  fonts/in.org.rachana.meera-new.metainfo.xml

%global fontdescription %{expand:
MeeraNew is a sans-serif font for Malayalam traditional script designed\
by KH Hussain and developed by Rachana Institute of Typography.
}


# https://gitlab.com/rit-fonts/%%{fontsource}/-/jobs/artifacts/%%{version}/download?job=build-tag
Source0:    %{fontsource}-%{version}.zip

%fontpkg

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -qc
%patch -P1 -p1

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.2-5
- Import
