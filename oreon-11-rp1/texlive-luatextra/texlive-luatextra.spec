%global source0_hash 172b50412fa43e5248766ee588bdeef5aaa4d0e3a27f82bfb9af1aa1d6bdc44a
%global source1_hash a89bc1425d4cf64a1e6acb8d868445cb316e4c6f253ec32b2d48cc4e812c9818

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatextra.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatextra.doc.r77682.tar.xz
BuildRequires:  tar
Provides:       texlive-luatextra-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-luatextra-doc <= 11:%{version}
Provides:       tex(luatextra.sty)

%description
Additional macros for LuaTeX.

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
%doc %{_texmf_main}/doc/lualatex/luatextra/
%{_texmf_main}/tex/lualatex/luatextra/

%changelog
%autochangelog
