%global source0_hash none

# what it's called on pypi
%global srcname pyjwt
# what it's imported as
%global libname jwt
# package name fragment
%global pkgname %{libname}

%global common_description %{expand:
A Python implementation of JSON Web Token draft 01. This library provides a
means of representing signed content using JSON data structures, including
claims to be transferred between two parties encoded as digitally signed and
encrypted JSON objects.}


Name:           python-%{pkgname}
Version:        2.10.1
Release:        3%{?dist}
Summary:        JSON Web Token implementation in Python
License:        MIT
URL:            https://github.com/jpadilla/pyjwt
Source:         %pypi_source
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
Recommends:     python3-%{pkgname}+crypto


%description -n python3-%{pkgname} %{common_description}


%pyproject_extras_subpkg -n python3-%{pkgname} crypto


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{srcname}-%{version}
# remove coverage buildreq and relax pytest req
sed -e '/coverage\[toml\]/d' \
    -e '/pytest/ s/,<7.0.0//' \
    -i pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x crypto,tests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{libname}


%check
%pytest -k 'not (test_ec_to_jwk_with_invalid_curve or test_get_jwt_set_sslcontext_default)'


%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.rst


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.10.1-3
- Prepare for Oreon 11 (RP1)
