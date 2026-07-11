%global source0_hash 81eb6eba59764b6ccb7210f8e1c928eb7b2d8d57d3a59b0411b027dab8d549f4
%global source1_hash f3e55f59c658c8b9cf0f3a378b44997591dd613eee66cb4b9c4a52ef73f1395f

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-currfile
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Provide file name info for the current TeX file
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/currfile.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/currfile.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-currfile-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-currfile-doc <= 11:%{version}
Provides:       tex(currfile-abspath.sty)
Provides:       tex(currfile.sty)

%description
Provide file name info for the current TeX file.

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
%doc %{_texmf_main}/doc/latex/currfile/
%{_texmf_main}/tex/latex/currfile/

%changelog
%autochangelog
