%global source0_hash 5821a7933f075fb47563417c0e92e0b7c031158b4c9a6a7e56163479b658b368
%bcond_without tests
%global pypi_name dotmap
Name:           python-%{pypi_name}
Version:        1.3.30
Release:        1%{?dist}
Summary:        Dot access dictionary with dynamic hierarchy creation and ordered iteration
License:        MIT
URL:            https://github.com/drgrib/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/d/dotmap/dotmap-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dotmap = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{pypi_name}
Summary:        Dot access dictionary with dynamic hierarchy creation and ordered iteration
BuildRequires:  make
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif
%description -n python3-%{pypi_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/dotmap* usr/lib64/python3*/site-packages/dotmap* usr/bin/*

%check

%if %{with tests}
python3 -m unittest
%endif
%license LICENSE.txt
%doc README.md
%files
%files -n python3-dotmap -f %{oreon_filedir}/python3-dotmap.list

%changelog

%autochangelog
