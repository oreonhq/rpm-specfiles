%global source0_hash 006535e22fed944aec17bef6e8725472476194743c87bd233e912eb463f8ff05

%global srcname voluptuous

Name:      python-%{srcname}
Version:   0.16.0
Release:   %autorelease
Summary:   Python data validation library

License:   BSD-3-Clause
URL:       http://github.com/alecthomas/voluptuous
Source0:   %{pypi_source}
BuildArch: noarch

%global _description %{expand:
Voluptuous, despite the name, is a Python data validation library. It is 
primarily intended for validating data coming into Python as JSON, YAML, etc.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: python3-devel
BuildRequires: %{py3_dist setuptools}
BuildRequires: %{py3_dist pytest}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files voluptuous

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license COPYING

%changelog
%autochangelog
