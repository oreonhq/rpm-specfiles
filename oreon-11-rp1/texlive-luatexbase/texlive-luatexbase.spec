%global source0_hash 1a497d3bd314884a07f4eb60d22d4c3d3496233f6d8e1e89da16fb3ffb86cb65
%global source1_hash 41f9924168e029e8728f1a3fcc426d1e87631463b4a0b22797f0f7c08c677ae6

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-luatexbase
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Basic resource management for LuaTeX code
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatexbase.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatexbase.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-luatexbase-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-luatexbase-doc <= 11:%{version}
Provides:       tex(luatexbase-attr.sty)
Provides:       tex(luatexbase-cctb.sty)
Provides:       tex(luatexbase-compat.sty)
Provides:       tex(luatexbase-loader.sty)
Provides:       tex(luatexbase-mcb.sty)
Provides:       tex(luatexbase-modutils.sty)
Provides:       tex(luatexbase-regs.sty)
Provides:       tex(luatexbase.loader.lua)
Provides:       tex(luatexbase.sty)

%description
Basic resource management for LuaTeX code.

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
%doc %{_texmf_main}/doc/luatex/luatexbase/
%{_texmf_main}/tex/luatex/luatexbase/

%changelog
%autochangelog
