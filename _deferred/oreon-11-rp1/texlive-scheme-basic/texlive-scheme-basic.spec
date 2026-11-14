# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global tl_version 2026

Name:           texlive-scheme-basic
Epoch:          12
Version:        svn54191
Release:        1%{?dist}
Summary:        basic scheme (plain and latex)

License:        LPPL-1.3c
URL:            https://tug.org/texlive/
BuildArch:      noarch

BuildRequires:  oreon-rpm-macros
BuildRequires:  texlive-base

Requires:       texlive-base
Requires:       texlive-collection-basic
Requires:       texlive-collection-latex

%description
basic scheme (plain and latex) This is the basic TeX Live scheme: it is a small
set of files sufficient to typeset plain TeX or LaTeX documents in PostScript
or PDF, using the Computer Modern fonts. This scheme corresponds to
collection-basic and collection-latex.

%prep
:

%build
:

%install
:

%files

%changelog
%autochangelog
