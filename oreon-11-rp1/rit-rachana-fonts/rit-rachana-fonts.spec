# SPDX-License-Identifier: MIT
Version:    1.5.2
Release:    5%{?dist}
URL:        https://gitlab.com/rit-fonts/%{fontsource}

%global foundry        RIT
%global fontlicense    OFL-1.1
%global fontlicenses   fonts/LICENSE.txt
%global fontdocs       fonts/*.md

%global fontfamily     RIT Rachana
%global fontsource     RIT-Rachana
%global fontsummary    OpenType font for Malayalam traditional script

%global fonts          fonts/otf/*.otf
%global fontconfs      fonts/65-0-rit-rachana-fonts.conf
%global fontappstreams fonts/in.org.rachana.rit-rachana.metainfo.xml

%global fontdescription %{expand:
RIT Rachana is OpenType font for Malayalam traditional script designed by Hussain K H.
It covers Unicode 13.0 and entire character set in 'definitive character set' of Malayalam. 
}

# https://gitlab.com/rit-fonts/%%{fontsource}/-/jobs/artifacts/%%{version}/download?job=build-tag
Source0:    %{fontsource}-%{version}.zip

%fontpkg

%prep
%setup -qc

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.2-5
- Import
