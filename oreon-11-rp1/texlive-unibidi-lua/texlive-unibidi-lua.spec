%global source0_hash 472229e2406872f42d7c5e175557043d3e597f7dd4aa05100145021ba47f1f10
%global source1_hash 11d1c221e355498eb860ecbea6d07ff0b885eab6e094e41e504e2b2b6f1280e0

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
