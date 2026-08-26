%global source0_hash 469cb75a3d37250331e717f591dce665b2d704ec491f6da238bfbcb137da94615ce94edd00c2d699ade97e4f7a50b4d4ca4e78f90b654e8123193f22594026f8
%global source1_hash 3b87f97b46fa88a090535dd0182f15b1be20dc0575b68175b7eda721ab67c207cfe354f9f7dc3fa47393a33b415f8251c315ae09596e8d497057a6ee25b25ffa

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/svn-prov.r79618.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/svn-prov.doc.r79618.tar.xz
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
