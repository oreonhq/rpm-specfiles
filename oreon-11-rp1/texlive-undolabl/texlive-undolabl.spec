%global source0_hash 5a72b1ed0a016c07f159461a6dc874226f6cf48dffc913ff4392debe49dd34a6809bad46a660eb27cc16d32584adb69ac8521fa86c3252aac5ab1ab5d8b68b28
%global source1_hash ad5eeea49dee85151648870c27302e9aaf2ed3fcf1ce6fcf69aec3f74c3009bb0f6f7bb2b775083e8ef39fc250b7080475d01067b70b88fbff27c810bb77d9c7

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-undolabl
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Override existing labels
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/undolabl.tar.xz#/undolabl.or11.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/undolabl.doc.tar.xz#/undolabl.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-undolabl-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-undolabl-doc <= 11:%{version}
Provides:       tex(undolabl.sty)

%description
Override existing labels.

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
%doc %{_texmf_main}/doc/latex/undolabl/
%{_texmf_main}/tex/latex/undolabl/

%changelog
%autochangelog
