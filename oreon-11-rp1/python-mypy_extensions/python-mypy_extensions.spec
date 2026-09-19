%global source0_hash 52e68efc3284861e772bbcd66823fde5ae21fd2fdb51c62a211403730b916558

%global srcname mypy_extensions

Name:           python-%{srcname}
Version:        1.1.0
Release:        6%{?dist}
Summary:        Extensions for mypy (separated out from mypy/extensions)

License:        MIT
URL:            https://github.com/python/mypy_extensions
Source:         %{pypi_source}

BuildArch:      noarch

%global _description \
The "mypy_extensions" module defines experimental extensions to the standard\
"typing" module that are supported by the mypy typechecker.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
rm -vrf *.egg-info/

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
