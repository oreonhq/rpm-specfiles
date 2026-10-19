%global source0_hash faa3bd00ef1c9b209b1f31b154dd41c596fec3824f61a70c251fb5569acd7ba6
Name:           python-superqt
Version:        0.8.2
Release:        1%{?dist}
Summary:        Missing widgets and components for PyQt/PySide
License:        ...
URL:            https://github.com/pyapp-kit/superqt
Source0:        https://files.pythonhosted.org/packages/source/s/superqt/superqt-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-superqt = %{version}-%{release}
# /oreon:deps
%package -n       python3-superqt+cmap
Summary:        Metapackage for python3-superqt cmap extras
Requires:       python3-superqt = %{version}-%{release}
Requires:       python3dist(cmap) >= 0.2
Provides:       python3dist(superqt[cmap]) = %{version}-%{release}

%description -n python3-superqt+cmap
Metapackage for python3-superqt cmap extras.

%package -n       python3-superqt+font-fa5
Summary:        Metapackage for python3-superqt font-fa5 extras
Requires:       python3-superqt = %{version}-%{release}
Requires:       python3dist(fonticon-fontawesome5) >= 5.15.4
Provides:       python3dist(superqt[font-fa5]) = %{version}-%{release}

%description -n python3-superqt+font-fa5
Metapackage for python3-superqt font-fa5 extras.

%package -n       python3-superqt+font-fa6
Summary:        Metapackage for python3-superqt font-fa6 extras
Requires:       python3-superqt = %{version}-%{release}
Requires:       python3dist(fonticon-fontawesome6) >= 6.4.0
Provides:       python3dist(superqt[font-fa6]) = %{version}-%{release}

%description -n python3-superqt+font-fa6
Metapackage for python3-superqt font-fa6 extras.

%package -n       python3-superqt+font-mi6
Summary:        Metapackage for python3-superqt font-mi6 extras
Requires:       python3-superqt = %{version}-%{release}
Requires:       python3dist(fonticon-materialdesignicons6) >= 6.9.96
Provides:       python3dist(superqt[font-mi6]) = %{version}-%{release}

%description -n python3-superqt+font-mi6
Metapackage for python3-superqt font-mi6 extras.

%package -n       python3-superqt+font-mi7
Summary:        Metapackage for python3-superqt font-mi7 extras
Requires:       python3-superqt = %{version}-%{release}
Requires:       python3dist(fonticon-materialdesignicons7) >= 7.2.96
Provides:       python3dist(superqt[font-mi7]) = %{version}-%{release}

%description -n python3-superqt+font-mi7
Metapackage for python3-superqt font-mi7 extras.

%package -n       python3-superqt+iconify
Summary:        Metapackage for python3-superqt iconify extras
Requires:       python3-superqt = %{version}-%{release}
Requires:       python3dist(pyconify) >= 0.1.4
Provides:       python3dist(superqt[iconify]) = %{version}-%{release}

%description -n python3-superqt+iconify
Metapackage for python3-superqt iconify extras.

%package -n       python3-superqt+pyqt5
Summary:        Metapackage for python3-superqt pyqt5 extras
Requires:       python3-superqt = %{version}-%{release}
Requires:       python3dist(pyqt5) >= 5.15.10
Requires:       python3dist(pyqt5-qt5) >= 5.15.16
Requires:       python3dist(pyqt5-qt5) == 5.15.2
Provides:       python3dist(superqt[pyqt5]) = %{version}-%{release}

%description -n python3-superqt+pyqt5
Metapackage for python3-superqt pyqt5 extras.

%package -n       python3-superqt+pyqt6
Summary:        Metapackage for python3-superqt pyqt6 extras
Requires:       python3-superqt = %{version}-%{release}
Requires:       python3dist(pyqt6) >= 6.4.0
Requires:       python3dist(pyqt6) >= 6.7.0
Provides:       python3dist(superqt[pyqt6]) = %{version}-%{release}

%description -n python3-superqt+pyqt6
Metapackage for python3-superqt pyqt6 extras.

%package -n       python3-superqt+pyside6
Summary:        Metapackage for python3-superqt pyside6 extras
Requires:       python3-superqt = %{version}-%{release}
Requires:       python3dist(pyside6) >= 6.4.0
Requires:       python3dist(pyside6) >= 6.7.0
Provides:       python3dist(superqt[pyside6]) = %{version}-%{release}

%description -n python3-superqt+pyside6
Metapackage for python3-superqt pyside6 extras.

%package -n       python3-superqt+quantity
Summary:        Metapackage for python3-superqt quantity extras
Requires:       python3-superqt = %{version}-%{release}
Requires:       python3dist(pint) >= 0.21
Provides:       python3dist(superqt[quantity]) = %{version}-%{release}

%description -n python3-superqt+quantity
Metapackage for python3-superqt quantity extras.

%description

%package -n     python3-superqt
Summary:        Missing widgets and components for PyQt/PySide
# oreon:reqs
Requires:       python3dist(pygments) >= 2.4.0
Requires:       python3dist(qtpy) >= 2.4.0
Requires:       python3dist(typing-extensions) >= 4.12.0
Requires:       python3dist(typing-extensions) >= 4.5.0
# /oreon:reqs
%description -n python3-superqt

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir superqt-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-superqt usr/lib/python3*/site-packages/superqt* usr/lib64/python3*/site-packages/superqt* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/superqt* usr/lib64/python3*/site-packages/superqt* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-superqt -f %{oreon_filedir}/python3-superqt.list

%changelog

%autochangelog
