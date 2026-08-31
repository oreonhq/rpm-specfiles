%global source0_hash b2e3dc0671924515fe44fc3f5e370e7c6df0485e00578dfe997ed12d916a4541578b015e9dfb5b60d4f2ba17c4216d5a956ba0c9c7edb8bba71969a353c630e0
%global source1_hash 57b34f0f79efee8dc3d09e9646151d3451c899742e232534ca29302774b00582828649cb7c97d6d64cebcdb577ef85d59cc9dd9d7037ea58e8152384c0fb1d0f

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-xurl
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Allow URL breaks at any alphanumerical character
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/xurl.tar.xz#/xurl.or11.tar.xz
Source1:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/xurl.doc.tar.xz#/xurl.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-xurl-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xurl-doc <= 11:%{version}
Provides:       tex(xurl.sty)

%description
Allow URL breaks at any alphanumerical character.

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
%doc %{_texmf_main}/doc/latex/xurl/
%{_texmf_main}/tex/latex/xurl/

%changelog
%autochangelog
