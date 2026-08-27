%global source0_hash 161f156bc9b96a06adc6083c4a9a64f38b91a712ecc6bcd8efe3c2d0cb08c1b5c261abe05856bd781baa0a92c86ffdb0e9b0631bc500447c33359fcefdd88cea

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
%global source1_hash 83aaa87b0d21a16c13b18faacaf353d9ab8fcffd638148209824e05219e8c4eb804caf1c9dc8f73abfea632130b730da1dfb30cf6c89475093d6c0e2ff9843ad

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlcontrib/archive/eq-save.tar.xz#/eq-save.or11.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlcontrib/archive/eq-save.doc.tar.xz#/eq-save.doc.or11.tar.xz
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
