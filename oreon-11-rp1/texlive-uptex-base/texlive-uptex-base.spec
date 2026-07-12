%global source0_hash b56449f827a13da8e199a6beba37f7f68be6db516d63b61cc49c067fd387f426
%global source1_hash 5cd0b6791b8f09e5f8132d512a1868ee9004cacf906ed90cee8f05f157ef3a00

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-uptex-base
Epoch:          12
Version:        svn77840
Release:        1%{?dist}
Summary:        Plain TeX formats and documents for upTeX
License:        BSD
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uptex-base.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uptex-base.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-uptex-base-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-uptex-base-doc <= 11:%{version}
Provides:       tex(ukinsoku.tex)
Provides:       tex(uptex.tex)

%description
Plain TeX formats and documents for upTeX.

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
%doc %{_texmf_main}/doc/uptex/uptex-base/
%{_texmf_main}/tex/uptex/uptex-base/

%changelog
%autochangelog
