%global source0_hash 5bd0133833979011ea643e8b54ad7b0e116abf1dab0ba83656168afd35d397c19c0486efb4e48111a9bb009c5061bc94aee69769cf519b0eb0aebb168679ac6e
%global source1_hash f1c7eaba6f87d61b46ede616a9b9fa7edc7d9f0fc472ade3bd839cb10b1a0893ddbbf035668cb301cf98fa9e732499a12b19fa8b46a49d413771b533bbecc2e0

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-japanese-otf
Epoch:          12
Version:        svn79618
Release:        1%{?dist}
Summary:        Advanced font selection for platex
License:        BSD
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/japanese-otf.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/japanese-otf.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-japanese-otf-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-japanese-otf-doc <= 11:%{version}
Provides:       tex(ajmacros.sty)
Provides:       tex(mlcid.sty)
Provides:       tex(mlutf.sty)
Provides:       tex(otf.sty)
Provides:       tex(redeffont.sty)

%description
Advanced font selection for platex.

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
%doc %{_texmf_main}/doc/fonts/japanese-otf/
%{_texmf_main}/fonts/tfm/public/japanese-otf/
%{_texmf_main}/fonts/vf/public/japanese-otf/
%{_texmf_main}/tex/platex/japanese-otf/

%changelog
%autochangelog
