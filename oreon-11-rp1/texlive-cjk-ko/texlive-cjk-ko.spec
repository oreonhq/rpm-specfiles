%global source0_hash 4252436af26489464f4865a91902518a6af47e4d176b12e04cfbe4573ad8303df2f613920dd9bfbd0842bb13cbf847bc7ce6c274218a38cf719ba82573d6b7a6
%global source1_hash 4bc8c11c2f1240590d5576d69acc7fab41df8b75dd71448351d079d318f3e28ec9ec8f11165fad5d60d548274de7c7aaeb132a5f4e87966d5bb005fb968980ea

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-cjk-ko
Epoch:          12
Version:        svn79618
Release:        1%{?dist}
Summary:        Extension of CJK package for Korean typesetting
License:        GPL-2.0-or-later
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjk-ko.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjk-ko.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-cjk-ko-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-cjk-ko-doc <= 11:%{version}
Provides:       tex(cjkutf8-josa.sty)
Provides:       tex(cjkutf8-ko.sty)
Provides:       tex(cjkutf8-nanummjhanja.sty)
Provides:       tex(kolabels-utf.sty)
Provides:       tex(konames-utf.sty)
Provides:       tex(kotex.sty)

%description
Extension of CJK package for Korean typesetting.

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
%doc %{_texmf_main}/doc/latex/cjk-ko/
%{_texmf_main}/tex/latex/cjk-ko/

%changelog
%autochangelog
