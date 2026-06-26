%global source0_hash 20488ef3f15dd4f04d6225a44b5deb5525e39ba433142246aecfa4d9ec27ba81

%bcond_without check

Name:           python-pytest-datadir
Version:        1.8.0
Release:        1%{?dist}
Summary:        Pytest plugin for test data directories and files
License:        MIT
URL:            https://github.com/gabrielcnr/pytest-datadir
Source0:        https://github.com/gabrielcnr/pytest-datadir/archive/v%{version}/pytest-datadir-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
This package contains a pytest plugin for manipulating test data directories
and files.}

%description %_description

%package -n     python3-pytest-datadir
Summary:        %{summary}

%description -n python3-pytest-datadir %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n pytest-datadir-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_datadir

%if %{with check}
%check
%pyproject_check_import
%pytest
%endif

%files -n python3-pytest-datadir -f %{pyproject_files}
%doc AUTHORS README.md
%license LICENSE

%changelog
%autochangelog
