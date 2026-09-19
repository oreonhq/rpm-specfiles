%global source0_hash be272480ef4d4f2f52cbdc0073eeef89aee817d7302ca34c7cf667b62d5e0ae000c61b3aa34ccd6cf16ef772bed87326bd6056b1b536de222e8d148ce33f3a55
%global source1_hash f148ef68cc8472074fb6f6e7c35ca1df4b6f5962c73a768900477ae33e95800c1df8cae92a680b8a57e73aa0745277e2c5e7c5800fce1a89a1d411d31730cec7

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-subfigure
Epoch:          12
Version:        svn79618
Release:        1%{?dist}
Summary:        Deprecated package for subfigures
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/subfigure.tar.xz#/subfigure.or11.tar.xz
Source1:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/subfigure.doc.tar.xz#/subfigure.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-subfigure-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-subfigure-doc <= 11:%{version}
Provides:       tex(subfigure.sty)
Provides:       tex(subfigure.cfg)

%description
Deprecated package for subfigures.

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
%doc %{_texmf_main}/doc/latex/subfigure/
%{_texmf_main}/tex/latex/subfigure/

%changelog
%autochangelog
