%global source0_hash 5b297f364f5343fd199baaea9006465f98bdddd937f385f168e5237fc9816c2b

%global tl_version 2025
%global revision 362

# mathtime-ltx is part of texlive, but it lives in their contrib archive.
# ... but stuff in texlive still depends on it, so I've packaged it.
# Epoch inherits from texlive for consistency.

Name:           texlive-mathtime-ltx
Epoch:          12
Version:        svn%{revision}
Release:        2%{?dist}
Summary:        LaTeX macros for using MathTime and MathTime Plus
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlcontrib/archive/mathtime-ltx.r362.tar.xz
Source1:	https://ctan.math.illinois.edu/systems/texlive/tlcontrib/archive/mathtime-ltx.doc.r362.tar.xz
# License texts
Source2:        texlive-licenses.tar.xz

BuildRequires:  texlive-base
Provides:	tex(mathpi.sty) = %{tl_version}
Provides:	tex(mathtime.sty) = %{tl_version}

Requires:       texlive-base
Requires:	texlive-kpathsea

%description
LaTeX macros for using MathTime and MathTime Plus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Extract license files
tar -xf %{SOURCE2}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_texmf_main}

tar -xf %{SOURCE0} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE1} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

%files
%license lppl.txt
%{_texmf_main}/tex/latex/mathtime-ltx/
%{_texmf_main}/fonts/enc/dvips/mathtime-ltx/
%doc %{_texmf_main}/doc/latex/mathtime-ltx/

%changelog
%autochangelog
