%global source0_hash 8e30df5e8f2a927191afacd22653924ba5ec54ca00f965f4af3ed38e37b727a9
Name:           python-psygnal
Version:        0.16.1
Release:        1%{?dist}
Summary:        Fast python callback/event system modeled after Qt Signals
License:        ...
URL:            https://github.com/pyapp-kit/psygnal
Source0:        https://files.pythonhosted.org/packages/source/p/psygnal/psygnal-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.8.0
Requires:       python3-psygnal = %{version}-%{release}
# /oreon:deps
%package -n       python3-psygnal+proxy
Summary:        Metapackage for python3-psygnal proxy extras
Requires:       python3-psygnal = %{version}-%{release}
Provides:       python3dist(psygnal[proxy]) = %{version}-%{release}

%description -n python3-psygnal+proxy
Metapackage for python3-psygnal proxy extras.

%package -n       python3-psygnal+pydantic
Summary:        Metapackage for python3-psygnal pydantic extras
Requires:       python3-psygnal = %{version}-%{release}
Provides:       python3dist(psygnal[pydantic]) = %{version}-%{release}

%description -n python3-psygnal+pydantic
Metapackage for python3-psygnal pydantic extras.

%description

%package -n     python3-psygnal
Summary:        Fast python callback/event system modeled after Qt Signals
%description -n python3-psygnal

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir psygnal-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-psygnal usr/lib/python3*/site-packages/psygnal* usr/lib64/python3*/site-packages/psygnal* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/psygnal* usr/lib64/python3*/site-packages/psygnal* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-psygnal -f %{oreon_filedir}/python3-psygnal.list

%changelog

%autochangelog
