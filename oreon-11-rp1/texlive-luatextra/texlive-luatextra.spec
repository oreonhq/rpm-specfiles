%global source0_hash 735c4715697424d6edf224781b8e19b7db4a2e5259b55e0837cc0410bdf640978df549125f47563a1abe21324e1483ea7df75caf9c00fb30a51902359613a886
%global source1_hash 115fd6c7737d895b6bedade0b0b433c991ce976a688a8ea1f6f74ec4a5309c57de1ef37bfea5ca2776048c9dd8b5cdca988d4fc83c3b89e0b1ab9b17b175fc61

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-luatextra
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Additional macros for LuaTeX
License:        MIT
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatextra.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatextra.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-luatextra-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-luatextra-doc <= 11:%{version}
Provides:       tex(luatextra.sty)

%description
Additional macros for LuaTeX.

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
%doc %{_texmf_main}/doc/lualatex/luatextra/
%{_texmf_main}/tex/lualatex/luatextra/

%changelog
%autochangelog
