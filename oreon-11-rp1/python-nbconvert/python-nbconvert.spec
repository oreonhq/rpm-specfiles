%global source0_hash 34d0d0a7e73ce3cbab6c5aae8f4f468797280b01fd8bd2ca746da8569eddd7d2
Name:           python-nbconvert
Version:        7.17.1
Release:        1%{?dist}
Summary:        Convert Jupyter Notebooks _.ipynb files_ to other formats.
License:        ...
URL:            https://jupyter.org
Source0:        https://files.pythonhosted.org/packages/source/n/nbconvert/nbconvert-%{version}.tar.gz
BuildArch:      noarch
Patch1:         backport-mistune-3.1.0-support.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.5
Requires:       python3-nbconvert = %{version}-%{release}
# /oreon:deps
%package -n       python3-nbconvert+qtpng
Summary:        Metapackage for python3-nbconvert qtpng extras
Requires:       python3-nbconvert = %{version}-%{release}
Requires:       python3dist(pyqtwebengine) >= 5.15
Provides:       python3dist(nbconvert[qtpng]) = %{version}-%{release}

%description -n python3-nbconvert+qtpng
Metapackage for python3-nbconvert qtpng extras.

%package -n       python3-nbconvert+qtpdf
Summary:        Metapackage for python3-nbconvert qtpdf extras
Requires:       python3-nbconvert = %{version}-%{release}
Provides:       python3dist(nbconvert[qtpdf]) = %{version}-%{release}

%description -n python3-nbconvert+qtpdf
Metapackage for python3-nbconvert qtpdf extras.

%package -n       python3-nbconvert+webpdf
Summary:        Metapackage for python3-nbconvert webpdf extras
Requires:       python3-nbconvert = %{version}-%{release}
Provides:       python3dist(nbconvert[webpdf]) = %{version}-%{release}

%description -n python3-nbconvert+webpdf
Metapackage for python3-nbconvert webpdf extras.

%package -n       python3-nbconvert+test
Summary:        Metapackage for python3-nbconvert test extras
Requires:       python3-nbconvert = %{version}-%{release}
Requires:       python3dist(pytest) >= 7
Requires:       python3dist(ipywidgets) >= 7.5
Provides:       python3dist(nbconvert[test]) = %{version}-%{release}

%description -n python3-nbconvert+test
Metapackage for python3-nbconvert test extras.

%package -n       python3-nbconvert+serve
Summary:        Metapackage for python3-nbconvert serve extras
Requires:       python3-nbconvert = %{version}-%{release}
Requires:       python3dist(tornado) >= 6.1
Provides:       python3dist(nbconvert[serve]) = %{version}-%{release}

%description -n python3-nbconvert+serve
Metapackage for python3-nbconvert serve extras.

%package -n       python3-nbconvert+docs
Summary:        Metapackage for python3-nbconvert docs extras
Requires:       python3-nbconvert = %{version}-%{release}
Requires:       python3dist(sphinx) >= 5.0.2
Requires:       python3dist(nbsphinx) >= 0.2.12
Provides:       python3dist(nbconvert[docs]) = %{version}-%{release}

%description -n python3-nbconvert+docs
Metapackage for python3-nbconvert docs extras.

%package -n       python3-nbconvert+all
Summary:        Metapackage for python3-nbconvert all extras
Requires:       python3-nbconvert = %{version}-%{release}
Provides:       python3dist(nbconvert[all]) = %{version}-%{release}

%description -n python3-nbconvert+all
Metapackage for python3-nbconvert all extras.

%description

%package -n     python3-nbconvert
Summary:        Convert Jupyter Notebooks _.ipynb files_ to other formats.
# oreon:reqs
Requires:       python3dist(bleach[css])
Requires:       python3dist(importlib-metadata) >= 3.6
Requires:       python3dist(jinja2) >= 3.0
Requires:       python3dist(jupyter-core) >= 4.7
Requires:       python3dist(markupsafe) >= 2.0
Requires:       python3dist(mistune) < 4
Requires:       python3dist(mistune) >= 2.0.3
Requires:       python3dist(nbclient) >= 0.5.0
Requires:       python3dist(nbformat) >= 5.7
Requires:       python3dist(pandocfilters) >= 1.4.1
Requires:       python3dist(pygments) >= 2.4.1
Requires:       python3dist(traitlets) >= 5.1
# /oreon:reqs
%description -n python3-nbconvert

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir nbconvert-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-nbconvert usr/lib/python3*/site-packages/nbconvert* usr/lib64/python3*/site-packages/nbconvert* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/nbconvert* usr/lib64/python3*/site-packages/nbconvert* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-nbconvert -f %{oreon_filedir}/python3-nbconvert.list

%changelog

%autochangelog
