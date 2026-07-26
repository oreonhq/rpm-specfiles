%global source0_hash 60ea0036a5514e2610e5bf561586f324e75ffd91a7209f5fb9e06b8fe28b06bb

%global srcname sievelib

Name:           python-%{srcname}
Version:        1.4.2
Release:        7%{?dist}
Summary:        Client-side SIEVE library
License:        MIT
URL:            https://github.com/tonioo/sievelib
Source0:        %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Client-side Sieve and Managesieve library written in Python.
* Sieve : An Email Filtering Language (RFC 5228).
* ManageSieve : A Protocol for Remotely Managing Sieve Scripts (RFC 5804).}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
# remove bundled egg-info
rm -rf %{srcname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sievelib

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license COPYING

%changelog
%autochangelog
