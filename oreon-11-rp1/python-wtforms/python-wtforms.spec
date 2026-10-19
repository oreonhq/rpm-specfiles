%global source0_hash 7b00c73f8670f35d4edb0293dcd81b980528bee72fd662b182aaba27ae570b93
Name:           python-wtforms
Version:        3.2.2
Release:        1%{?dist}
Summary:        Form validation and rendering for Python web development.
License:        ...
URL:            https://github.com/pallets-eco/wtforms/
Source0:        https://files.pythonhosted.org/packages/source/w/wtforms/wtforms-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-wtforms = %{version}-%{release}
# /oreon:deps
%package -n       python3-wtforms+email
Summary:        Metapackage for python3-wtforms email extras
Requires:       python3-wtforms = %{version}-%{release}
Requires:       python3dist(email-validator) >= 2.0
Provides:       python3dist(wtforms[email]) = %{version}-%{release}

%description -n python3-wtforms+email
Metapackage for python3-wtforms email extras.

%description

%package -n     python3-wtforms
Summary:        Form validation and rendering for Python web development.
# oreon:reqs
Requires:       python3dist(markupsafe) >= 1.1.1
# /oreon:reqs
%description -n python3-wtforms

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir wtforms-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-wtforms usr/lib/python3*/site-packages/wtforms* usr/lib64/python3*/site-packages/wtforms* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/wtforms* usr/lib64/python3*/site-packages/wtforms* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-wtforms -f %{oreon_filedir}/python3-wtforms.list

%changelog

%autochangelog
