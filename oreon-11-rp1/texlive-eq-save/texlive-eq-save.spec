%global source0_hash a7f586060a95044a638f3138e6446c895a95af8481ce67c94e7f9319892ea7ad

%global tl_version 2025
%global revision 299

# eq-save is part of texlive, but it lives in their contrib archive.
# ... but stuff in texlive still depends on it, so I've packaged it.
# Epoch inherits from texlive for consistency.

Name:           texlive-eq-save
Epoch:          12
Version:        svn%{revision}
Release:        2%{?dist}
Summary:        Save exerquiz quizzes and resume
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlcontrib/archive/eq-save.tar.xz
Source1:	https://ctan.math.illinois.edu/systems/texlive/tlcontrib/archive/eq-save.doc.tar.xz
# License texts
Source2:        texlive-licenses.tar.xz

BuildRequires:  texlive-base
Provides:	tex(eq-save.sty) = %{tl_version}
Requires:       texlive-base
Requires:	texlive-kpathsea
Requires:	tex(exerquiz.sty)
Requires:	tex(atbegshi.sty)

%description
The package has a scheme for saving data from exerquiz
documents so the student can return later to continue with quiz
results restored.

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
%{_texmf_main}/tex/latex/eq-save/
%doc %{_texmf_main}/doc/latex/eq-save/

%changelog
%autochangelog
