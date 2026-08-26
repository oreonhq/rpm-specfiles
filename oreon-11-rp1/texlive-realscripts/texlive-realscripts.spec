%global source0_hash 7cc319f1655044a9c5396740180b30b4cae94cc8d6d37b7ef547ee6ae8c7e8e7c394764fda0cce2e31c7c9449f7f4587e06e7c4f6c20ca31e92f69708fd4fe4e
%global source1_hash a8a4d06974f46b4918d6fc86b5543a2af089f97b2553a26c532f6000ea135979c5ee2fd09d9ffc858c2440a3d2f237da149e4eaa79bb6d33f1f02afc31a583e8

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-realscripts
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Access OpenType subscript and superscript glyphs
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/realscripts.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/realscripts.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-realscripts-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-realscripts-doc <= 11:%{version}
Provides:       tex(realscripts.sty)

%description
Access OpenType subscript and superscript glyphs.

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
%doc %{_texmf_main}/doc/latex/realscripts/
%{_texmf_main}/tex/latex/realscripts/

%changelog
%autochangelog
