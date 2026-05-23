%global tl_version 2025

Name:           texlive-scheme-basic
Epoch:          12
Version:        svn54191
Release:        2%{?dist}
Summary:        basic scheme (plain and latex)

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-collection-basic
Requires:       texlive-collection-latex

%description
basic scheme (plain and latex) This is the basic TeX Live scheme: it is a small
set of files sufficient to typeset plain TeX or LaTeX documents in PostScript
or PDF, using the Computer Modern fonts. This scheme corresponds to
collection-basic and collection-latex.



%build
# Nothing to build

%install
# Nothing to install

# Main scheme metapackage (empty)
%files


%changelog
* Sat May 23 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12:svn54191-2
- Import TeX Live 2025 split from f44 for Oreon 11
