%global source0_hash b937359bde7ade3645edb6435a824ee6af66e51e7cb518694706224e63e4d92391911f01745d331cb92e62c34c085aa5f284babacf6f7ab0a0474cbf06b00859
%global source1_hash 85b6422630754144e4f9c552899e588f1650af2837cf88e8f47106e2919bee8dd956002e102f83dd76107edb0e61e2a6d4ebfaaf6fc06289942fdb32385454ba

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-ptex-base
Epoch:          12
Version:        svn64072
Release:        1%{?dist}
Summary:        Plain TeX format and docs for pTeX base
License:        BSD
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex-base.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex-base.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-ptex-base-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ptex-base-doc <= 11:%{version}
Provides:       tex(ascii-jplain.tex)
Provides:       tex(kinsoku.tex)
Provides:       tex(ptex.tex)

%description
Plain TeX format and docs for pTeX base.

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
%doc %{_texmf_main}/doc/ptex/ptex-base/
%{_texmf_main}/tex/ptex/ptex-base/

%changelog
%autochangelog
