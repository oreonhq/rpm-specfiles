%global source0_hash b426a7a6d6d53189d318f2b6236ab5d6429eaf09259f1ca33eb716eed10d2905
Name:           python-lark
Version:        1.3.1
Release:        1%{?dist}
Summary:        a modern parsing library
License:        MIT
URL:            https://github.com/lark-parser/lark
Source0:        https://files.pythonhosted.org/packages/source/l/lark/lark-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80
BuildRequires:  python3dist(setuptools-scm) >= 9.2.2
Requires:       python3-lark = %{version}-%{release}
# /oreon:deps
%package -n       python3-lark+regex
Summary:        Metapackage for python3-lark regex extras
Requires:       python3-lark = %{version}-%{release}
Provides:       python3dist(lark[regex]) = %{version}-%{release}

%description -n python3-lark+regex
Metapackage for python3-lark regex extras.

%package -n       python3-lark+nearley
Summary:        Metapackage for python3-lark nearley extras
Requires:       python3-lark = %{version}-%{release}
Provides:       python3dist(lark[nearley]) = %{version}-%{release}

%description -n python3-lark+nearley
Metapackage for python3-lark nearley extras.

%package -n       python3-lark+atomic_cache
Summary:        Metapackage for python3-lark atomic_cache extras
Requires:       python3-lark = %{version}-%{release}
Provides:       python3dist(lark[atomic_cache]) = %{version}-%{release}

%description -n python3-lark+atomic_cache
Metapackage for python3-lark atomic_cache extras.

%package -n       python3-lark+interegular
Summary:        Metapackage for python3-lark interegular extras
Requires:       python3-lark = %{version}-%{release}
Requires:       python3dist(interegular) >= 0.3.1
Requires:       python3dist(interegular) < 0.4.0
Provides:       python3dist(lark[interegular]) = %{version}-%{release}

%description -n python3-lark+interegular
Metapackage for python3-lark interegular extras.

%description

%package -n     python3-lark
Summary:        a modern parsing library
%description -n python3-lark

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir lark-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lark usr/lib/python3*/site-packages/lark* usr/lib64/python3*/site-packages/lark* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lark* usr/lib64/python3*/site-packages/lark* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-lark -f %{oreon_filedir}/python3-lark.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.2-1
- Prepare for Oreon 11 (RP1)
