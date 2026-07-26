%global source0_hash 723f24f4d65fc8d99b33a002fbbb3771d4cc9d664c97085bf37f3997ae8063af

%global sum Integrate more support into Python's distutils
%global srcname distutils-extra

Name:           python-%{srcname}
Version:        2.39
Release:        40%{?dist}
Summary:        %{sum}

License:        GPL-2.0-or-later
URL:            https://launchpad.net/python-distutils-extra
Source0:        http://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Enables you to easily integrate gettext support, themed icons and
scrollkeeper based documentation into Python's distutils. 

%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       intltool
Requires:       python3dist(setuptools)
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Enables you to easily integrate gettext support, themed icons and
scrollkeeper based documentation into Python's distutils. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%doc doc/*
%license LICENSE
%{python3_sitelib}/DistUtilsExtra/
%{python3_sitelib}/python_distutils_extra*.dist-info

%changelog
%autochangelog
