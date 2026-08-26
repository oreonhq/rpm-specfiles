%global source0_hash b1909754c3b531853dae44d17d788f9b7a7d0b10f76893d13ce8848cb7ed5a055f448dc829bfaab64a3cda1326dacec07949bdd8d2e543ed05b09ce28efeaf2e
%global source1_hash 6261a9ab885bc2575dc8b6167a70530ef13a6cd2277d4983afe72fef6b74c2edad55bc29a9bc8c8b863a5ec4b46e07d250391d20964caab9bdb1416575d25130

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-footmisc
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        A range of footnote options
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/footmisc.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/footmisc.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-footmisc-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-footmisc-doc <= 11:%{version}
Provides:       tex(footmisc-2011-06-06.sty)
Provides:       tex(footmisc-2022-02-14.sty)
Provides:       tex(footmisc.sty)

%description
A range of footnote options.

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
%doc %{_texmf_main}/doc/latex/footmisc/
%{_texmf_main}/tex/latex/footmisc/

%changelog
%autochangelog
