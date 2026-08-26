%global source0_hash 26edcf42839432a7bac8bb5f4314cb322fb73319792c63827f351f86083c8ddf
%global source1_hash a3180c5ac498572d04d681de7894b34698fceb9cff90e5d82fdd4496427d4f4e

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-beton
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Use Concrete fonts
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beton.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beton.doc.r77682.tar.xz
BuildRequires:  tar
Provides:       texlive-beton-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-beton-doc <= 11:%{version}
Provides:       tex(beton.sty)

%description
Use Concrete fonts.

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
%license %{_texmf_main}/doc/latex/beton/legal.txt
%doc %{_texmf_main}/doc/latex/beton/
%{_texmf_main}/tex/latex/beton/
%exclude %{_texmf_main}/doc/latex/beton/legal.txt

%changelog
%autochangelog
