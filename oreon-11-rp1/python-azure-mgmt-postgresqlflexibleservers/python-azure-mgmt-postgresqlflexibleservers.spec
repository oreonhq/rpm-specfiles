%global source0_hash 13d2f45ba218a364fb0405684f8070f261ae3ed597d5a54d04e3298732c4cdaa

%global         srcname         azure-mgmt-postgresqlflexibleservers
%global         tarball_name    azure_mgmt_postgresqlflexibleservers

Name:           python-%{srcname}
Version:        2.0.0
%global         pypi_version    2.0.0
Release:        %autorelease
Summary:        The Microsoft Azure Postgresqlflexibleservers Management Client Library
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{tarball_name} %{pypi_version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This is the Microsoft Azure Postgresqlflexibleservers Management Client Library.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{tarball_name}-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l azure

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
