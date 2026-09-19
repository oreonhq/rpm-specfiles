%global source0_hash 92d8569169725c6b1b51b8f051398e116c525bddea4679bf5df5270d31bd1bdf84287ca64f71c4501b2843b83ef48e535a4109e4061498270ae6f273279c60c1
%global source1_hash 860bfebea94341ac679b1c5770ed4b8a27a8cadecc79068731536b4240dd44923cf52a9ddabb4bb102beebb003bbd006fa739ffb86f3b8ffd4edd0b39e834d49

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-tikz-cd
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Create commutative diagrams with TikZ
License:        GPL-3.0-or-later OR LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/tikz-cd.tar.xz#/tikz-cd.or11.tar.xz
Source1:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/tikz-cd.doc.tar.xz#/tikz-cd.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-tikz-cd-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tikz-cd-doc <= 11:%{version}
Provides:       tex(tikz-cd.sty)
Provides:       tex(tikzlibrarycd.code.tex)

%description
Create commutative diagrams with TikZ.

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
%doc %{_texmf_main}/doc/latex/tikz-cd/
%{_texmf_main}/tex/generic/tikz-cd/
%{_texmf_main}/tex/latex/tikz-cd/

%changelog
%autochangelog
