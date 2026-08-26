%global source0_hash 7425b3bab2d1a29a1ccb57349b40acd2ad0b40b40e3f3e7f26f85462a55d2b0c9896b875ef642a132f1f148f1ec20b12bc852d21bb4ceb095487f6ac60804b7c
%global source1_hash 505f8d9c2f0122836f9d2309b68824e98d52db5425d1896d9d65b910f0b019d6c5c27acdbbdf80ef48e27cbb8477c1056907a6096e2105f46abaea70299aa8ba

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-t2
Epoch:          12
Version:        svn79618
Release:        1%{?dist}
Summary:        Support for using T2 encoding (provides misccorr)
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/t2.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/t2.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-t2-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-t2-doc <= 11:%{version}
Provides:       tex(citehack.sty)
Provides:       tex(mathtext.sty)
Provides:       tex(misccorr.sty)
Provides:       tex(alias-cmc.tex)
Provides:       tex(alias-wncy.tex)
Provides:       tex(cyralias.tex)
Provides:       tex(fnstcorr.tex)

%description
Support for using T2 encoding (provides misccorr).

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
%doc %{_texmf_main}/doc/generic/t2/
%{_texmf_main}/fonts/enc/t2/
%{_texmf_main}/tex/generic/t2/
%{_texmf_main}/tex/latex/t2/

%changelog
%autochangelog
