%global source0_hash 4d9debb8b99007ae47165abc08670bd74cb74b5227dda7f643eccc4e9eb5642c

%global srcname smmap

Name:           python-%{srcname}
Version:        5.0.3
Release:        1%{?dist}
Summary:        Sliding window memory map manager

License:        BSD-3-Clause
URL:            https://github.com/gitpython-developers/smmap
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

%global _description %{expand:
Smmap wraps an interface around mmap and tracks the mapped files as well as
the amount of clients who use it. If the system runs out of resources,
or if a memory limit is reached, it will automatically unload unused maps
to allow continued operation.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
