%global source0_hash 8ec9fbfde2e32f020b167e348f3ab3bac6625a5f15af524d790108ac7147a410
Name:           python-sounddevice
Version:        0.5.6
Release:        1%{?dist}
Summary:        Play and Record Sound with Python
License:        MIT
URL:            https://github.com/spatialaudio/python-sounddevice/
Source0:        https://files.pythonhosted.org/packages/source/s/sounddevice/sounddevice-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sounddevice = %{version}-%{release}
# /oreon:deps
%package -n       python3-sounddevice+numpy
Summary:        Metapackage for python3-sounddevice numpy extras
Requires:       python3-sounddevice = %{version}-%{release}
Provides:       python3dist(sounddevice[numpy]) = %{version}-%{release}

%description -n python3-sounddevice+numpy
Metapackage for python3-sounddevice numpy extras.

%description

%package -n     python3-sounddevice
Summary:        Play and Record Sound with Python
%description -n python3-sounddevice

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sounddevice-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sounddevice usr/lib/python3*/site-packages/sounddevice* usr/lib64/python3*/site-packages/sounddevice* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sounddevice* usr/lib64/python3*/site-packages/sounddevice* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sounddevice -f %{oreon_filedir}/python3-sounddevice.list

%changelog

%autochangelog
