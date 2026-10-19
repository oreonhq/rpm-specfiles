%global source0_hash df80a10726cd1f71cca6b52548eded6e12422a5295a849b34fac3af4db536ed8
Name:           python-fsleyes-widgets
Version:        0.17.0
Release:        1%{?dist}
Summary:        A collection of wxPython widgets used by FSLeyes
License:        ...
URL:            https://git.fmrib.ox.ac.uk/fsl/fsleyes/widgets
Source0:        https://files.pythonhosted.org/packages/source/f/fsleyes_widgets/fsleyes_widgets-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fsleyes-widgets = %{version}-%{release}
# /oreon:deps
%package -n       python3-fsleyes-widgets+doc
Summary:        Metapackage for python3-fsleyes-widgets doc extras
Requires:       python3-fsleyes-widgets = %{version}-%{release}
Provides:       python3dist(fsleyes-widgets[doc]) = %{version}-%{release}

%description -n python3-fsleyes-widgets+doc
Metapackage for python3-fsleyes-widgets doc extras.

%package -n       python3-fsleyes-widgets+test
Summary:        Metapackage for python3-fsleyes-widgets test extras
Requires:       python3-fsleyes-widgets = %{version}-%{release}
Provides:       python3dist(fsleyes-widgets[test]) = %{version}-%{release}

%description -n python3-fsleyes-widgets+test
Metapackage for python3-fsleyes-widgets test extras.

%package -n       python3-fsleyes-widgets+style
Summary:        Metapackage for python3-fsleyes-widgets style extras
Requires:       python3-fsleyes-widgets = %{version}-%{release}
Provides:       python3dist(fsleyes-widgets[style]) = %{version}-%{release}

%description -n python3-fsleyes-widgets+style
Metapackage for python3-fsleyes-widgets style extras.

%description

%package -n     python3-fsleyes-widgets
Summary:        A collection of wxPython widgets used by FSLeyes
# oreon:reqs
Requires:       python3dist(matplotlib) >= 3.5
Requires:       python3dist(wxpython) >= 3.0.2.0
# /oreon:reqs
%description -n python3-fsleyes-widgets

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fsleyes_widgets-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fsleyes-widgets usr/lib/python3*/site-packages/fsleyes_widgets* usr/lib64/python3*/site-packages/fsleyes_widgets* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fsleyes_widgets* usr/lib64/python3*/site-packages/fsleyes_widgets* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fsleyes-widgets -f %{oreon_filedir}/python3-fsleyes-widgets.list

%changelog

%autochangelog
