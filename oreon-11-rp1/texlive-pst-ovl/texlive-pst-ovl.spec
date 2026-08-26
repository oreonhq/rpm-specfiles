%global source0_hash d0236e64f46468e02caddfc41b16e8f95123b863f9f6d2b40b23dd3cbca8c275
%global source1_hash ace3003f2a584d2f16eb2d8ce1d24458ffa8909028d97bf1430ee6010802b207

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-pst-ovl
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Overlay macros for PSTricks
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-ovl.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-ovl.doc.r77682.tar.xz
BuildRequires:  tar
Provides:       texlive-pst-ovl-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pst-ovl-doc <= 11:%{version}
Provides:       tex(pst-ovl.sty)
Provides:       tex(pst-ovl.tex)

%description
Overlay macros for PSTricks.

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
%doc %{_texmf_main}/doc/generic/pst-ovl/
%{_texmf_main}/dvips/pst-ovl/
%{_texmf_main}/tex/generic/pst-ovl/
%{_texmf_main}/tex/latex/pst-ovl/

%changelog
%autochangelog
