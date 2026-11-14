# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global tl_version 2026

Name:           texlive
Epoch:          12
Version:        %{tl_version}
Release:        1%{?dist}
Summary:        Metapackage that provides scheme-basic and collection-latexrecommended
License:        LPPL-1.3c
URL:            https://tug.org/texlive/
BuildArch:      noarch

BuildRequires:  oreon-rpm-macros

Requires:       texlive-base
Requires:       texlive-kpathsea
Recommends:     texlive-collection-latexrecommended
Recommends:     texlive-scheme-basic

%description
A metapackage to help people get the most useful parts of TeXLive.
Specifically, texlive-scheme-basic and
texlive-collection-latexrecommended. All of the applicable scheme
and collection metapackages exist and you can install them instead
(or in addition).

%prep
:

%build
:

%install
:

%files

%changelog
%autochangelog
