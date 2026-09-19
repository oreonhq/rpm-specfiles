%global source0_hash 2281f946427a882010042844a38c7bbe9e0d0aaf9d46babe46366ed6f169b72e

Name:		python-hsluv
Version:	5.0.4
Release:	9%{?dist}
Summary:	A Python implementation of HSLuv (revision 4)
License:	MIT
URL:		https://www.hsluv.org/
Source0:	%{pypi_source hsluv}

BuildArch:	noarch
BuildRequires:	python3-devel

# Tests
BuildRequires:	python3dist(pytest)

%global _description %{expand:
A Python implementation of HSLuv (revision 4).}

%description %_description

%package -n python3-hsluv
Summary: %{summary}

%description -n python3-hsluv %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n hsluv-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l hsluv

%check
%pytest
%pyproject_check_import

%files -n python3-hsluv -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
