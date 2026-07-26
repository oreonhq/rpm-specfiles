%global source0_hash aeac9f43e0ea97830bed69cb309ad5746b5ed2b9dce733ac4c136c8e16a7d6e5

%global pypi_name django-debreach

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        16%{?dist}
Summary:        Basic/extra mitigation against the BREACH attack for Django projects

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://github.com/lpomfrey/django-debreach
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Basic/extra mitigation against the BREACH attack for Django projects.

When combined with rate limiting in your web-server, or by using something
like django-ratelimit, the techniques here should provide at least some
protection against the BREACH attack.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3dist(django) >= 2.0
%description -n python3-%{pypi_name}
Basic/extra mitigation against the BREACH attack for Django projects.

When combined with rate limiting in your web-server, or by using something
like django-ratelimit, the techniques here should provide at least some
protection against the BREACH attack.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files debreach

%check
PYTHONPATH=. %{__python3} runtests.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
