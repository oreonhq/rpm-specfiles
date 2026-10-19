%global source0_hash 176b9e6781f7f40fd2de040701305341b5776986717798dc98afdb985e89d345
Name:           python-mackup
Version:        0.11.2
Release:        1%{?dist}
Summary:        Backup and keep your application settings in sync.
License:        GPL-3.0-or-later
URL:            https://github.com/lra/mackup.git
Source0:        https://files.pythonhosted.org/packages/source/m/mackup/mackup-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mackup = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mackup
Summary:        Backup and keep your application settings in sync.
# oreon:reqs
Requires:       python3dist(docopt-ng) >= 0.9.0
# /oreon:reqs
%description -n python3-mackup

%prep
%global oreon_srcdir mackup-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mackup usr/lib/python3*/site-packages/mackup* usr/lib64/python3*/site-packages/mackup* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mackup* usr/lib64/python3*/site-packages/mackup* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mackup -f %{oreon_filedir}/python3-mackup.list

%changelog

%autochangelog
