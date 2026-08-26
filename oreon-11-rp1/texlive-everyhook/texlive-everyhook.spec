%global source0_hash 56547973d184de21ff5d6d3eaf1baf9b8cdbcf93307c31fbbcf658350ef0d441509ce359266ea6f962ef9b40b1680b47e4c14a822aa043ab8174ab0610df1665
%global source1_hash 331def0138dac385605b3ea1d88af6d5d1ae29bac696b76f41cdcfd070d50915eb3371a14a894b1e59bf35d55eb7dabecfe18e89f0bfbe6f028ce5fedfe1bbc2

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; if test ${#%{source0_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; if test ${#%{source1_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
