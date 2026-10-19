%global source0_hash 0154689a5aa009174b5e332a6997318e82e1b12b57fce03162ed49ea25c65652
Name:           python-blurb
Version:        2.1.0
Release:        1%{?dist}
Summary:        Command-line tool to manage CPython Misc/NEWS.d entries.
License:        ...
URL:            https://github.com/python/blurb
Source0:        https://files.pythonhosted.org/packages/source/b/blurb/blurb-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-blurb = %{version}-%{release}
# /oreon:deps
%package -n       python3-blurb+tests
Summary:        Metapackage for python3-blurb tests extras
Requires:       python3-blurb = %{version}-%{release}
Provides:       python3dist(blurb[tests]) = %{version}-%{release}

%description -n python3-blurb+tests
Metapackage for python3-blurb tests extras.

%description

%package -n     python3-blurb
Summary:        Command-line tool to manage CPython Misc/NEWS.d entries.
%description -n python3-blurb

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir blurb-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-blurb usr/lib/python3*/site-packages/blurb* usr/lib64/python3*/site-packages/blurb* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/blurb* usr/lib64/python3*/site-packages/blurb* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-blurb -f %{oreon_filedir}/python3-blurb.list

%changelog

%autochangelog
