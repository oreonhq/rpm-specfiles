%global source0_hash a30bd361ac18c8b52f6844076bc26465335949ea9c7a004d95f5196ec6fdef3e

%global         srcname         microsoft-security-utilities-secret-masker
%global         tarball_name    microsoft_security_utilities_secret_masker

Name:           python-%{srcname}
Version:        1.0.0~b4
%global         pypi_version    1.0.0b4
Release:        %autorelease
Summary:        Microsoft Security Utilities - Secret Masker
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{tarball_name} %{pypi_version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
The Secret Masker Python library focuses on:

  - providing some built-in detection rules in json format
  - detecting sensitive data for given input
  - masking sensitive data with simple symbols or sha256 hash for given input}

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
%pyproject_save_files %{tarball_name}

%check
%pyproject_check_import
# Sadly there's no tests in the PyPI package and no git repository.

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst HISTORY.rst
%license LICENSE

%changelog
%autochangelog
