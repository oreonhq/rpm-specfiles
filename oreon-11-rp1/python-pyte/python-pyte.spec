%global source0_hash ef84b6ba3b5ece72da5f0f33b7a6719bf3b13c7e24fdb92ce8161a3ae11eee31

Summary:        In memory VT-compatible terminal emulator
Name:           python-pyte
Version:        0.8.2
Release:        15%{?dist}
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            https://github.com/selectel/pyte
Source0:        https://github.com/selectel/pyte/archive/%{version}/pyte-%{version}.tar.gz
Patch0:         python-pyte-0.8.0-docs.patch
# Remove reference to unused and deprecated pytest-runner
# https://github.com/selectel/pyte/pull/177
Patch1:         %{url}/pull/177.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-wcwidth
%description
In memory VTXXX-compatible terminal emulator.  XXX stands for a series
of video terminals, developed by DEC between 1970 and 1995.

%package     -n python3-pyte
Summary:        %{summary}
%description -n python3-pyte
In memory VTXXX-compatible terminal emulator.  XXX stands for a series
of video terminals, developed by DEC between 1970 and 1995.

%package     -n python3-pyte-docs
Summary:        Documentation of API in Python module pyte
%description -n python3-pyte-docs
This contains documentation of the API in Python module pyte.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pyte-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd docs && make all

%install
%pyproject_install
%pyproject_save_files -l pyte

%check
%pyproject_check_import

export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{pytest} --color=yes

%files -n python3-pyte -f %{pyproject_files}
%doc AUTHORS CHANGES README 

%files -n python3-pyte-docs
%license LICENSE
%doc examples/
%doc docs/_build/html

%changelog
%autochangelog
