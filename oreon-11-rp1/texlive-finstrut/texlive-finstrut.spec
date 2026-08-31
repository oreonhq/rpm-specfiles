%global source0_hash 9a4d446bcf36576330da37435d8b9aadb07a3892febc219cddc51053302a48d546c4da251a818262dcce30c81b6fe8bcfe0484f8802ee427661c3fb792a47153
%global source1_hash 6be2bce2a777f869b88d3f574837b70b6a0b959f23db092554a1879e9f278f341696e8f4d5d80853366685739f7929d9bc1003a5382d9bd961260413d4855e63

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-finstrut
Epoch:          12
Version:        svn21719
Release:        1%{?dist}
Summary:        Adjust behaviour of the ends of footnotes
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/finstrut.tar.xz#/finstrut.or11.tar.xz
Source1:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/finstrut.doc.tar.xz#/finstrut.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-finstrut-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-finstrut-doc <= 11:%{version}
Provides:       tex(finstrut.sty)

%description
Adjust behaviour of the ends of footnotes.

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
%doc %{_texmf_main}/doc/latex/finstrut/
%{_texmf_main}/tex/latex/finstrut/

%changelog
%autochangelog
