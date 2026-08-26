%global source0_hash 030413280971d17decff54f02ac44749010eb127fa684033e811417e391eb84d
%global source1_hash 95c51411a1789104ae9af10578783078bda28e82216219d6e6b9d451a2b80b58

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ntheorem.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ntheorem.doc.r77682.tar.xz
BuildRequires:  tar
Provides:       texlive-ntheorem-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ntheorem-doc <= 11:%{version}
Provides:       tex(ntheorem.sty)

%description
Enhanced theorem environment.

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
%doc %{_texmf_main}/doc/latex/ntheorem/
%{_texmf_main}/tex/latex/ntheorem/

%changelog
%autochangelog
