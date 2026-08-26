%global source0_hash 05b299a20058aca84f0d953977dd6463a053394d663ed3e71f4bccee3d0ab3e398214856c07b84184a0843f541e92ef8f89e5fdb11249914860bd717ac2c2aee
%global source1_hash 507546f508639abd56ff0451be062a7b872842decbc8860c4db09fa7c5854767d04a1c9acc90bb1d387cdc4a47c6edbf8d0f48ae02953bea9b57554134d36362

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpatch.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpatch.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-xpatch-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xpatch-doc <= 11:%{version}
Provides:       tex(xpatch.sty)

%description
Extending etoolbox patching commands.

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
%doc %{_texmf_main}/doc/latex/xpatch/
%{_texmf_main}/tex/latex/xpatch/

%changelog
%autochangelog
