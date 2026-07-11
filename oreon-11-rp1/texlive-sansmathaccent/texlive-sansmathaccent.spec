%global source0_hash 62cf97334eb2c1d4056cb7f72ef2e59d99edaef151c3f4870116cc23056394b9
%global source1_hash 213ce2af2390b35ef395abd735b6e947936fbef0d38686cd323d1462af63471b

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sansmathaccent.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sansmathaccent.doc.tar.xz
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
