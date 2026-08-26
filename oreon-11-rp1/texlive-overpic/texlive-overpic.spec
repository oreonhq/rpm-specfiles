%global source0_hash 1f065ad736fff812c7298c871ca2608c492b89688128ceba5cf31667eed98b49ba01fdc3b1ee6a44ec5a653ff6b29237936fc8154d0988594718100c9150c6ce
%global source1_hash 4089d5d57ed8c8d99c8dada0d7297b97b05ae0a914400d9ae68551080c3dbb3dc4294854db99e543e80f829cdf72dc6eb11b8d4f4d3487deec386fcbd7b8324f

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-overpic
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Combine LaTeX commands over included graphics
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/overpic.r79813.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/overpic.doc.r79813.tar.xz
BuildRequires:  tar
Provides:       texlive-overpic-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-overpic-doc <= 11:%{version}
Provides:       tex(overpic.sty)

%description
Combine LaTeX commands over included graphics.

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
%doc %{_texmf_main}/doc/latex/overpic/
%{_texmf_main}/tex/latex/overpic/

%changelog
%autochangelog
