%global source0_hash 692c525bcf07044cac2663cd7bc700a3b1368d05055b987ac83eb2efb8d1661a
%bcond_without tests
%global pretty_name tcxparser
%global pypi_name python-%{pretty_name}
%global extract_name python_tcxparser
Name:           python-%{pretty_name}
Version:        2.3.0
Release:        1%{?dist}
Summary:        Tcxparser is a minimal parser for Garmin TCX file format
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/vkurup/%{pypi_name}
Source0:        https://github.com/vkurup/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-tcxparser = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{pretty_name}
Summary:        Tcxparser is a minimal parser for Garmin TCX file format
%description -n python3-%{pretty_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/tcxparser* usr/lib64/python3*/site-packages/tcxparser* usr/bin/*

%check

%if %{with tests}
python3 -m unittest
%endif
%files
%files -n python3-tcxparser -f %{oreon_filedir}/python3-tcxparser.list

%changelog

%autochangelog
