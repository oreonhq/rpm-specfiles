%global source0_hash 6fe02cc75d2b655392c7e6e4b756ad8963a10e1d3bd42da820fa78f7be98c2e5
%global source1_hash 51223b4d2b4ddead6d5f1368a029203f3b6ba0a9b87ccc5454c117937690e5bf

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
