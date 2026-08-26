%global source0_hash 0336a9bcef7960cff2f24945da93fd06d46e8315727014f3db70046fd4f5f97a4eb582097c6e25448aaeb57ac895006ebdcbacbdcd9144ba2d5a568fa7a10a24
%global source1_hash 79f0968218cb4678b91a3959704600d49a7005bbf906ddf0f8a699e1de4787530bb74a3a1a4f0033b502d6031b60dad5a089d3e506c880778e8369e6b0984e2a

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-transparent
Epoch:          12
Version:        svn79461
Release:        1%{?dist}
Summary:        Using a color stack for transparency with pdfTeX
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/transparent.r79461.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/transparent.doc.r79461.tar.xz
BuildRequires:  tar
Provides:       texlive-transparent-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-transparent-doc <= 11:%{version}
Provides:       tex(transparent-nometadata.sty)
Provides:       tex(transparent.sty)

%description
Using a color stack for transparency with pdfTeX.

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
%doc %{_texmf_main}/doc/latex/transparent/
%{_texmf_main}/tex/latex/transparent/

%changelog
%autochangelog
