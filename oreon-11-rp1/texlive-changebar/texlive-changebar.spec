%global source0_hash b53ea53e6f01a674f1ff28275be0b504f8a96b8a89c85de7dd5a87cbbdf8d42e
%global source1_hash ad8f1294623a19d0877381bd78f83562813e918e578aaf8b52662c210e3a04a7

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-changebar
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Generate changebars in LaTeX documents
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/changebar.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/changebar.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-changebar-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-changebar-doc <= 11:%{version}
Provides:       tex(changebar.sty)

%description
Generate changebars in LaTeX documents.

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
%doc %{_texmf_main}/doc/latex/changebar/
%{_texmf_main}/tex/latex/changebar/

%changelog
%autochangelog
