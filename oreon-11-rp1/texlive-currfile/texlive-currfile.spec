%global source0_hash 1f6452c0ee5861938ca693ee37f4fc46a61ccbdeb4273a75d416f5d28b421b0eeda3250c385cb2eb806d7d87661876f96582947a4fd1e62cc9497706908368de
%global source1_hash d2a0e08fab0994e97e71efb81ee6bed52446f28871bfb61a32fe77d69f0780172a43aea190eea8f48255ba1a08c2e6ea6a82cf0dc2344da6c640ea9a01c0a9e1

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/currfile.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/currfile.doc.r77682.tar.xz
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
