%global source0_hash 13a795ec51c28b1599211e236f556886a87a48be87531ae43e0ee4d07ff32340
%global source1_hash ad084a4f6734953310f617a7b9428c2e656b648040967d793860d4d32607a1fc

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-cjkpunct
Epoch:          12
Version:        svn41119
Release:        1%{?dist}
Summary:        Adjust location and spacing of CJK punctuation
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjkpunct.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjkpunct.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-cjkpunct-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-cjkpunct-doc <= 11:%{version}
Provides:       tex(CJKpunct.sty)

%description
Adjust location and spacing of CJK punctuation.

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
%doc %{_texmf_main}/doc/latex/cjkpunct/
%{_texmf_main}/tex/latex/cjkpunct/

%changelog
%autochangelog
