%global source0_hash ac6397369f128212c43064a2b4878038dab78dab41875364554aaf2a684e6979

Name:      python-pbkdf2
Version:   1.3
Release:   39%{?dist}
Summary:   A module for a password-based key derivation function

License:   MIT
URL:       https://www.dlitz.net/software/python-pbkdf2/
Source0:   %{pypi_source pbkdf2}
Patch1:    pbkdf2-license.patch
Patch2:    pbkdf2-remove-shebang.patch

BuildArch:     noarch
BuildRequires: python3-devel

%global _description %{expand:
A pure Python Implementation of the password-based key derivation function,
PBKDF2, specified in RSA PKCS#5 v2.0.}

%description %_description

%package -n python3-pbkdf2
Summary: %{summary}

%description -n python3-pbkdf2 %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pbkdf2-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pbkdf2

%check
%pyproject_check_import

%{python3} -m unittest test/*

%files -n python3-pbkdf2 -f %{pyproject_files}
%doc README.txt

%changelog
%autochangelog
