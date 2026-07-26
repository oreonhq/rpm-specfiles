%global source0_hash 6b5d7b4b05cfda53aae55fc43aaf29421e0c45a6eac57ed52ddf3041bc73c7fc

%global forgeurl https://github.com/noxdafox/pebble

# Tests take rather long compared to build. Allow skipping.
%bcond tests 1

Name:           python-pebble
Version:        5.2.0
Release:        %autorelease
Summary:        Threading and multiprocessing eye-candy for Python

%global tag %{version}
%forgemeta

License:        LGPL-3.0-or-later
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Pebble provides an API to manage threads and processes within an application.
It wraps Python’s standard library threading and multiprocessing objects.}

%description %_description

%package -n python3-pebble
Summary:        %{summary}

%description -n python3-pebble %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pebble

%check
%if %{with tests}
  # test intermittently hangs
  %{pytest} -v -k "not test_process_pool_multiple_futures"
%else
  %pyproject_check_import
%endif

%files -n python3-pebble -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
