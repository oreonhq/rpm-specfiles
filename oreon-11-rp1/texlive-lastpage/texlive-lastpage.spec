%global source0_hash 6e968d2b8fcb2d82ef404a54f39a3bd43714f45cb14986a16f726c39a17af0e4
%global source1_hash f6452b5d6ccb03501476e4004e616147b8e3f0451741d94a38cd2390a3bd72a8
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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lastpage.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lastpage.doc.r77682.tar.xz
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
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
