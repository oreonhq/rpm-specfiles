%global source0_hash e1be6e64c09536316d20a442d615361b0089cd529d5844ba437ca383e8a3182ef5ba6e4db5d0561a2669c26623c0c8bb9f9c3c275545c23fe820d19e765e26bf
%global source1_hash 8b0050fd0699306f98a162ba8b077b96493d21c587756e29a5ac19ceb8f7dcc74d27dfc574d6524d787a26ecef13c79ddcea34bf3c14ff60f3829bae834323d4

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-unibidi-lua
Epoch:          12
Version:        svn79055
Release:        1%{?dist}
Summary:        Unicode bidi algorithm for LuaTeX
License:        MIT
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unibidi-lua.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unibidi-lua.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-unibidi-lua-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-unibidi-lua-doc <= 11:%{version}
Provides:       tex(unibidi-lua.sty)
Provides:       tex(unibidi-lua-data.lua)
Provides:       tex(unibidi-lua-interface.lua)
Provides:       tex(unibidi-lua.lua)
Provides:       tex(unibidi-lua.tex)

%description
Unicode bidi algorithm for LuaTeX.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; if test ${#%{source0_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; if test ${#%{source1_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

%build

%install
mkdir -p %{buildroot}%{_texmf_main}
tar -xf %{SOURCE0} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE1} -C %{buildroot}%{_texmf_main}
rm -rf %{buildroot}%{_texmf_main}/tlpkg

%files
%license %{_texmf_main}/doc/luatex/unibidi-lua/COPYING
%doc %{_texmf_main}/doc/luatex/unibidi-lua/
%{_texmf_main}/tex/luatex/unibidi-lua/
%exclude %{_texmf_main}/doc/luatex/unibidi-lua/COPYING

%changelog
%autochangelog
