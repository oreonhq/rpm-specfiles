%global source0_hash 83dc49aa4c113c8a0569e780616126252780fb134e1b409281a0445cce1a3b35
%global source1_hash 2111baa763d9406fb709ec3418ddc9dfc62b427ea51bad4cdbee6723d9adbb81

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-luabidi
Epoch:          12
Version:        svn78654
Release:        1%{?dist}
Summary:        Bidi functions for LuaTeX
License:        LPPL-1.3c AND MIT
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luabidi.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luabidi.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-luabidi-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-luabidi-doc <= 11:%{version}
Provides:       tex(luabidi.sty)

%description
Bidi functions for LuaTeX.

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
%doc %{_texmf_main}/doc/lualatex/luabidi/
%{_texmf_main}/tex/lualatex/luabidi/

%changelog
%autochangelog
