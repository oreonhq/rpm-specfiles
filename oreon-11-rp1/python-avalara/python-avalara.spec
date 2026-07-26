%global source0_hash 00e632202e60b8fc8e8aff6e604eb31167851bb2ab285ed114335bfc2fe8d1a6

%global srcname AvaTax-REST-V2-Python-SDK
%global pkgname avalara

Name:           python-avalara
Version:        25.12.0
Release:        7%{?dist}
Summary:        AvaTax Python SDK

License:        Apache-2.0
URL:            https://github.com/avadev/%{srcname}
Source0:        https://github.com/avadev/%{srcname}/archive/refs/tags/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Sales Tax API SDK for Python and AvaTax REST.}

%description %_description

%package -n python3-%{pkgname}
Summary: %{summary}

%description -n python3-%{pkgname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pkgname}

%check
%pyproject_check_import
# Not running tests here as they require you to have an account and an internet connection.

%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
