%global source0_hash aeef4e1b00c32316d624ea7e3ac87c244bf2e59abbb6c042e7791f69ae0669cb

%global srcname supersmoother

Name:           python-%{srcname}
Version:        0.4
Release:        %autorelease
Summary:        Python implementation of Friedman's Supersmoother

License:        BSD-2-Clause
URL:            https://github.com/jakevdp/supersmoother
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist pytest}
# Required for tests
BuildRequires:  %{py3_dist numpy}

%description
This is an efficient implementation of Friedman’s SuperSmoother based in
Python. It makes use of numpy for fast numerical computation.

%package -n python3-%{srcname}
Summary:    %{summary}

%description -n python3-%{srcname}
This is an efficient implementation of Friedman’s SuperSmoother based in
Python. It makes use of numpy for fast numerical computation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l supersmoother

%check
%pyproject_check_import -t
#_pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGES.md README.md

%changelog
%autochangelog
