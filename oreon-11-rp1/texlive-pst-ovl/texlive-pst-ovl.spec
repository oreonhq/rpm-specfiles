%global source0_hash ef9f3364fc9b523f8b1d87cd013d90a85fcc1af53042d3e8614fa295c1710a1a61dbfa2356ffc0f857551bcc99db448fe7f4684bb348e7095b4189d586ef571b
%global source1_hash c1842c80d82f02f13cd76e11c7a5eba5906b535761093ef1a03bcf9236d0885ebae14b0be12ecb05a7f8dc5ed22eda8463670203dbf080e0656d208a13d3d1e8

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-pst-ovl
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Overlay macros for PSTricks
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-ovl.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-ovl.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-pst-ovl-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pst-ovl-doc <= 11:%{version}
Provides:       tex(pst-ovl.sty)
Provides:       tex(pst-ovl.tex)

%description
Overlay macros for PSTricks.

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
%doc %{_texmf_main}/doc/generic/pst-ovl/
%{_texmf_main}/dvips/pst-ovl/
%{_texmf_main}/tex/generic/pst-ovl/
%{_texmf_main}/tex/latex/pst-ovl/

%changelog
%autochangelog
