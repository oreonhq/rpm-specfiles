%global source0_hash 0d5ed318e8c77bbea56b2033df902d86f2a585c8ec1870fb184167a23ba9d5f871af32bdd0e6576ad1de2efa745b340cb55312e13cd9bf75778d167d96821620
%global source1_hash 8364779804341cd337b651097db3b4ecbc6eef5f8d7c9ea39a001f98b7e576161d3b8100010f167f21eff539c66f57eab80c51bba7eab382c8778f798e1fc977
%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist
Name:           texlive-lettrine
Epoch:          12
Version:        svn77053
Release:        1%{?dist}
Summary:        Typeset dropped capitals
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lettrine.tar.xz#/lettrine.or11.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lettrine.doc.tar.xz#/lettrine.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-lettrine-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lettrine-doc <= 11:%{version}
Provides:       tex(lettrine-2006-03-17.sty)
Provides:       tex(lettrine-2015-08-31.sty)
Provides:       tex(lettrine-2018-08-18.sty)
Provides:       tex(lettrine-2022-09-25.sty)
Provides:       tex(lettrine-2023-04-18.sty)
Provides:       tex(lettrine.cfg)
Provides:       tex(lettrine.sty)
%description
Typeset dropped capitals.
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
%doc %{_texmf_main}/doc/latex/lettrine/
%{_texmf_main}/tex/latex/lettrine/
%changelog
%autochangelog
