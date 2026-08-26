%global source0_hash be514397b9844ae4a4f2e4f8c79d78e8b3b434bacffc18ccde3cbca462bfc49cbf7affd75b70fb013266c00f8f9be8636729ee18ee1274b0241ad74293751450
%global source1_hash d92f76ffd3049776bd0f8e80ce9cf7d46a55a5988eaccb9c8982f63b80490af1983a5600724501f6431f401b22a9a34d8f9dca20c6f2b8ccf85ddef0a65a063b

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-amsfonts
Epoch:          12
Version:        svn77682
Release:        11%{?dist}
Summary:        TeX fonts from the American Mathematical Society
License:        OFL-1.1
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsfonts.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsfonts.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-amsfonts-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amsfonts-doc <= 11:%{version}

%description
An extended set of fonts for use in mathematics from the American Mathematical
Society. Split from texlive-collection-basic for oreon bootstrap.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; if test ${#%{source0_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; if test ${#%{source1_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

%build

%install
mkdir -p %{buildroot}%{_texmf_main}
tar -xf %{SOURCE0} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE1} -C %{buildroot}%{_texmf_main}
rm -rf %{buildroot}%{_texmf_main}/tlpkg

%files
%license %{_texmf_main}/doc/fonts/amsfonts/OFL.txt
%{_texmf_main}/fonts/afm/public/amsfonts/
%{_texmf_main}/fonts/map/dvips/amsfonts/
%{_texmf_main}/fonts/source/public/amsfonts/
%{_texmf_main}/fonts/tfm/public/amsfonts/
%{_texmf_main}/fonts/type1/public/amsfonts/
%{_texmf_main}/tex/latex/amsfonts/
%{_texmf_main}/tex/plain/amsfonts/
%doc %{_texmf_main}/doc/fonts/amsfonts/
%exclude %{_texmf_main}/doc/fonts/amsfonts/OFL.txt

%changelog
%autochangelog
