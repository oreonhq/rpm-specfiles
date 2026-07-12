%global source0_hash 6c9ab42ce4d8b73162100112bfd1972537c629421a60aaa782630ccc4f9c0d0f
%global source1_hash 824313e23a2e678442fa98e2478db87e5afea3e7b7d946d939b1a276743af3de

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/undolabl.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/undolabl.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-undolabl-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-undolabl-doc <= 11:%{version}
Provides:       tex(undolabl.sty)

%description
Override existing labels.

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
%doc %{_texmf_main}/doc/latex/undolabl/
%{_texmf_main}/tex/latex/undolabl/

%changelog
%autochangelog
