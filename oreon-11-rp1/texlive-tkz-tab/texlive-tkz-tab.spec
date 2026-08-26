%global source0_hash 8bbc301292f7433620c9a75f462ae022e7daa2b42c135bb37a036ad24256b8b4
%global source1_hash 060b8ed8ddf6bf1e5198fd3ec45478733f54567782a5a33c39a8e8ca89ba97d0

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-tkz-tab
Epoch:          12
Version:        svn79618
Release:        1%{?dist}
Summary:        Tables of signs and variations using PGF/TikZ
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-tab.r79618.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-tab.doc.r79618.tar.xz
BuildRequires:  tar
Provides:       texlive-tkz-tab-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tkz-tab-doc <= 11:%{version}
Provides:       tex(tkz-tab.sty)

%description
Tables of signs and variations using PGF/TikZ.

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
%doc %{_texmf_main}/doc/latex/tkz-tab/
%{_texmf_main}/tex/latex/tkz-tab/

%changelog
%autochangelog
