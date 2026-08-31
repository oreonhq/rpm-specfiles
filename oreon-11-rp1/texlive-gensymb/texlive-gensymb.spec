%global source0_hash 00af23b7267f7296b5543b1748994cd87fc03b8577ae5c98c3a9c912279a7d0c75020d0d3bd2095020c2fd2afcc3fc91007790a62c36b54b0537a14ee12d746a
%global source1_hash 996b118977d1a22dfeb789a1d35242e9a3fb038ed482247512009f81bf29270fee56f1e64ac6640267ea27021d12b6dc2934c7929d463b818485d58629242508

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-gensymb
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Generic symbols for LaTeX and plain TeX
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/gensymb.tar.xz#/gensymb.or11.tar.xz
Source1:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/gensymb.doc.tar.xz#/gensymb.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-gensymb-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-gensymb-doc <= 11:%{version}
Provides:       tex(gensymb.sty)

%description
Generic symbols for LaTeX and plain TeX.

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
%doc %{_texmf_main}/doc/latex/gensymb/
%{_texmf_main}/tex/latex/gensymb/

%changelog
%autochangelog
