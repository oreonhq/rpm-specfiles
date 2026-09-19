%global source0_hash 21392b91fafd81c09bba3a6b57c31d9147e5d311fa652e72153a7eda5d4a726f

Name:           python-retask
Version:        1.1.0
Release:        13%{?dist}
Summary:        Python module to create and manage distributed task queues

License:        MIT
URL:            http://retask.readthedocs.org/en/latest/index.html
Source0:        https://pypi.python.org/packages/source/r/retask/retask-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-redis
BuildRequires:  pyproject-rpm-macros

%global _description\
Python module to create and manage distributed task queues using redis.

%description %_description

%generate_buildrequires
%pyproject_buildrequires

%package -n python3-retask
Summary:        %{summary}
%{?python_provide:%python_provide python3-retask}
Requires:       python3-redis

%description -n python3-retask %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n retask-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-retask
%doc LICENSE
%{python3_sitelib}/retask*/

%changelog
%autochangelog
