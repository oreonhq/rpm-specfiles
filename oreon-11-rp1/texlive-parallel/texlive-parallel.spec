%global source0_hash 2f607e1f1ad0b3f0a6b43dbef392a1a2f500e041fbea3dae6bf4de696444e128

Name:           texlive-parallel
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Typeset parallel texts in two columns
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parallel.r77682.tar.xz
BuildArch:      noarch
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(parallel.sty)

%description
Provides an environment for typesetting text in two parallel columns.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
