%global source0_hash 1e068a0b402a5c69b44a86d797cb24266b2883c698decd8b8464c99b131d292cc5ac44249ba8e89dc0a414d6f12d73d4c069ffc3081cfa4b9926ca412bfc3dd6
%global source1_hash f9ac2953877cd830e1cf3402f3f2bac1f8159d05a4a74e89047c494ae04dc8930f1c09701f83871b4361976572ae7d1c5fbdaf3af3d9e6db12347a207f1b82cb

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-zhmetrics-uptex
Epoch:          12
Version:        svn40728
Release:        1%{?dist}
Summary:        Chinese font metrics for upTeX
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhmetrics-uptex.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhmetrics-uptex.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-zhmetrics-uptex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-zhmetrics-uptex-doc <= 11:%{version}
Provides:       texlive-zhmetrics-uptex = %{epoch}:%{version}-%{release}

%description
Chinese font metrics for upTeX.

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
%doc %{_texmf_main}/doc/fonts/zhmetrics-uptex/
%{_texmf_main}/fonts/tfm/public/zhmetrics-uptex/
%{_texmf_main}/fonts/vf/public/zhmetrics-uptex/

%changelog
%autochangelog
