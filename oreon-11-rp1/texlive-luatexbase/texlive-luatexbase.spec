%global source0_hash bec9026e8e32b3204df841f3d7ab25135f1c5e112cfc8b24ebea48def74e0ce49e446a4d45332b5e266002b83a096d901dfa78af4b4d86d7f4123986a9ef1edb
%global source1_hash b7e21911e3862a4ece388ba6cdb99cc3c88037faf2bafc6281df343812fd7618930af6eec702c675d110f2654c48eb01915360d64222edce02aa25816739c90f

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
Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/luatexbase.tar.xz#/luatexbase.or11.tar.xz
Source1:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/luatexbase.doc.tar.xz#/luatexbase.doc.or11.tar.xz
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h_expected="%{source1_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
