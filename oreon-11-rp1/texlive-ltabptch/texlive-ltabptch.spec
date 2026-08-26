%global source0_hash abeb5f245a822605b877131a4b7db563ec5172b9593461484874a7959e71171a
%global source1_hash 564b851409b7cfdc94ead90a1213a410afdf530fd03d58ae6afffe76e753058d

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-ltabptch
Epoch:          12
Version:        svn17533
Release:        1%{?dist}
Summary:        Bug fix for longtable
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltabptch.r17533.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltabptch.doc.r17533.tar.xz
BuildRequires:  tar
Provides:       texlive-ltabptch-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ltabptch-doc <= 11:%{version}
Provides:       tex(ltabptch.sty)

%description
Bug fix for longtable.

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
%doc %{_texmf_main}/doc/latex/ltabptch/
%{_texmf_main}/tex/latex/ltabptch/

%changelog
%autochangelog
