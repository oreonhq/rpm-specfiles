%global source0_hash 42bc819e84ad9b5c4da40590b69e35526f3b2d6acf080daff57b7f74e996f7d6
%global source1_hash ed17678607e927a9fa94a4f004d5278429f7f2b1206d588d8388fab237e55b71

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-everyhook
Epoch:          12
Version:        svn35675
Release:        1%{?dist}
Summary:        Hooks for standard TeX token registers
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/everyhook.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/everyhook.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-everyhook-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-everyhook-doc <= 11:%{version}
Provides:       tex(everyhook.sty)

%description
Hooks for standard TeX token registers.

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
%doc %{_texmf_main}/doc/latex/everyhook/
%{_texmf_main}/tex/latex/everyhook/

%changelog
%autochangelog
