%global source0_hash 73f0b0c06d7925ca2b6d52b2dc51c2533a11f667cc6944f1f06c039ccc57c5ce
Name:           python-bokeh
Version:        3.10.0
Release:        1%{?dist}
Summary:        Interactive plots and applications in the browser from Python
License:        BSD-3-Clause
URL:            https://bokeh.org
Source0:        https://files.pythonhosted.org/packages/source/b/bokeh/bokeh-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-bokeh = %{version}-%{release}
# /oreon:deps
%package -n       python3-bokeh+sampledata
Summary:        Metapackage for python3-bokeh sampledata extras
Requires:       python3-bokeh = %{version}-%{release}
Requires:       python3dist(bokeh-sampledata) >= 2025.0
Provides:       python3dist(bokeh[sampledata]) = %{version}-%{release}

%description -n python3-bokeh+sampledata
Metapackage for python3-bokeh sampledata extras.

%package -n       python3-bokeh+extra
Summary:        Metapackage for python3-bokeh extra extras
Requires:       python3-bokeh = %{version}-%{release}
Requires:       python3dist(contourpy) >= 1.2
Requires:       python3dist(pandas) >= 2.0
Provides:       python3dist(bokeh[extra]) = %{version}-%{release}

%description -n python3-bokeh+extra
Metapackage for python3-bokeh extra extras.

%package -n       python3-bokeh+export
Summary:        Metapackage for python3-bokeh export extras
Requires:       python3-bokeh = %{version}-%{release}
Requires:       python3dist(selenium) >= 4.2
Provides:       python3dist(bokeh[export]) = %{version}-%{release}

%description -n python3-bokeh+export
Metapackage for python3-bokeh export extras.

%package -n       python3-bokeh+all
Summary:        Metapackage for python3-bokeh all extras
Requires:       python3-bokeh = %{version}-%{release}
Provides:       python3dist(bokeh[all]) = %{version}-%{release}

%description -n python3-bokeh+all
Metapackage for python3-bokeh all extras.

%description

%package -n     python3-bokeh
Summary:        Interactive plots and applications in the browser from Python
# oreon:reqs
Requires:       python3dist(jinja2) >= 2.9
Requires:       python3dist(narwhals) >= 1.13
Requires:       python3dist(numpy) >= 1.16
Requires:       python3dist(packaging) >= 16.8
Requires:       python3dist(pillow) >= 7.1.0
Requires:       python3dist(pyyaml) >= 3.10
Requires:       python3dist(tornado) >= 6.2
Requires:       python3dist(xyzservices) >= 2021.09.1
# /oreon:reqs
%description -n python3-bokeh

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir bokeh-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-bokeh usr/lib/python3*/site-packages/bokeh* usr/lib64/python3*/site-packages/bokeh* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/bokeh* usr/lib64/python3*/site-packages/bokeh* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-bokeh -f %{oreon_filedir}/python3-bokeh.list

%changelog

%autochangelog
