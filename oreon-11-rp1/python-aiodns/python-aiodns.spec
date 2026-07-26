%global source0_hash 5faadf797ec7a406f281f0cb02824ca0cdbc2a7c4531549ba52aac9cb1ead6cf

# All tests require network access (DNS). We can run them manually with, e.g.:
#   fedpkg mockbuild --with network_tests --enable-network
%bcond_with network_tests

Name:           python-aiodns
Version:        4.0.0
Release:        2%{?dist}
Summary:        Simple DNS resolver for asyncio

License:        MIT
URL:            https://github.com/saghul/aiodns
Source0:        %{url}/archive/v%{version}/aiodns-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with network_tests}
BuildRequires:  %{py3_dist pytest}
# Optional uvloop integration tests:
BuildRequires:  %{py3_dist uvloop}
%endif

%global _description %{expand:
aiodns provides a simple way for doing asynchronous DNS resolutions using
pycares.}

%description %{_description}

%package     -n python3-aiodns
Summary:        %{summary}

%description -n python3-aiodns %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n aiodns-%{version} -p0

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l aiodns

%check
%pyproject_check_import
%if %{with network_tests}
%pytest tests.py
%endif

%files -n python3-aiodns -f %{pyproject_files}
%doc README.rst ChangeLog

%changelog
%autochangelog
