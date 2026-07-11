%global source0_hash 1e21406e24a35d729d113a5ffa438459b46edee955d6ec39b333e89b8c5f122a
%global source1_hash 22340a974c1510d5cda4da9f2ec8bfc0521d8776dd2b5c2ba057a2dd120df577

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-minitoc
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Produce a table of contents for each chapter, part or section
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minitoc.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minitoc.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-minitoc-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-minitoc-doc <= 11:%{version}
Provides:       tex(minitoc.sty)
Provides:       tex(mtcmess.sty)
Provides:       tex(mtcoff.sty)
Provides:       tex(mtcpatchmem.sty)

%description
Produce a table of contents for each chapter, part or section.

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
%doc %{_texmf_main}/doc/latex/minitoc/
%{_texmf_main}/tex/latex/minitoc/

%changelog
%autochangelog
