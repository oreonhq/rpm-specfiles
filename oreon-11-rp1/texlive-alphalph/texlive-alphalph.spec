%global source0_hash 0b3f1b6efb00c1120326b9b8313d1bc55eb232e7f7d10acaab9425bd164ffa0552c6b63c6282983bdb9845d8a59553bd577b2ce7c377bd2e31c79baa4fde0534
%global source1_hash 1006dbb99d7fabd4a9910a92c49e0cd5b94607582fa05bbff71c8b1555bb5ddfb0e99ba101fb03665145c4b7f553fa8e1f9adda9b0b0eaa7d937ef55e5a79fd8

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-alphalph
Epoch:          12
Version:        svn79461
Release:        1%{?dist}
Summary:        Convert numbers to letters
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/alphalph.tar.xz#/alphalph.or11.tar.xz
Source1:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/alphalph.doc.tar.xz#/alphalph.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-alphalph-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-alphalph-doc <= 11:%{version}
Provides:       tex(alphalph.sty)

%description
Convert numbers to letters.

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
%doc %{_texmf_main}/doc/latex/alphalph/
%{_texmf_main}/tex/generic/alphalph/

%changelog
%autochangelog
