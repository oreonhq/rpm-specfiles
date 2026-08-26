%global source0_hash 31dc5396576113f6b0e2def3212e71ed9b241927a1e943bdf80da45859f75dbfa47ab8e8afe40cb63ed9885dba94154dd2a095bd35a997bb043c371ddb72f2ff
%global source1_hash 84c42b3d2a2560b24bd54d14c5f53576edfa3742c7cb31f186bf1d18c123a62e99e3bbf608afa59de8aeec5e1a52758c2864eac64f377e99743df503307e0846

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-sansmathaccent
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Correct placement of accents in sans-serif maths
License:        OFL-1.1
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sansmathaccent.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sansmathaccent.doc.r77682.tar.xz
BuildRequires:  tar
Provides:       texlive-sansmathaccent-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-sansmathaccent-doc <= 11:%{version}
Provides:       tex(sansmathaccent.sty)

%description
Correct placement of accents in sans-serif maths.

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
%doc %{_texmf_main}/doc/fonts/sansmathaccent/
%{_texmf_main}/fonts/map/dvips/sansmathaccent/
%{_texmf_main}/fonts/tfm/public/sansmathaccent/
%{_texmf_main}/fonts/vf/public/sansmathaccent/
%{_texmf_main}/tex/latex/sansmathaccent/

%changelog
%autochangelog
