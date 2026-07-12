%global source0_hash 49c8ccace7f9095b88b7d3b21f3483d0ea530d9381839e923d0838d5dbfee60e
%global source1_hash 1854843900a7e22b3363a56a95c31302a06657d6add95bb9875cdf8390b34b04
%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist
Name:           texlive-zhnumber
Epoch:          12
Version:        svn79618
Release:        1%{?dist}
Summary:        Typeset Chinese representations of numbers
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhnumber.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhnumber.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-zhnumber-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-zhnumber-doc <= 11:%{version}
Provides:       tex(zhnumber-big5.cfg)
Provides:       tex(zhnumber-gbk.cfg)
Provides:       tex(zhnumber-utf8.cfg)
Provides:       tex(zhnumber.sty)
%description
Typeset Chinese representations of numbers.
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
%doc %{_texmf_main}/doc/latex/zhnumber/
%{_texmf_main}/tex/latex/zhnumber/
%changelog
%autochangelog
