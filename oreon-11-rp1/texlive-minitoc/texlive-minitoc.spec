%global source0_hash 53f60676378be98246299d0d6b5696a0a737f7cf3febe3fd2d75174bbd74b09c815eb79f92d080d962447400032270006a0a16cf23eda156f21a3eb418e149d8
%global source1_hash 6527c533a7563b731c492f2aadf26f6ed3023fa11dfca75547f12f80038b5a62aae62c1682359a0a5baffea1b943085cac7240c0320cf49fbeedee0f12d6bc1b

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minitoc.tar.xz#/minitoc.or11.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minitoc.doc.tar.xz#/minitoc.doc.or11.tar.xz
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h_expected="%{source1_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
