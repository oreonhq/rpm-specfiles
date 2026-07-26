%global source0_hash f33ff8ea9a5f3e561a781fd844f549694c119677f07a97703d4c12b49a78f6d1

%global common_description %{expand:
mujson lets python libraries make use of the most performant JSON functions
available at import time.  It is small, and does not itself implement any
encoding or decoding functionality.}

Name:           python-mujson
Version:        1.4
Release:        20%{?dist}
Summary:        Use the fastest JSON functions available at import time
License:        MIT
URL:            https://github.com/mattgiles/mujson
# PyPI tarball is missing license
# https://github.com/mattgiles/mujson/issues/8
Source:         %{url}/archive/%{version}/mujson-%{version}.tar.gz
BuildArch:      noarch

%description %{common_description}

%package -n python3-mujson
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-mujson %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n mujson-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mujson

%check
%pyproject_check_import

%files -n python3-mujson -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
