%global source0_hash 9aac11583994f6b22fab6464180490cc3a336d46eb682f1438acebe3c0bbe53d
Name:           python-cmd2
Version:        4.2.4
Release:        1%{?dist}
Summary:        cmd2 - quickly build feature-rich and user-friendly interactive command line applications in Python
License:        MIT
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/c/cmd2/cmd2-%{version}.tar.gz
BuildArch:      noarch
Patch1:           Add-support-for-Python-3.14-and-remove-for-Python-3.8.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(build) >= 1.3.0
BuildRequires:  python3dist(setuptools) >= 80.8.0
BuildRequires:  python3dist(setuptools-scm) >= 9.2.1
Requires:       python3-cmd2 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cmd2
Summary:        cmd2 - quickly build feature-rich and user-friendly interactive command line applications in Python
# oreon:reqs
Requires:       python3dist(prompt-toolkit) >= 3.0.53
Requires:       python3dist(pyperclip) >= 1.8.2
Requires:       python3dist(rich) >= 15.0.0
Requires:       python3dist(rich-argparse) >= 1.7.2
# /oreon:reqs
%description -n python3-cmd2

%prep
%global oreon_srcdir cmd2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cmd2 usr/lib/python3*/site-packages/cmd2* usr/lib64/python3*/site-packages/cmd2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cmd2* usr/lib64/python3*/site-packages/cmd2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cmd2 -f %{oreon_filedir}/python3-cmd2.list

%changelog

%autochangelog
