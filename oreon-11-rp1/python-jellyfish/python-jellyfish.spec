%global source0_hash 0f994e4e67cb674fc181e2d25c6959170bfd074b6261828921b7e4debe1d0a6d

%global realname jellyfish
# Share doc between python-jellyfish and python3-jellyfish
%global _docdir_fmt %{name}

Name:           python-%{realname}
Version:        0.9.1
Release:        16%{?dist}
Summary:        A python library for doing approximate and phonetic matching of strings

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/jamesturk/%{realname}
Source0:        https://github.com/jamesturk/%{realname}/archive/v%{version}.tar.gz
# git repo is here https://github.com/jamesturk/jellyfish-testdata.git
# tgz created with: git archive HEAD -o jellyfish-testdata-20160204.tgz
Source1:        jellyfish-testdata-20200727.tgz
# We do not use the C binding so we just install everything in site_lib
Patch0:         fix-build.patch
# The following two patches are needed because we do not ship any C implementation so we manually
# disable the tests that check for this C version
Patch1:         test-only-python-implementation.diff
Patch2:         nocimplementation-fix-0.9.1.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description\
Jellyfish does approximate and phonetic string matching. It\
includes the following string comparison algorithms:\
Levenshtein Distance, Damerau-Levenshtein Distance,\
Jaro Distance, Jaro-Winkler Distance, Match Rating Approach\
Comparison and Hamming Distance\
\
And the following phonetic encodings:\
American Soundex, Metaphone, NYSIIS (New York State Identification\
and Intelligence System), Match Rating Codex

%description %_description

%package -n python3-%{realname}
Summary:        A python library for doing approximate and phonetic matching of strings

%description -n python3-%{realname} %{_description}

Python 3 Version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{realname}-%{version} -p1
tar xf %{SOURCE1} -C testdata

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{realname}

%check
%pyproject_check_import

# testdata is here: https://github.com/jamesturk/jellyfish-testdata.git
PYTHONPATH=. pytest-3 jellyfish/test.py

%files -n python3-%{realname} -f %{pyproject_files}
%doc README.md docs/

%changelog
%autochangelog
