%global source0_hash 565f9ad031c702dae404e27a099e3e09186a3ab1b9520f06d215502b651fd910
Name:           python-webencodings
Version:        0.6.1
Release:        1%{?dist}
Summary:        Character encoding aliases for legacy web content
License:        ...
URL:            https://github.com/CourtBouillon/webencodings
Source0:        https://files.pythonhosted.org/packages/source/w/webencodings/webencodings-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 5
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-webencodings = %{version}-%{release}
# /oreon:deps
%package -n       python3-webencodings+doc
Summary:        Metapackage for python3-webencodings doc extras
Requires:       python3-webencodings = %{version}-%{release}
Provides:       python3dist(webencodings[doc]) = %{version}-%{release}

%description -n python3-webencodings+doc
Metapackage for python3-webencodings doc extras.

%package -n       python3-webencodings+test
Summary:        Metapackage for python3-webencodings test extras
Requires:       python3-webencodings = %{version}-%{release}
Provides:       python3dist(webencodings[test]) = %{version}-%{release}

%description -n python3-webencodings+test
Metapackage for python3-webencodings test extras.

%description

%package -n     python3-webencodings
Summary:        Character encoding aliases for legacy web content
%description -n python3-webencodings

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir webencodings-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-webencodings usr/lib/python3*/site-packages/webencodings* usr/lib64/python3*/site-packages/webencodings* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/webencodings* usr/lib64/python3*/site-packages/webencodings* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-webencodings -f %{oreon_filedir}/python3-webencodings.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.1-33
- Prepare for Oreon 11 (RP1)
