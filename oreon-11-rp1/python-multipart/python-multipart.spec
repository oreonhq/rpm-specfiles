%global source0_hash 211d7cfc1a7a43e75c4d24ee0e8e0f4f61d522f1a21575303ae85333dea687bf

Name:           python-multipart
Version:        1.3.1
Release:        %autorelease
Summary:        Parser for multipart/form-data
License:        MIT
URL:            https://github.com/defnull/multipart
Source:         %{pypi_source multipart}
BuildArch:      noarch

%global _description %{expand:
This module provides a fast incremental non-blocking parser for
multipart/form-data [HTML5, RFC7578], as well as blocking alternatives for
easier use in WSGI or CGI applications.}

%description %_description

%package -n python3-multipart
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%if %{defined fc43}
# This package originally used the same import namespace:
Conflicts:      python3-python-multipart
# Upstream for the other package switched the primary import name to “import
# python_multipart,” leaving “import multipart” as a compatibility shim that
# redirects to *this* multipart package if and only if it is installed. From
# Fedora 44, our python3-python-multipart no longer installs that compatibility
# shim (even though upstream still offers it) and therefore the Conflicts may
# be removed.
%endif

%description -n python3-multipart %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n multipart-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l multipart

%check
%pytest

%files -n python3-multipart -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
