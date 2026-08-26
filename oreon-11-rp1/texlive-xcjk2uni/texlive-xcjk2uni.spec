%global source0_hash 0f1589f740bc9a24eb2b7214711c6e4f7c3a0f2fbe2ec76fc1d5bf0c11471c18
%global source1_hash 043124bacfad0c2aac9087ab39abcdac54daaa026ccada1b67729d667631d06a

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-xcjk2uni
Epoch:          12
Version:        svn54958
Release:        1%{?dist}
Summary:        Convert CJK characters to Unicode
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xcjk2uni.r54958.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xcjk2uni.doc.r54958.tar.xz
BuildRequires:  tar
Provides:       texlive-xcjk2uni-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xcjk2uni-doc <= 11:%{version}
Provides:       tex(xCJK2uni.sty)
Provides:       tex(xCJK2uni-UBg5plus.def)
Provides:       tex(xCJK2uni-UBig5.def)
Provides:       tex(xCJK2uni-UGB.def)
Provides:       tex(xCJK2uni-UGBK.def)
Provides:       tex(xCJK2uni-UJIS.def)
Provides:       tex(xCJK2uni-UKS.def)

%description
Convert CJK characters to Unicode.

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
%doc %{_texmf_main}/doc/latex/xcjk2uni/
%{_texmf_main}/tex/latex/xcjk2uni/

%changelog
%autochangelog
