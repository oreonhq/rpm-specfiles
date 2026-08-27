%global source0_hash 11dabad848e1d7412f475893a0d615c207bb7fa280e09bf9325dd2aa942a5a15a0b19045a0cef9b3ea37e234fb3cf0b585c35f7c775634d143e7aba48cf17ec4
%global source1_hash 4913af89c0b4e744c8f0031f69ad272ae995d8122e12c1cc41b66d7e81afbfd16cec7d94fa17c2eb5c0bbb3fe93f2ca0ab0de2ace31e660c4748325435e857e4
%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist
Name:           texlive-lastpage
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Reference last page for Page N of M
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lastpage.tar.xz#/lastpage.or11.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lastpage.doc.tar.xz#/lastpage.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-lastpage-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lastpage-doc <= 11:%{version}
Provides:       tex(lastpage.sty)
Provides:       tex(lastpage209.sty)
Provides:       tex(lastpage2e.sty)
Provides:       tex(lastpageclassic.sty)
Provides:       tex(lastpagemodern.sty)
%description
Reference last page for Page N of M.
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
%doc %{_texmf_main}/doc/latex/lastpage/
%{_texmf_main}/tex/latex/lastpage/
%changelog
%autochangelog
