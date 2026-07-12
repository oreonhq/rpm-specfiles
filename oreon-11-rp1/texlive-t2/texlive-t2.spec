%global source0_hash b58966fcb138e6b0e6f3a59f3b25b2567fcb30fa60f770ae8b61ccff14553b24
%global source1_hash 1ddb02bb52a824070d26bc4c0876037bed081e11c59c1673935c9885ac24a4dd

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
