%global source0_hash dc983d19a509c94dba722ee6abd33940f7c05a89e243c47e907eb4db6f1a43e5
Name:           python-typing-extensions
Version:        4.16.0
Release:        1%{?dist}
Summary:        Backported and Experimental Type Hints for Python 3.9+
License:        PSF-2.0
URL:            https://github.com/python/typing_extensions
Source0:        https://files.pythonhosted.org/packages/source/t/typing_extensions/typing_extensions-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-typing-extensions = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-typing-extensions
Summary:        Backported and Experimental Type Hints for Python 3.9+
%description -n python3-typing-extensions

%prep
%global oreon_srcdir typing_extensions-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-typing-extensions usr/lib/python3*/site-packages/typing_extensions* usr/lib64/python3*/site-packages/typing_extensions* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/typing_extensions* usr/lib64/python3*/site-packages/typing_extensions* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-typing-extensions -f %{oreon_filedir}/python3-typing-extensions.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.15.0-4
- Prepare for Oreon 11 (RP1)
