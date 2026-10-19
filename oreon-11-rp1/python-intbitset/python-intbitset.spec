%global source0_hash f82fafe0bcb4fe7a010d942099b5a84d721d37c897538ed632f788962c1411f8
Name:           python-intbitset
Version:        4.1.2
Release:        1%{?dist}
Summary:        C-based extension implementing fast integer bit sets.
License:        LGPL-3.0-or-later
URL:            http://github.com/inveniosoftware-contrib/intbitset/
Source0:        https://files.pythonhosted.org/packages/source/i/intbitset/intbitset-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-intbitset = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-intbitset
Summary:        C-based extension implementing fast integer bit sets.
%description -n python3-intbitset

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir intbitset-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-intbitset usr/lib/python3*/site-packages/intbitset* usr/lib64/python3*/site-packages/intbitset* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/intbitset* usr/lib64/python3*/site-packages/intbitset* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-intbitset -f %{oreon_filedir}/python3-intbitset.list

%changelog

%autochangelog
