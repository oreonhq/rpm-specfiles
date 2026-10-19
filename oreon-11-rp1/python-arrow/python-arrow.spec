%global source0_hash ed0cc050e98001b8779e84d461b0098c4ac597e88704a655582b21d116e526d7
Name:               python-arrow
Version:            1.4.0
Release:        1%{?dist}
Summary:        Better dates and times for Python
License:            Apache-2.0
URL:                https://github.com/arrow-py/arrow
Source0:        https://files.pythonhosted.org/packages/source/a/arrow/arrow-%{version}.tar.gz
Patch:              0002-Fedora-dependency-adjustments.patch
BuildArch:          noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-arrow = %{version}-%{release}
# /oreon:deps
%package -n       python3-arrow+test
Summary:        Metapackage for python3-arrow test extras
Requires:       python3-arrow = %{version}-%{release}
Requires:       python3dist(dateparser) == 1.*
Requires:       python3dist(pytz) == 2025.2
Requires:       python3dist(simplejson) == 3.*
Provides:       python3dist(arrow[test]) = %{version}-%{release}

%description -n python3-arrow+test
Metapackage for python3-arrow test extras.

%package -n       python3-arrow+doc
Summary:        Metapackage for python3-arrow doc extras
Requires:       python3-arrow = %{version}-%{release}
Requires:       python3dist(sphinx) >= 7.0.0
Requires:       python3dist(sphinx-rtd-theme) >= 1.3.0
Provides:       python3dist(arrow[doc]) = %{version}-%{release}

%description -n python3-arrow+doc
Metapackage for python3-arrow doc extras.

%description

%package -n         python3-arrow
Summary:        Better dates and times for Python
BuildRequires:      python3-devel
# oreon:reqs
Requires:       python3dist(backports.zoneinfo) == 0.2.1
Requires:       python3dist(python-dateutil) >= 2.7.0
# /oreon:reqs
%description -n python3-arrow

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n arrow-%{version}
# Fix python tzdata dependency
sed -i 's/tzdata;python_version/pytzdata;python_version/' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-arrow usr/lib/python3*/site-packages/arrow* usr/lib64/python3*/site-packages/arrow* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/arrow* usr/lib64/python3*/site-packages/arrow* usr/bin/*

%check

%pytest
%files
%files -n python3-arrow -f %{oreon_filedir}/python3-arrow.list

%changelog

%autochangelog
