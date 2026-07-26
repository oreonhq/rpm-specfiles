%global source0_hash 3a55207bcfed53ddd5c5bae174524062935efed17792e9de2ad0205ce9ad63f7

Name:           python-monotonic
Version:        1.6
Release:        %autorelease
Summary:        An implementation of time.monotonic() for Python 2 & < 3.3
License:        Apache-2.0
URL:            https://github.com/atdt/monotonic
Source:         %{pypi_source monotonic}
BuildArch:      noarch

%global _description %{expand:
This module provides a monotonic() function which returns the value (in
fractional seconds) of a clock which never goes backwards.  On Python 3.3 or
newer, monotonic will be an alias of time.monotonic from the standard library.
On older versions, it will fall back to an equivalent implementation.}

%description %_description

%package -n python3-monotonic
Summary:        %{summary}
BuildRequires:  python3-devel
# Monotonic's GitHub repo was archived in 2021.  No other packages in Fedora
# depend on it.
Provides:       deprecated()

%description -n python3-monotonic %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n monotonic-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l monotonic

%check
%pyproject_check_import

%files -n python3-monotonic -f %{pyproject_files}

%changelog
%autochangelog
