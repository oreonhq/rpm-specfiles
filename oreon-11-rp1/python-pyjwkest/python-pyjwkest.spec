%global source0_hash 5560fd5ba08655f29ff6ad1df1e15dc05abc9d976fcbcec8d2b5167f49b70222

Name:           python-pyjwkest
Version:        1.4.2
Release:        12%{?dist}
Summary:        Python implementation of JWT, JWE, JWS and JWK

# pyjwkest: Apache-2.0
# src/jwkest/aes_gcm.py: MIT
# src/jwkest/PBKDF2.py: MIT
License:        Apache-2.0 AND MIT
URL:            https://github.com/IdentityPython/pyjwkest
Source:         %{pypi_source pyjwkest}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand: 
Python implementation of JWT, JWE, JWS and JWK, which is used by pyoidc.}

%description %_description

%package -n     python3-pyjwkest
Summary:        %{summary}

%description -n python3-pyjwkest %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pyjwkest-%{version}
# The project does not need future anymore
# https://github.com/IdentityPython/pyjwkest/issues/102
sed -i 's/, "future"//' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files 'jwkest' +auto

%check
%pyproject_check_import -t

%files -n python3-pyjwkest -f %{pyproject_files}

%changelog
%autochangelog
