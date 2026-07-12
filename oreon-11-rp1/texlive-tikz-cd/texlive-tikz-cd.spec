%global source0_hash e225b02dcc2a334508529e27a7d7b3f283939b57507019ab6bcf99ff453ac2cb
%global source1_hash b723efcdb7a584f5056c93f851f47eddb89bfb5001c81c3273e63ed8036bbe73

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-tikz-cd
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Create commutative diagrams with TikZ
License:        GPL-3.0-or-later OR LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-cd.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-cd.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-tikz-cd-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tikz-cd-doc <= 11:%{version}
Provides:       tex(tikz-cd.sty)
Provides:       tex(tikzlibrarycd.code.tex)

%description
Create commutative diagrams with TikZ.

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
%doc %{_texmf_main}/doc/latex/tikz-cd/
%{_texmf_main}/tex/generic/tikz-cd/
%{_texmf_main}/tex/latex/tikz-cd/

%changelog
%autochangelog
