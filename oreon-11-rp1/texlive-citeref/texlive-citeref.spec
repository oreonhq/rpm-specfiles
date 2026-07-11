%global source0_hash 145a1f6e78da6e85793b942ec51d6820a6b1ddaa9f88f69487afb2f0aa7139e8
%global source1_hash 9e450b7ee1f945111d3e118d64d1a56c09ca01a0ce90d9971c014814555ab22a

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/citeref.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/citeref.doc.tar.xz
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
