%global source0_hash d210b1e0d08f77e55ebcf9940ecc0c639663d12937d8c7b72de7cbbb6d0a4009
Name:           python-yaml2ical
Version:        0.15.0
Release:        1%{?dist}
Summary:        Convert YAML meeting descriptions into iCalendar files
License:        Apache-2.0
URL:            https://opendev.org/opendev/yaml2ical
Source0:        https://files.pythonhosted.org/packages/source/y/yaml2ical/yaml2ical-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-yaml2ical = %{version}-%{release}
# /oreon:deps
%package -n       python3-yaml2ical+test-linters
Summary:        Metapackage for python3-yaml2ical test-linters extras
Requires:       python3-yaml2ical = %{version}-%{release}
Requires:       python3dist(hacking) >= 7
Requires:       python3dist(hacking) < 8
Provides:       python3dist(yaml2ical[test-linters]) = %{version}-%{release}

%description -n python3-yaml2ical+test-linters
Metapackage for python3-yaml2ical test-linters extras.

%package -n       python3-yaml2ical+test-unit
Summary:        Metapackage for python3-yaml2ical test-unit extras
Requires:       python3-yaml2ical = %{version}-%{release}
Requires:       python3dist(coverage) >= 3.6
Requires:       python3dist(fixtures) >= 3.0.0
Requires:       python3dist(python-subunit) >= 0.0.18
Requires:       python3dist(stestr) >= 1.0.0
Requires:       python3dist(testtools) >= 1.4.0
Provides:       python3dist(yaml2ical[test-unit]) = %{version}-%{release}

%description -n python3-yaml2ical+test-unit
Metapackage for python3-yaml2ical test-unit extras.

%description

%package -n     python3-yaml2ical
Summary:        Convert YAML meeting descriptions into iCalendar files
# oreon:reqs
Requires:       python3dist(jinja2) >= 2.8
Requires:       python3dist(pbr) >= 1.6
Requires:       python3dist(pyyaml) >= 3.1.0
# /oreon:reqs
%description -n python3-yaml2ical

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir yaml2ical-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-yaml2ical usr/lib/python3*/site-packages/yaml2ical* usr/lib64/python3*/site-packages/yaml2ical* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/yaml2ical* usr/lib64/python3*/site-packages/yaml2ical* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-yaml2ical -f %{oreon_filedir}/python3-yaml2ical.list

%changelog

%autochangelog
