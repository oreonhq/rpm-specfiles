%global source0_hash 84cd6ebf447ccaa39c23956674de1b540dfbc2e3eb7f601f36265c8c92b3abed

%global srcname aaargh
%global desc \
Aaargh is a Python module that makes building friendly command line\
applications really easy. Applications built with Aaargh provide\
a single executable with a subcommand for each exposed Python function.\
Each subcommand may have its own command line arguments.\
This is similar to the way version control systems provide multiple commands\
using a single entry point.

Name:           python-%{srcname}
Version:        0.7.1
Release:        35%{?dist}
Summary:        An astonishingly awesome application argument helper

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/wbolster/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description %{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-%{srcname} %{desc}
Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import
py.test-3 -v

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
