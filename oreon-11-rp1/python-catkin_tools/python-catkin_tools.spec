%global source0_hash 2de860e29778064b5f06f32202a667665654269ad70ea95f7ab54741fae57794
Name:           python-catkin-tools
Version:        0.9.5
Release:        1%{?dist}
Summary:        Command line tools for working with catkin.
License:        ...
URL:            https://catkin-tools.readthedocs.org/
Source0:        https://files.pythonhosted.org/packages/source/c/catkin_tools/catkin_tools-%{version}.tar.gz
BuildArch:      noarch
Patch0:         %{srcname}-0.9.5-sphinx8.patch
Patch1:         %{name}-rm-python-mock-usage.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-catkin-tools = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-catkin-tools
Summary:        Command line tools for working with catkin.
%description -n python3-catkin-tools

%prep
%global oreon_srcdir catkin_tools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-catkin-tools usr/lib/python3*/site-packages/catkin_tools* usr/lib64/python3*/site-packages/catkin_tools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/catkin_tools* usr/lib64/python3*/site-packages/catkin_tools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-catkin-tools -f %{oreon_filedir}/python3-catkin-tools.list

%changelog

%autochangelog
