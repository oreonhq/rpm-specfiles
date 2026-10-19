%global source0_hash 0c9e1c414ffb0720be26285d472e263d1e704b71d31a7e13274b9996db4969e1
Name:           python-rich-toolkit
Version:        0.20.5
Release:        1%{?dist}
Summary:        Rich toolkit for building command-line applications
License:        MIT
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/r/rich_toolkit/rich_toolkit-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rich-toolkit = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-rich-toolkit
Summary:        Rich toolkit for building command-line applications
# oreon:reqs
Requires:       python3dist(click) >= 8.1.7
Requires:       python3dist(rich) >= 13.7.1
Requires:       python3dist(typing-extensions) >= 4.12.2
# /oreon:reqs
%description -n python3-rich-toolkit

%prep
%global oreon_srcdir rich_toolkit-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rich-toolkit usr/lib/python3*/site-packages/rich_toolkit* usr/lib64/python3*/site-packages/rich_toolkit* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rich_toolkit* usr/lib64/python3*/site-packages/rich_toolkit* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rich-toolkit -f %{oreon_filedir}/python3-rich-toolkit.list

%changelog

%autochangelog
