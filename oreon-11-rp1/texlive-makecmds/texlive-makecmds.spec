%global source0_hash 1af6eeaab78147530894c05c08eb35dfdf7674d532eba3cf657250fd71a32759e687420ebef2e1f1f73e3d59e388354cb70d90018197d267e1b85480ea2b2b3e
%global source1_hash e71632ff0f93450512e2ba4e3b4db52f2bc7015b8736cc1a7f6ae2d09b016cdff5e3e7af7000f5a2f504af6e9ed21420988224064cfc5b2ebfd7f6f1b96e2ae7

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-makecmds
Epoch:          12
Version:        svn79618
Release:        1%{?dist}
Summary:        The makecmds package
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/makecmds.tar.xz#/makecmds.or11.tar.xz
Source1:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/makecmds.doc.tar.xz#/makecmds.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-makecmds-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-makecmds-doc <= 11:%{version}
Provides:       tex(makecmds.sty)

%description
The makecmds package.

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
%doc %{_texmf_main}/doc/latex/makecmds/
%{_texmf_main}/tex/latex/makecmds/

%changelog
%autochangelog
