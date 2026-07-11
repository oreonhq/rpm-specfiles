%global source0_hash 91006383de0aa2244953c9d1aca8213316119c8359b836a47a0fc0cbb0b46188
%global source1_hash e33b25aedd9cfa5549f86de6d1a976e4da767fc50ded75e50f87734fc0a86266

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-pdfcol
Epoch:          12
Version:        svn64469
Release:        1%{?dist}
Summary:        Macros for maintaining colour stacks under pdfTeX
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfcol.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfcol.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-pdfcol-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pdfcol-doc <= 11:%{version}
Provides:       tex(pdfcol.sty)

%description
Macros for maintaining colour stacks under pdfTeX.

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
%doc %{_texmf_main}/doc/latex/pdfcol/
%{_texmf_main}/tex/latex/pdfcol/

%changelog
%autochangelog
