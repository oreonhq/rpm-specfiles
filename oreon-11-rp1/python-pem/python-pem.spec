%global source0_hash db25c38b857edba2e8e41e1c1f4086011f2a8e2598c8aa190e05e9425da9c829

# tests are enabled by default
%bcond_without tests

%global         srcname     pem
%global         forgeurl    https://github.com/hynek/pem
Version:        23.1.0
%global         tag         %{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Easy PEM file parsing

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

%if 0%{?rhel}
# Patch out the fancy pypi readme module from the requirements in EPEL.
# See BZ 2303831.
Patch0:         remove-fancy-pypi-readme.patch 
%endif

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pretend)
BuildRequires:  python3dist(pyopenssl)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(service-identity)
BuildRequires:  python3dist(twisted)
%endif

%global _description %{expand:
pem is an MIT-licensed Python module for parsing and splitting of PEM files,
i.e. Base64-encoded DER keys and certificates.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pem

%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
%autochangelog
