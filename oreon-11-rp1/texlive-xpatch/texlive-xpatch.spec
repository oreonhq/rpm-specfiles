%global source0_hash 4ad016952188a1e822871242ebbb6fb4ea1eb0041a7fd7e50fe87d9d001bb7c3
%global source1_hash 324de7e91bd860b51180c566836933943af903b19fe2cf7f01e6af84624da22c

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-xpatch
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Extending etoolbox patching commands
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpatch.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpatch.doc.r77682.tar.xz
BuildRequires:  tar
Provides:       texlive-xpatch-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xpatch-doc <= 11:%{version}
Provides:       tex(xpatch.sty)

%description
Extending etoolbox patching commands.

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
%doc %{_texmf_main}/doc/latex/xpatch/
%{_texmf_main}/tex/latex/xpatch/

%changelog
%autochangelog
