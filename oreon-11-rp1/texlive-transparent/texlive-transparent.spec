%global source0_hash a83f6b878cae99137ee6a556ba997a95615f6b990470df6586584abb6371b619
%global source1_hash 4d56130f80e8be7b5d99c133c320dd0ee88dc78b49ee821b572b939ea251c5b9

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-transparent
Epoch:          12
Version:        svn79461
Release:        1%{?dist}
Summary:        Using a color stack for transparency with pdfTeX
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/transparent.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/transparent.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-transparent-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-transparent-doc <= 11:%{version}
Provides:       tex(transparent-nometadata.sty)
Provides:       tex(transparent.sty)

%description
Using a color stack for transparency with pdfTeX.

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
%doc %{_texmf_main}/doc/latex/transparent/
%{_texmf_main}/tex/latex/transparent/

%changelog
%autochangelog
