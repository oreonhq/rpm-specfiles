%global source0_hash c41817426c3eaa04617d4cde03164700c77daeee6a47279a5d686481e67e9c4f
%global source1_hash 457b8632eb8c0ca73e72cd0169938c17879a843bd916e5f8a98476122dede637

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-epsf
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Simple macros for EPS inclusion
License:        Public Domain
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epsf.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epsf.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-epsf-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-epsf-doc <= 11:%{version}
Provides:       tex(epsf.sty)
Provides:       tex(epsf.tex)

%description
Simple macros for EPS inclusion.

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
%license %{_texmf_main}/doc/generic/epsf/LICENSE
%doc %{_texmf_main}/doc/generic/epsf/
%{_texmf_main}/tex/generic/epsf/
%exclude %{_texmf_main}/doc/generic/epsf/LICENSE

%changelog
%autochangelog
