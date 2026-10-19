%global source0_hash cd3d118267d07bcfd1c9e8d5f434725c2cf9d89521b00b216cff08a1414c3535
Name:           python-ephyviewer
Version:        1.8.0
Release:        1%{?dist}
Summary:        Simple viewers for ephys signals, events, video and more
License:        MIT
URL:            https://ephyviewer.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/e/ephyviewer/ephyviewer-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{forgeurl}/pull/185.patch
Patch:          %{forgeurl}/pull/188.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 62.0
Requires:       python3-ephyviewer = %{version}-%{release}
# /oreon:deps
%package -n       python3-ephyviewer+test
Summary:        Metapackage for python3-ephyviewer test extras
Requires:       python3-ephyviewer = %{version}-%{release}
Requires:       python3dist(neo) >= 0.14.4
Requires:       python3dist(spikeinterface) >= 0.103.0
Provides:       python3dist(ephyviewer[test]) = %{version}-%{release}

%description -n python3-ephyviewer+test
Metapackage for python3-ephyviewer test extras.

%package -n       python3-ephyviewer+docs
Summary:        Metapackage for python3-ephyviewer docs extras
Requires:       python3-ephyviewer = %{version}-%{release}
Provides:       python3dist(ephyviewer[docs]) = %{version}-%{release}

%description -n python3-ephyviewer+docs
Metapackage for python3-ephyviewer docs extras.

%description

%package -n     python3-ephyviewer
Summary:        Simple viewers for ephys signals, events, video and more
# oreon:reqs
Requires:       python3dist(matplotlib) >= 2.0
Requires:       python3dist(pyqtgraph) >= 0.14.0
# /oreon:reqs
%description -n python3-ephyviewer

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ephyviewer-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ephyviewer usr/lib/python3*/site-packages/ephyviewer* usr/lib64/python3*/site-packages/ephyviewer* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ephyviewer* usr/lib64/python3*/site-packages/ephyviewer* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ephyviewer -f %{oreon_filedir}/python3-ephyviewer.list

%changelog

%autochangelog
