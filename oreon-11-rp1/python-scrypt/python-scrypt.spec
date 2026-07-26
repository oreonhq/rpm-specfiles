%global source0_hash a7b637848ed518c1ea2b31a9ecaaa3f49616598d8442de8706cf1f01fbabf0a7

Name:           python-scrypt
Version:        0.8.27
Release:        7%{?dist}
Summary:        Python bindings for the scrypt key derivation function

License:        BSD-2-Clause
URL:            https://github.com/holgern/py-scrypt
Source0:        %{pypi_source scrypt}

BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Scrypt is useful when encrypting password as it is possible to specify
a minimum amount of time to use when encrypting and decrypting.
If, for example, a password takes 0.05 seconds to verify, a user won't notice
the slight delay when signing in, but doing a brute force search of several
billion passwords will take a considerable amount of time. This is in contrast
to more traditional hash functions such as MD5 or the SHA family which can be
implemented extremely fast on cheap hardware.}

%description %_description

%package -n     python3-scrypt
Summary:        Bindings for the scrypt key derivation function library
Provides:       bundled(scrypt) = 1.2.1

%description -n python3-scrypt %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n scrypt-%{version}
# remove useless shebang
sed -i '1d' scrypt/scrypt.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '_scrypt*' scrypt

%check
%pyproject_check_import

%{pytest}

%files -n python3-scrypt -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
