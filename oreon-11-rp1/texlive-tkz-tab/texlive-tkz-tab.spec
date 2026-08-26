%global source0_hash 2603061c545c7da0bd474ab7a34d0f0364b85341a390d3a30f6d084b5cb7ad96cd8ea2cd002ef9cb91b718f819a0157a79b96eb0135c7f3c46566239a5bc18fc
%global source1_hash a36c37c5d06ad720ac3f57f7be7d11e53c10d4cd57f32498359b667d336cfd7c5e528f05b23d0f501ec227a097db3f76302fe182062388e97a49d544ee9cb0ed

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
