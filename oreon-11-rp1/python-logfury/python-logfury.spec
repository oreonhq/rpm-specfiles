%global source0_hash 130a5daceab9ad534924252ddf70482aa2c96662b3a3825a7d30981d03b76a26

Name:           python-logfury
Version:        1.0.1
Release:        20%{?dist}
Summary:        Library for logging of method calls for Python

License:        BSD-3-Clause
URL:            https://github.com/ppolewicz/logfury
Source0:        %{pypi_source logfury}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools_scm

Patch0:         relax-setuptools_scm.patch

%description
%{summary}.

%package -n python3-logfury
Summary: %{summary}

%description -n python3-logfury
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n logfury-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l logfury

%check
%pyproject_check_import

%files -n python3-logfury -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.rst

%changelog
%autochangelog
