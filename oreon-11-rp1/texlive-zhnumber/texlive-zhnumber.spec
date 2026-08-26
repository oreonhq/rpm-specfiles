%global source0_hash 68fff717d021971424e40595db094183a80a5698a084e6cfee9e5132cec17fed6b1b7b42a111fa3325bde59f8357f4112435eae11e9ccc1d07d6475b1fd2e638
%global source1_hash 49031f2c2b863d6275a35f23936486b10f5a692f06289fef5353d75868c99e36b1523d3a1cb66aa5e7753332701382f102847df557d4404c9abf85634b148147
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; if test ${#%{source0_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; if test ${#%{source1_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
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
