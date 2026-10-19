%global source0_hash 1c4ab2f2972764c896a8ac61ac53e261c8d29f0c6ccd652f84e18f08a4cab190
Name:           python-audioread
Version:        3.1.0
Release:        1%{?dist}
Summary:        Multi-library, cross-platform audio decoding.
License:        MIT
URL:            https://github.com/beetbox/audioread
Source0:        https://files.pythonhosted.org/packages/source/a/audioread/audioread-%{version}.tar.gz
BuildArch:      noarch
Patch0:         0001-Remove-legacy-sound-modules-absent-in-Python-3.13.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-audioread = %{version}-%{release}
# /oreon:deps
%package -n       python3-audioread+test
Summary:        Metapackage for python3-audioread test extras
Requires:       python3-audioread = %{version}-%{release}
Requires:       python3dist(pytest) >= 8.4.2
Requires:       python3dist(pytest-cov) >= 7.0.0
Provides:       python3dist(audioread[test]) = %{version}-%{release}

%description -n python3-audioread+test
Metapackage for python3-audioread test extras.

%package -n       python3-audioread+mad
Summary:        Metapackage for python3-audioread mad extras
Requires:       python3-audioread = %{version}-%{release}
Requires:       python3dist(pymad[mad]) (>=0.11.3
Requires:       python3dist(pymad[mad]) < 0.12.0)
Provides:       python3dist(audioread[mad]) = %{version}-%{release}

%description -n python3-audioread+mad
Metapackage for python3-audioread mad extras.

%package -n       python3-audioread+gi
Summary:        Metapackage for python3-audioread gi extras
Requires:       python3-audioread = %{version}-%{release}
Requires:       python3dist(pygobject) (>=3.54.2
Requires:       python3dist(pygobject) < 4.0.0)
Provides:       python3dist(audioread[gi]) = %{version}-%{release}

%description -n python3-audioread+gi
Metapackage for python3-audioread gi extras.

%description

%package -n     python3-audioread
Summary:        Multi-library, cross-platform audio decoding.
%description -n python3-audioread

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir audioread-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-audioread usr/lib/python3*/site-packages/audioread* usr/lib64/python3*/site-packages/audioread* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/audioread* usr/lib64/python3*/site-packages/audioread* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-audioread -f %{oreon_filedir}/python3-audioread.list

%changelog

%autochangelog
