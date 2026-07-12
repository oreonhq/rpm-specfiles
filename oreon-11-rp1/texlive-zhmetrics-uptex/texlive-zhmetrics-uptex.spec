%global source0_hash 23d39e30eccc3b650f2a87ad830e1906f1e24d47e41d40cc36d846cd6c32350f
%global source1_hash 5e11ac8d55376b5c1283440654f065de738bbe1b2c0c6ddcba99672a4814a9c6

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
