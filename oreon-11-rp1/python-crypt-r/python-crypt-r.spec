%global source0_hash none

Name:           python-crypt-r
Version:        3.13.1
Release:        %autorelease
Summary:        A copy of the `crypt` module that was removed in Python 3.13

License:        Python-2.0.1
URL:            https://github.com/fedora-python/crypt_r
Source:         %{pypi_source crypt_r}

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  libxcrypt-devel


%global _description %{expand:
The crypt_r module is a renamed copy of the crypt module as it was present in
Python 3.12 before it was removed.

See PEP 594 for details of the removal.

Unlike crypt, this library always exposes the crypt_r(3) function, not crypt(3).

This module implements an interface to the crypt_r(3) routine, which is
a one-way hash function based upon a modified DES algorithm; see the Unix man
page for further details. Possible uses include storing hashed passwords so you
can check passwords without storing the actual password, or attempting to crack
Unix passwords with a dictionary.}

%description %_description

%package -n     python3-crypt-r
Summary:        %{summary}

%description -n python3-crypt-r %_description


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n crypt_r-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l _crypt_r crypt_r crypt


%check
# from tox.ini:
%{py3_test_envvars} %{python3} tests/test_crypt_r.py


%files -n python3-crypt-r -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog

