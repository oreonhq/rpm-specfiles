%global source0_hash adb31d4c263f2bd041081ab33b498309a57c77f9acf2db65aadf0898179cf93a
Name:           python-tenacity
Version:        9.1.4
Release:        1%{?dist}
Summary:        Retry code until it succeeds
License:        ...
URL:            https://github.com/jd/tenacity
Source0:        https://files.pythonhosted.org/packages/source/t/tenacity/tenacity-%{version}.tar.gz
BuildArch:      noarch
Patch0:         528.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 21.0.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4
Requires:       python3-tenacity = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-tenacity
Summary:        Retry code until it succeeds
%description -n python3-tenacity

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir tenacity-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tenacity usr/lib/python3*/site-packages/tenacity* usr/lib64/python3*/site-packages/tenacity* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tenacity* usr/lib64/python3*/site-packages/tenacity* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tenacity -f %{oreon_filedir}/python3-tenacity.list

%changelog

%autochangelog
