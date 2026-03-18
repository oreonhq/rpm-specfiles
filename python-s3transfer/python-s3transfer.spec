%global srcname s3transfer
%global _description \
S3transfer is a Python library for managing Amazon S3 transfers.

Name:           python-%{srcname}
Version:        0.16.0
Release:        2%{?dist}
Summary:        Amazon S3 Transfer Manager

License:        Apache-2.0
URL:            https://pypi.org/project/s3transfer/
Source0:        %{pypi_source}

BuildArch:      noarch

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
# required to run the test suite
BuildRequires:  python3dist(botocore) >= 1.12.36
BuildRequires:  python3dist(botocore) < 2.0
BuildRequires:  python3dist(pytest)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest tests/unit tests/functional

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16.0-2
- Prepare for Oreon 11 (RP1)
