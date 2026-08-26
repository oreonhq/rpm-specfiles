%global source0_hash 26faae5989ce0b1d2f1dedafc3d9c43f86de8a37f0c0ee1a0ed05d4d23e43c0a3dffcd15a64799ff1dacffe69e1c4283cadbfd5e418e25ebbe900f432517e0c0
%global source1_hash 1b44781faf2fe617b805ba672a203dc93942acceff5c274e61c9a47e3b8d9bb9fc8258d9fd1eb89ff3dcc2496b0b17a33dfb63c7e1f197be0283313a916bfc1c

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
