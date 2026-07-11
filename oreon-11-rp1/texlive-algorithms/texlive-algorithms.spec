%global source0_hash 24981ccfbd8c00c622fe9090a11a524d714ad42e294459ae5fde7e46e97f2919
%global source1_hash 6561bbc856f175d591306f357ea57e11facb7991f69226f915ca0a00de9c7a68

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-algorithms
Epoch:          12
Version:        svn78101
Release:        1%{?dist}
Summary:        A suite of tools for typesetting algorithms in pseudo-code
License:        LGPL-2.1-only
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algorithms.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algorithms.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-algorithms-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-algorithms-doc <= 11:%{version}
Provides:       tex(algorithm.sty)
Provides:       tex(algorithmic.sty)

%description
A suite of tools for typesetting algorithms in pseudo-code.

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
%license %{_texmf_main}/doc/latex/algorithms/COPYING
%doc %{_texmf_main}/doc/latex/algorithms/
%{_texmf_main}/tex/latex/algorithms/
%exclude %{_texmf_main}/doc/latex/algorithms/COPYING

%changelog
%autochangelog
