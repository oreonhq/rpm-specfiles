%global source0_hash a1b28d6079f27203fa3098b69a98572675b3ff5bd02286c43e6dacd66615f879
Name:           python-py-walk
Version:        0.3.3
Release:        1%{?dist}
Summary:        Filter filesystem paths based on gitignore-like patterns
License:        MIT
URL:            https://github.com/pacha/py-walk
Source0:        https://files.pythonhosted.org/packages/source/p/py_walk/py_walk-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-py-walk = %{version}-%{release}
# /oreon:deps
%package -n       python3-py-walk+dev
Summary:        Metapackage for python3-py-walk dev extras
Requires:       python3-py-walk = %{version}-%{release}
Provides:       python3dist(py-walk[dev]) = %{version}-%{release}

%description -n python3-py-walk+dev
Metapackage for python3-py-walk dev extras.

%package -n       python3-py-walk+tests
Summary:        Metapackage for python3-py-walk tests extras
Requires:       python3-py-walk = %{version}-%{release}
Provides:       python3dist(py-walk[tests]) = %{version}-%{release}

%description -n python3-py-walk+tests
Metapackage for python3-py-walk tests extras.

%package -n       python3-py-walk+type-checks
Summary:        Metapackage for python3-py-walk type-checks extras
Requires:       python3-py-walk = %{version}-%{release}
Provides:       python3dist(py-walk[type-checks]) = %{version}-%{release}

%description -n python3-py-walk+type-checks
Metapackage for python3-py-walk type-checks extras.

%package -n       python3-py-walk+code-formatting
Summary:        Metapackage for python3-py-walk code-formatting extras
Requires:       python3-py-walk = %{version}-%{release}
Provides:       python3dist(py-walk[code-formatting]) = %{version}-%{release}

%description -n python3-py-walk+code-formatting
Metapackage for python3-py-walk code-formatting extras.

%package -n       python3-py-walk+publish
Summary:        Metapackage for python3-py-walk publish extras
Requires:       python3-py-walk = %{version}-%{release}
Provides:       python3dist(py-walk[publish]) = %{version}-%{release}

%description -n python3-py-walk+publish
Metapackage for python3-py-walk publish extras.

%description

%package -n     python3-py-walk
Summary:        Filter filesystem paths based on gitignore-like patterns
%description -n python3-py-walk

#%%pyproject_extras_subpkg -n python3-py-walk,tests 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir py_walk-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-py-walk usr/lib/python3*/site-packages/py_walk* usr/lib64/python3*/site-packages/py_walk* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/py_walk* usr/lib64/python3*/site-packages/py_walk* usr/bin/*

%check

%pyproject_check_import
%pytest tests
%files
%files -n python3-py-walk -f %{oreon_filedir}/python3-py-walk.list

%changelog

%autochangelog
