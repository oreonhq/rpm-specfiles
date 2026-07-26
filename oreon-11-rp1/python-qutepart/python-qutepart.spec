%global source0_hash cc44161275de68f453e769e58a9a46e83aa7f1319d05b18e5a18c2a88e64756c

%global srcname     qutepart
%global sum         Code editor widget
%global desc_common \
Qutepart is a code editor widget for PyQt. Features: \
    - Syntax highlighting for 196 languages. \
    - Smart indentation for many languages. \
    - Line numbers. \
    - Bookmarks. \
    - Advanced edit operations. \
    - Matching braces highlighting. \
    - Autocompletion based on document content. \
    - Marking too long lines with red line. \
    - Rectangular selection and copy-paste. \
    - Linter marks support.

# issue#69, tests for vim abort with python 3.7, maybe too slow?
%bcond_with     test_vim

Name:           python-%{srcname}
Version:        3.3.3
Release:        17%{?dist}
Summary:        %{sum}

# LGPL 2.1 >> 2.0 (explicitly allows dynamic linking)
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/andreikop/%{srcname}

Source0:        %{url}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
# https://github.com/andreikop/qutepart/issues/96
# Handle PEP623, forced on python3.12
Patch0:         qutepart-3.3.3-pep623.patch

BuildRequires:  gcc
BuildRequires:  pcre-devel

BuildRequires:  python3-qt5
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx

BuildRequires:  xorg-x11-server-Xvfb

%description
%{desc_common}

%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       pcre
Requires:       python3-qt5
Provides:       python-%{srcname}
Obsoletes:      python2-%{srcname} < 3.2.0

%description -n python3-%{srcname}
%{desc_common}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}
%patch -P0 -p1
# disable PyQt5 mocking for sphinx
sed -i -r 's,(MOCK_MODULES = \[).*\],\1],' doc/source/conf.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd doc
sphinx-build-3 source html
# E: non-standard-executable-perm
#find -name \*.so |xargs chmod 0755
# W: hidden-file-or-dir
rm -r html/.buildinfo html/.doctrees

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import

# let's find all modules and don't crash after execution
pushd tests
rm -f test_all.py
%if !%{with test_vim}
# FIXME (core dumped)
rm test_vim.py
%endif
# FIXME we saw crashes with python3 = 3.9, rhbz#1793009
%if 0%{?python3_version_nodots} > 38
true Skipping tests due to strange crashes! Python: %{python3_version_nodots} / %{?python3_pkgversion}
%else
# test_all.py: Look for all tests. Using test_* instead of
# test_*.py finds modules (test_syntax and test_indenter).
# Do some fake X
xvfb-run -s '-screen :0 1024x768x16'\
 %{__python3} -m unittest -vvv test_*
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md ChangeLog todo.txt
%doc doc/html/

%changelog
%autochangelog
