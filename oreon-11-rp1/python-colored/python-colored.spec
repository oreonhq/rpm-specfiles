%global source0_hash e727d9c76aa6811ebf8e68fbe5eb4488e3c6b89082703cfe68c6765050301f54

Name:           python-colored
Version:        2.2.4
Release:        11%{?dist}
Summary:        Library for color and formatting in terminal

License:        MIT
URL:            https://gitlab.com/dslackw/colored
Source:         https://gitlab.com/dslackw/colored/-/archive/%{version}/colored-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Very simple Python library for color and formatting in terminal.
Collection of color codes and names for 256 color terminal setups.}

%description %_description

%package -n python3-colored
Summary:        %{summary}

%description -n python3-colored %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n colored-%{version}
# remove shebangs
sed -i '/#!\/usr\/bin\/env python/d' colored/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files colored

%check
# tests from upstream appear to be incomplete and/or things that must be run manually.
%pyproject_check_import colored

%files -n python3-colored -f %{pyproject_files}
%doc README.* CHANGES.md

%changelog
%autochangelog
