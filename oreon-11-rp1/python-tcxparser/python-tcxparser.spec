%global source0_hash 692c525bcf07044cac2663cd7bc700a3b1368d05055b987ac83eb2efb8d1661a

%bcond_without tests

%global pretty_name tcxparser
%global pypi_name python-%{pretty_name}
%global extract_name python_tcxparser

%global _description %{expand:
python-tcxparser is a minimal parser for Garmin's TCX file format. It is not in
any way exhaustive. It extracts just enough data to show the most important
attributes of sport activity.}

Name:           python-%{pretty_name}
Version:        2.3.0
Release:        16%{?dist}
Summary:        Tcxparser is a minimal parser for Garmin TCX file format

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/vkurup/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist lxml}

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}

%description -n python3-%{pretty_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{pretty_name}

%check
%if %{with tests}
python3 -m unittest
%endif

%files -n python3-%{pretty_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst AUTHORS.rst CHANGES.rst

%changelog
%autochangelog
