%global source0_hash e625a7dc779acacddd25ecce2f2f9b7e4ce74fc9caf22c64b9d1ff9b32365ffc
%global source1_hash 06a3f922bd469b3ebbf642ba8a30f200b23fcbbbccef2127e957356d87a6de46

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-catchfile
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Catch an external file into a macro
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/catchfile.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/catchfile.doc.r77682.tar.xz
BuildRequires:  tar
Provides:       texlive-catchfile-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-catchfile-doc <= 11:%{version}
Provides:       tex(catchfile.sty)

%description
Catch an external file into a macro.

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
%doc %{_texmf_main}/doc/latex/catchfile/
%{_texmf_main}/tex/generic/catchfile/

%changelog
%autochangelog
