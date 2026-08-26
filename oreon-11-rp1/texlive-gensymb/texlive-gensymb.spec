%global source0_hash cf5ffe40e96388d8c1b944bc41a481df0567cdd0c2914e7c96bc8aee4f6d05b3
%global source1_hash c2481e0cb548549e5bc0e1edb7ef87131b94a18c1d20c1e1d33375ba27e19493

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-gensymb
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Generic symbols for LaTeX and plain TeX
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gensymb.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gensymb.doc.r77682.tar.xz
BuildRequires:  tar
Provides:       texlive-gensymb-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-gensymb-doc <= 11:%{version}
Provides:       tex(gensymb.sty)

%description
Generic symbols for LaTeX and plain TeX.

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
%doc %{_texmf_main}/doc/latex/gensymb/
%{_texmf_main}/tex/latex/gensymb/

%changelog
%autochangelog
