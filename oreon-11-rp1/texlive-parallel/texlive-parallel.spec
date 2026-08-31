%global source0_hash c375a62dd5d220adfcb99ec42ecf8aeb75161d5c1ef542578a1911d3b3e343144716c26f518df448583ed4443242c1e66479f7c34cf074bd4d257d1a4e8c7358

Name:           texlive-parallel
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Typeset parallel texts in two columns
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/parallel.tar.xz#/parallel.or11.tar.xz
BuildArch:      noarch
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(parallel.sty)

%description
Provides an environment for typesetting text in two parallel columns.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T
tar xf %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{_texmf_main}/tex/latex/parallel
cp -a tex/latex/parallel/* %{buildroot}%{_texmf_main}/tex/latex/parallel/

%files
%{_texmf_main}/tex/latex/parallel/

%changelog
%autochangelog
