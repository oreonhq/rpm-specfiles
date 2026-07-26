%global source0_hash d022c33afbdc8405c226621b015e8067888173d85f7f5ecebb3cafed9a20f02c

%global srcname partd

Name:           python-%{srcname}
Version:        1.4.2
Release:        %autorelease
Summary:        Appendable key-value storage

License:        BSD-3-Clause
URL:            https://github.com/dask/partd
Source:         %pypi_source %{srcname}

BuildArch:      noarch

# Needed for the zeromq test
BuildRequires:  systemd-resolved

%global _description %{expand:
Key-value byte store with appendable values: Partd stores key-value pairs.
Values are raw bytes. We append on old values. Partd excels at shuffling
operations.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

Recommends:     python3-%{srcname}+complete

%description -n python3-%{srcname} %{_description}

%pyproject_extras_subpkg -n python3-%{srcname} complete

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x complete

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%{pytest}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
