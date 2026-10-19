%global source0_hash ff9e9b1c48389ef78ed1787e7693c555e84e6bb9bac16be1fd65e1616dbf80c8
Name:           python-emoji
Version:        2.16.0
Release:        1%{?dist}
Summary:        Emoji for Python
License:        ...
URL:            https://github.com/carpedm20/emoji/
Source0:        https://files.pythonhosted.org/packages/source/e/emoji/emoji-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 65.0.0
Requires:       python3-emoji = %{version}-%{release}
# /oreon:deps
%package -n       python3-emoji+dev
Summary:        Metapackage for python3-emoji dev extras
Requires:       python3-emoji = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.4.4
Provides:       python3dist(emoji[dev]) = %{version}-%{release}

%description -n python3-emoji+dev
Metapackage for python3-emoji dev extras.

%description

%package -n     python3-emoji
Summary:        Emoji for Python
%description -n python3-emoji

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir emoji-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-emoji usr/lib/python3*/site-packages/emoji* usr/lib64/python3*/site-packages/emoji* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/emoji* usr/lib64/python3*/site-packages/emoji* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-emoji -f %{oreon_filedir}/python3-emoji.list

%changelog

%autochangelog
