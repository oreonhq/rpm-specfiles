%global source0_hash 213f663184838c2113939b8c3bfbeb344ed37db5dd040e0f21834675136310ed7256cc50f827f29695feb758031b9c6f859e1696c15ac57a6d3e157b7c894dc5
%global source1_hash 4b18f3d63b301a60e1a5b501b24fa08b1b09024f112f225a2ab9855f8308c187ff763344a5921ffede13112a23e06920957259ca5e8b4420f092bcfd4aacaa35

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-xstring
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        String manipulation for LaTeX
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xstring.tar.xz#/xstring.or11.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xstring.doc.tar.xz#/xstring.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-xstring-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xstring-doc <= 11:%{version}
Provides:       tex(xstring.sty)
Provides:       tex(xstring.tex)

%description
String manipulation for LaTeX.

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
%doc %{_texmf_main}/doc/generic/xstring/
%{_texmf_main}/tex/generic/xstring/

%changelog
%autochangelog
