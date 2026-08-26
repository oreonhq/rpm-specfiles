%global source0_hash 5f56fb1d813962358c737023e06bc2fa249712d8ef984f835073e11b075b676e845596a61ac312991e646d72068670b60eb002f78ac322f66d8e5a9bce185063
%global source1_hash 21d1a8063586b09ba953ac5df96a3b1552c586d66c5f2af517b1b1ceb75b40f173bd411654dd313c6aeebabc35db7543ea8edcbc8705ae104c7f63e5a5b3cf57

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-citeref
Epoch:          12
Version:        svn47407
Release:        1%{?dist}
Summary:        Add reference-page-list to citations
License:        GPL-2.0-or-later
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/citeref.r47407.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/citeref.doc.r47407.tar.xz
BuildRequires:  tar
Provides:       texlive-citeref-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-citeref-doc <= 11:%{version}
Provides:       tex(citeref.sty)

%description
Add reference-page-list to citations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

%build

%install
mkdir -p %{buildroot}%{_texmf_main}
tar -xf %{SOURCE0} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE1} -C %{buildroot}%{_texmf_main}
rm -rf %{buildroot}%{_texmf_main}/tlpkg

%files
%doc %{_texmf_main}/doc/latex/citeref/
%{_texmf_main}/tex/latex/citeref/

%changelog
%autochangelog
