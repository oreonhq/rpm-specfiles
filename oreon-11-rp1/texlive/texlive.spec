%global source0_hash none
%global tl_version 2025
Name:           texlive
Epoch:          12
Version:        %{tl_version}
Release:        1%{?dist}
Summary:        Metapackage that provides scheme-basic and collection-latexrecommended
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Requires:       texlive-collection-latexrecommended
Requires:       texlive-scheme-basic
Requires:	texlive-kpathsea
# oreon:deps

# /oreon:deps
%description
A metapackage to help people get the most useful parts of TeXLive.
Specifically, texlive-scheme-basic and
texlive-collection-latexrecommended. All of the applicable scheme
and collection metapackages exist and you can install them instead
(or in addition).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%build

%install

%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Sat May 23 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12:2025-1
- Import TeX Live 2025 split from f44 for Oreon 11
