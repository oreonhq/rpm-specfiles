%global source0_hash f363ae3399fa129cdb34825c81df24458468aa3a3bc629223c12e0b13894e5662d1d3774a48049f64a5a55edeb957b7a5da5cf033da9fbd4c733467dcdcacb62
%global source1_hash c758b54d0c97c715c0ce2dff07ab7c85144bf782c515b553414505811ce0413f979a34201df5b6b7cc4e9c0a7a0d0e7cb1b7e742a8ebf4174cdacfd2f1ed84d3

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; if test ${#%{source0_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; if test ${#%{source1_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
