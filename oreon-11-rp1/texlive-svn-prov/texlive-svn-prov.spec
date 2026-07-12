%global source0_hash 74cf47446fd3ebe606dd944f16133571e79c15f85b7223bf5e5eed5692fb74b8
%global source1_hash 6e87986460ee9f003bd693ade233383b105d2e8de08c48aa28c0d43ad9926470

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-svn-prov
Epoch:          12
Version:        svn79618
Release:        1%{?dist}
Summary:        Subversion keywords as package macros
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/svn-prov.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/svn-prov.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-svn-prov-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-svn-prov-doc <= 11:%{version}
Provides:       tex(svn-prov.sty)

%description
Subversion keywords as package macros.

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
%doc %{_texmf_main}/doc/latex/svn-prov/
%{_texmf_main}/tex/latex/svn-prov/

%changelog
%autochangelog
