%global source0_hash f94ed2bc4cf69052e0f29592bd1e771a1789bd7bfc482dd0bc482134aff95823
Name:           python-click-option-group
Version:        0.5.9
Release:        1%{?dist}
Summary:        Option groups missing in Click
License:        BSD-3-Clause
URL:            https://github.com/click-contrib/click-option-group
Source0:        https://files.pythonhosted.org/packages/source/c/click_option_group/click_option_group-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-click-option-group = %{version}-%{release}
# /oreon:deps
%package -n       python3-click-option-group+test
Summary:        Metapackage for python3-click-option-group test extras
Requires:       python3-click-option-group = %{version}-%{release}
Provides:       python3dist(click-option-group[test]) = %{version}-%{release}

%description -n python3-click-option-group+test
Metapackage for python3-click-option-group test extras.

%package -n       python3-click-option-group+test-cov
Summary:        Metapackage for python3-click-option-group test-cov extras
Requires:       python3-click-option-group = %{version}-%{release}
Provides:       python3dist(click-option-group[test-cov]) = %{version}-%{release}

%description -n python3-click-option-group+test-cov
Metapackage for python3-click-option-group test-cov extras.

%package -n       python3-click-option-group+dev
Summary:        Metapackage for python3-click-option-group dev extras
Requires:       python3-click-option-group = %{version}-%{release}
Provides:       python3dist(click-option-group[dev]) = %{version}-%{release}

%description -n python3-click-option-group+dev
Metapackage for python3-click-option-group dev extras.

%package -n       python3-click-option-group+docs
Summary:        Metapackage for python3-click-option-group docs extras
Requires:       python3-click-option-group = %{version}-%{release}
Provides:       python3dist(click-option-group[docs]) = %{version}-%{release}

%description -n python3-click-option-group+docs
Metapackage for python3-click-option-group docs extras.

%description

%package -n     python3-click-option-group
Summary:        Option groups missing in Click
# oreon:reqs
Requires:       python3dist(click) >= 7.0
# /oreon:reqs
%description -n python3-click-option-group

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir click_option_group-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-click-option-group usr/lib/python3*/site-packages/click_option_group* usr/lib64/python3*/site-packages/click_option_group* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/click_option_group* usr/lib64/python3*/site-packages/click_option_group* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-click-option-group -f %{oreon_filedir}/python3-click-option-group.list

%changelog

%autochangelog
