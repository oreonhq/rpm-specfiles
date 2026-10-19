%global source0_hash 562a586db20216ba7d2be8263deb9eb079e56048f9b8906d11d5f45aa81c5247
Name:           python-curio
Version:        1.6
Release:        1%{?dist}
Summary:        Curio
License:        ...
URL:            https://github.com/dabeaz/curio
Source0:        https://files.pythonhosted.org/packages/source/c/curio/curio-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-curio = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-curio
Summary:        Curio
%description -n python3-curio

%prep
%global oreon_srcdir curio-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-curio usr/lib/python3*/site-packages/curio* usr/lib64/python3*/site-packages/curio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/curio* usr/lib64/python3*/site-packages/curio* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-curio -f %{oreon_filedir}/python3-curio.list

%changelog

%autochangelog
