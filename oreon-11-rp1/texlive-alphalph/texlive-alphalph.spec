%global source0_hash b47b23d6400d2e1f4bb162adf9b9a7ca9a6150000f3aa5647a675ecb02a283e9
%global source1_hash 3e1c098e1eeeadbb674444478c176230707ada053907cb1735bf13600c4b709f

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-alphalph
Epoch:          12
Version:        svn79461
Release:        1%{?dist}
Summary:        Convert numbers to letters
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/alphalph.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/alphalph.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-alphalph-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-alphalph-doc <= 11:%{version}
Provides:       tex(alphalph.sty)

%description
Convert numbers to letters.

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
%doc %{_texmf_main}/doc/latex/alphalph/
%{_texmf_main}/tex/generic/alphalph/

%changelog
%autochangelog
