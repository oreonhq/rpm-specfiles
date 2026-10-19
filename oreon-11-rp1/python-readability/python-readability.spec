%global source0_hash 5aace888855cb3ef1b7dd059e41bbc6ac1f7daba321b2d24062ca75fdf6e576d
Name:           python-readability
Version:        0.3.2
Release:        1%{?dist}
Summary:        Measure the readability of a given text using surface characteristics
License:        ...
URL:            https://github.com/andreasvc/readability/
Source0:        https://files.pythonhosted.org/packages/source/r/readability/readability-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-readability = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-readability
Summary:        Measure the readability of a given text using surface characteristics
%description -n python3-readability

%prep
%global oreon_srcdir readability-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-readability usr/lib/python3*/site-packages/readability* usr/lib64/python3*/site-packages/readability* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/readability* usr/lib64/python3*/site-packages/readability* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-readability -f %{oreon_filedir}/python3-readability.list

%changelog

%autochangelog
