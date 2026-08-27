%global source0_hash 672a92354c56341678ff3080ef978e8b152c8670283bc725474ccbac30a8149767bfaaca673a800d5098e0bb949ee2d8f9fa20c4da58b6c62fe163a10c916205
%global source1_hash f1df290a202826297921a646d17cb6bc14ed463769cd52140cbcfdb8576d1f296a25d2951c8770c6b57f46e88a712b8076a596064068263c4a5682570bd6abf2

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltabptch.tar.xz#/ltabptch.or11.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltabptch.doc.tar.xz#/ltabptch.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-ltabptch-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ltabptch-doc <= 11:%{version}
Provides:       tex(ltabptch.sty)

%description
Bug fix for longtable.

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
%doc %{_texmf_main}/doc/latex/ltabptch/
%{_texmf_main}/tex/latex/ltabptch/

%changelog
%autochangelog
