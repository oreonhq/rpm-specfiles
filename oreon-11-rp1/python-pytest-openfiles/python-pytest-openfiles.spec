%global source0_hash ff5160c34eaada82b983a2c316fcccb30e0094630e97784471f015956870a993

%global srcname pytest-openfiles
%global upname pytest_openfiles
%global sum The py.test openfiles plugin

Name:           python-%{srcname}
Version:        0.6.0
Release:        11%{?dist}
Summary:        %{sum}

# Note, this package is not actively developed
# Retirement roadmap:
# https://pypi.org/project/pytest-openfiles/#description

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{upname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
The pytest-openfiles plugin allows for the detection of open I/O resources at
the end of unit tests. This is particularly useful for testing code that
manipulates file handles or other I/O resources. It allows developers to
ensure that this kind of code properly cleans up I/O resources when they are
no longer needed.

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
The pytest-openfiles plugin allows for the detection of open I/O resources at
the end of unit tests. This is particularly useful for testing code that
manipulates file handles or other I/O resources. It allows developers to
ensure that this kind of code properly cleans up I/O resources when they are
no longer needed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pytest_openfiles

%check
%pyproject_check_import -t

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst

%changelog
%autochangelog
