%global source0_hash ef66d4e235a4b314346c4541b0a2e702338670ebd81568234c3c5b1692d6c6132adbea2c3da9428c090ec65a2a10c312415442bb634249e6fd8a3cc58514a96a
%global source1_hash 3cde8f9ce37a38293d589737f15a35ac4ec2afea2a821022878e92d8d32fc90f5068a672095aa72ac54352c089fcf3dc9430d6d72a6a22f524e6c9dec6171bdc

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-mnsymbol
Epoch:          12
Version:        svn18651
Release:        1%{?dist}
Summary:        Mathematical symbol font for Adobe MinionPro
License:        OFL-1.1
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mnsymbol.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mnsymbol.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-mnsymbol-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-mnsymbol-doc <= 11:%{version}
Provides:       tex(MnSymbol.sty)

%description
Mathematical symbol font for Adobe MinionPro.

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
%doc %{_texmf_main}/doc/latex/mnsymbol/
%{_texmf_main}/fonts/enc/dvips/mnsymbol/
%{_texmf_main}/fonts/map/dvips/mnsymbol/
%{_texmf_main}/fonts/map/vtex/mnsymbol/
%{_texmf_main}/fonts/opentype/public/mnsymbol/
%{_texmf_main}/fonts/source/public/mnsymbol/
%{_texmf_main}/fonts/tfm/public/mnsymbol/
%{_texmf_main}/fonts/type1/public/mnsymbol/
%{_texmf_main}/tex/latex/mnsymbol/

%changelog
%autochangelog
