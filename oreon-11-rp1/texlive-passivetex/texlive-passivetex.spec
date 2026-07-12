%global source0_hash 5a7928cb7c7317584e9090e34baee9b6a91ea727eed611fa5691164bf734eeb5
%global source1_hash none

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-passivetex
Epoch:          12
Version:        svn69742
Release:        1%{?dist}
Summary:        Support package for XML/SGML typesetting
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/passivetex.tar.xz
BuildRequires:  tar
Provides:       texlive-passivetex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-passivetex-doc <= 11:%{version}
Provides:       tex(dummyels.sty)
Provides:       tex(fotex.sty)
Provides:       tex(mlnames.sty)
Provides:       tex(teixml.sty)
Provides:       tex(teixmlslides.sty)
Provides:       tex(ucharacters.sty)
Provides:       tex(unicode.sty)

%description
Support package for XML/SGML typesetting.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || true

%build

%install
mkdir -p %{buildroot}%{_texmf_main}
tar -xf %{SOURCE0} -C %{buildroot}%{_texmf_main}
rm -rf %{buildroot}%{_texmf_main}/tlpkg

%files
%{_texmf_main}/tex/xmltex/passivetex/

%changelog
%autochangelog
