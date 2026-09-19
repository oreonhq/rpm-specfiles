%global source0_hash none

%global tl_version 2025

Name:           texlive-scheme-infraonly
Epoch:          12
Version:        svn54191
Release:        2%{?dist}
Summary:        infrastructure-only scheme (no TeX at all)

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-texlive.infra
Requires:       texlive-kpathsea
Requires:       texlive-hyphen-base
Requires:       texlive-texlive-scripts

%description
infrastructure-only scheme (no TeX at all) This is the TeX Live scheme for
infrastructure only, with no TeX engines at all. It is useful for automated
testing, where the actual programs and packages to be tested are installed
separately afterwards, with tlmgr install.

%build
# Nothing to build

%install
# Nothing to install

# Main scheme metapackage (empty)
%files

%changelog
%autochangelog
