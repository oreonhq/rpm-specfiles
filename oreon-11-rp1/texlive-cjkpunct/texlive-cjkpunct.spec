%global source0_hash cb44aa3386cd79f05980e5402adcbbf9f8b67fa76bdd5b293063fe9810520edbdf243656cfb54fe17d6ca43d405e6b16e8012eda63bae3cb3d8fc0f7755e2551
%global source1_hash cb9383b6d3fe9ffd5926d10dddcb1ea758aabda232f015b22f61dc8a9b316193b30ca2d8e2b849b1c03d92e0073bba6d90cc5b3b50f47b28a745dff2f7229486

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h_expected="%{source1_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
