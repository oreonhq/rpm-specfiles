%global source0_hash e7689dda71aaf739244d6c8690de13cb1361b8d0a79980fb48bb397455ca0bdd
Name:           python-apprise
Version:        1.13.1
Release:        1%{?dist}
Summary:        Push Notifications that work with just about every platform!
License:        BSD-2-Clause
URL:            https://appriseit.com
Source0:        https://files.pythonhosted.org/packages/source/a/apprise/apprise-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 69
Requires:       python3-apprise = %{version}-%{release}
# /oreon:deps
%package -n       python3-apprise+dev
Summary:        Metapackage for python3-apprise dev extras
Requires:       python3-apprise = %{version}-%{release}
Requires:       python3dist(ruff) == 0.15.8
Provides:       python3dist(apprise[dev]) = %{version}-%{release}

%description -n python3-apprise+dev
Metapackage for python3-apprise dev extras.

%package -n       python3-apprise+all-plugins
Summary:        Metapackage for python3-apprise all-plugins extras
Requires:       python3-apprise = %{version}-%{release}
Requires:       python3dist(paho-mqtt) >= 2.1.0
Requires:       python3dist(slixmpp) >= 1.16.0
Provides:       python3dist(apprise[all-plugins]) = %{version}-%{release}

%description -n python3-apprise+all-plugins
Metapackage for python3-apprise all-plugins extras.

%package -n       python3-apprise+windows
Summary:        Metapackage for python3-apprise windows extras
Requires:       python3-apprise = %{version}-%{release}
Provides:       python3dist(apprise[windows]) = %{version}-%{release}

%description -n python3-apprise+windows
Metapackage for python3-apprise windows extras.

%description

%package -n     python3-apprise
Summary:        Push Notifications that work with just about every platform!
# oreon:reqs
Requires:       python3dist(click) >= 5.0
# /oreon:reqs
%description -n python3-apprise

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir apprise-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-apprise usr/lib/python3*/site-packages/apprise* usr/lib64/python3*/site-packages/apprise* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/apprise* usr/lib64/python3*/site-packages/apprise* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-apprise -f %{oreon_filedir}/python3-apprise.list

%changelog

%autochangelog
