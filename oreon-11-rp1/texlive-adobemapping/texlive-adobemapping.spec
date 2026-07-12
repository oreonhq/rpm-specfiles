%global source0_hash a387389a11bd1220be3016ef74342bb9a4e1e888cee21379f3aadac786da1da1
%global source1_hash none

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-adobemapping
Epoch:          12
Version:        svn66552
Release:        1%{?dist}
Summary:        Adobe CMap resources for CJK fonts
License:        BSD
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adobemapping.tar.xz
BuildRequires:  tar
Provides:       texlive-adobemapping-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-adobemapping-doc <= 11:%{version}
Provides:       texlive-adobemapping = %{epoch}:%{version}-%{release}

%description
Adobe CMap resources for CJK fonts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || true

%build

%install
mkdir -p %{buildroot}%{_texmf_main}
tar -xf %{SOURCE0} -C %{buildroot}%{_texmf_main}
rm -rf %{buildroot}%{_texmf_main}/tlpkg

%files
%{_texmf_main}/fonts/cmap/adobemapping/

%changelog
%autochangelog
