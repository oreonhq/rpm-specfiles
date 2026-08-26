%global source0_hash 377a23e36c9f5cdcd9de36b338defcea19bce677c80e542777aeb05529c2b3b4a0a92e2c750a20c4ba21aee484968c9b6aecfeb202729a1b7a63fbb93755632e
%global source1_hash 823ae73016fc6b40ea5d45e033aa12963d866c5406fc421462a48137d6737b64c98f470ac0710f595812136107dfc6a7c1884d94f342cf228120e3c7db460960

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-ntheorem
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Enhanced theorem environment
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ntheorem.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ntheorem.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-ntheorem-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ntheorem-doc <= 11:%{version}
Provides:       tex(ntheorem.sty)

%description
Enhanced theorem environment.

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
%doc %{_texmf_main}/doc/latex/ntheorem/
%{_texmf_main}/tex/latex/ntheorem/

%changelog
%autochangelog
