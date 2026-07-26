%global source0_hash 97aacf9dbd4bfd829baad6e6309fa6573aaf1be3f6fa735c8ab05e46cecb261c

# Created by pyp2rpm-1.1.0b

%global pypi_name rfc3986
%global common_description %{expand:
A Python implementation of RFC 3986 including validation and authority parsing.}

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        6%{?dist}
Summary:        Validating URI References per RFC 3986

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://rfc3986.readthedocs.io
Source0:        %pypi_source
BuildArch:      noarch

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%description -n python3-%{pypi_name} %{common_description}

%pyproject_extras_subpkg -n python3-%{pypi_name} idna2008

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x idna2008

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
