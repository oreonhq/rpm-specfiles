%global source0_hash 2fba2fa8ed8c4b85e227c5dd7dc41c7d658de3b6f247927316175a57349b84d1

%global         srcname     multitasking

Name:           python-%{srcname}
Version:        0.0.12
Release:        %autorelease
Summary:        Non-blocking Python methods using decorators
License:        Apache-2.0
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
MultiTasking is a tiny Python library lets you convert your Python methods
into asynchronous, non-blocking methods simply by using a decorator.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# Remove the python shebang from non-executable files.
sed -i '1{\@^#!/usr/bin/env python@d}' multitasking/__init__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
