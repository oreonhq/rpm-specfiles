%global source0_hash bc23e44c676a7b45a5e7eca5b03ab76544273a3da93dde2d68c4ba631cf0bf23c7f07046f5a84456e71552bbf84c25f6fb17f2666ef400f096f9a1084443e316
%global source1_hash b686d073f89f8cea6318a168dbb0f624d58bf535d2c3adfc8a3a239e1391b61b7f23b4ef2190908f3da95aaed71ad61a14f49076e284fcc227a4e2942c2f490d

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-catchfile
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Catch an external file into a macro
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/catchfile.tar.xz#/catchfile.or11.tar.xz
Source1:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/catchfile.doc.tar.xz#/catchfile.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-catchfile-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-catchfile-doc <= 11:%{version}
Provides:       tex(catchfile.sty)

%description
Catch an external file into a macro.

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
%doc %{_texmf_main}/doc/latex/catchfile/
%{_texmf_main}/tex/generic/catchfile/

%changelog
%autochangelog
