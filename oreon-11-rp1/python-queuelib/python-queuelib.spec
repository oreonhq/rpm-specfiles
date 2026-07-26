%global source0_hash 63925ea0c71862ff89aea1fd493402fd84b519989371cfcf0a11b369fb59bbcb

%global srcname queuelib

Name:           python-queuelib
Version:        1.8.0
Release:        6%{?dist}
Summary:        Collection of persistent (disk-based) queues

License:        LicenseRef-Callaway-BSD
URL:            https://github.com/scrapy/queuelib
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
Queuelib is a collection of persistent (disk-based) queues for
Python. Queuelib goals are speed and simplicity.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-hatchling
BuildRequires:  python3-pytest

%description -n python3-%{srcname}
Queuelib is a collection of persistent (disk-based) queues for
Python. Queuelib goals are speed and simplicity.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files queuelib

%check
%pytest -v

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
