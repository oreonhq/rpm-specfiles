%global source0_hash dec0527223fdb0f897ccf54e96691cd68b933ac61de4c036e21fd35bff93d32766444fe6971492ce64328f92621bd2949ebb669ab33b6b6f4ede88280351292d
%global source1_hash c53cf11bc81d9a8f5aa19c264a1970d4819400ceaffa20b688d0709546113f932b82b6b6d12cf9fb31b2a3d2c0d45b6b33ee3cb3bd0060c961360389839b1475

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-ipaex
Epoch:          12
Version:        svn61719
Release:        1%{?dist}
Summary:        IPAex fonts for Japanese
License:        IPA
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ipaex.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ipaex.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-ipaex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ipaex-doc <= 11:%{version}
Provides:       texlive-ipaex = %{epoch}:%{version}-%{release}

%description
IPAex fonts for Japanese.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; if test ${#%{source0_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; if test ${#%{source1_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

%build

%install
mkdir -p %{buildroot}%{_texmf_main}
tar -xf %{SOURCE0} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE1} -C %{buildroot}%{_texmf_main}
rm -rf %{buildroot}%{_texmf_main}/tlpkg

%files
%doc %{_texmf_main}/doc/fonts/ipaex/
%{_texmf_main}/fonts/truetype/public/ipaex/

%changelog
%autochangelog
