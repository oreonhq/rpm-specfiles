%global source0_hash ea716fcaf5dd491cadc34f7a03e55f146e91c43c77f1d631853ba025f121f3f0

%global srcname pocketlint

Name:      python-%{srcname}
Version:   0.26
Release:   %autorelease
Summary:   Support for running pylint against projects

License:   GPL-2.0-or-later
Url:       https://github.com/rhinstaller/%{srcname}
Source0:   https://github.com/rhinstaller/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch: noarch

%description
Addon pylint modules and configuration settings for checking the validity of
Python-based source projects.

%package -n python3-%{srcname}
Summary: Support for running pylint against projects (Python 3 version)
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-pylint

Requires: python3-packaging
Requires: python3-polib
Requires: python3-pylint

%description -n python3-%{srcname}
Addon pylint modules and configuration settings for checking the validity of
Python-based source projects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
make PYTHON=%{__python3} check

%files -n python3-%{srcname}
%license COPYING
%{python3_sitelib}/%{srcname}*dist-info
%{python3_sitelib}/%{srcname}/

%changelog
%autochangelog
