%global source0_hash 1263c4bb481002e83a96e9253915b33241ac3e1ed6219a2793d3121f65159107
Name:           python-jaraco-path
Version:        3.7.2
Release:        1%{?dist}
Summary:        Miscellaneous path functions
License:        MIT
URL:            https://github.com/jaraco/jaraco.path
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco_path/jaraco_path-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.1
Requires:       python3-jaraco-path = %{version}-%{release}
# /oreon:deps
%package -n       python3-jaraco-path+test
Summary:        Metapackage for python3-jaraco-path test extras
Requires:       python3-jaraco-path = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Provides:       python3dist(jaraco-path[test]) = %{version}-%{release}

%description -n python3-jaraco-path+test
Metapackage for python3-jaraco-path test extras.

%package -n       python3-jaraco-path+doc
Summary:        Metapackage for python3-jaraco-path doc extras
Requires:       python3-jaraco-path = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.5
Requires:       python3dist(jaraco.packaging) >= 9.3
Requires:       python3dist(rst.linker) >= 1.9
Provides:       python3dist(jaraco-path[doc]) = %{version}-%{release}

%description -n python3-jaraco-path+doc
Metapackage for python3-jaraco-path doc extras.

%package -n       python3-jaraco-path+check
Summary:        Metapackage for python3-jaraco-path check extras
Requires:       python3-jaraco-path = %{version}-%{release}
Requires:       python3dist(pytest-checkdocs) >= 2.4
Requires:       python3dist(pytest-ruff) >= 0.2.1
Provides:       python3dist(jaraco-path[check]) = %{version}-%{release}

%description -n python3-jaraco-path+check
Metapackage for python3-jaraco-path check extras.

%package -n       python3-jaraco-path+cover
Summary:        Metapackage for python3-jaraco-path cover extras
Requires:       python3-jaraco-path = %{version}-%{release}
Provides:       python3dist(jaraco-path[cover]) = %{version}-%{release}

%description -n python3-jaraco-path+cover
Metapackage for python3-jaraco-path cover extras.

%package -n       python3-jaraco-path+enabler
Summary:        Metapackage for python3-jaraco-path enabler extras
Requires:       python3-jaraco-path = %{version}-%{release}
Requires:       python3dist(pytest-enabler) >= 2.2
Provides:       python3dist(jaraco-path[enabler]) = %{version}-%{release}

%description -n python3-jaraco-path+enabler
Metapackage for python3-jaraco-path enabler extras.

%package -n       python3-jaraco-path+type
Summary:        Metapackage for python3-jaraco-path type extras
Requires:       python3-jaraco-path = %{version}-%{release}
Provides:       python3dist(jaraco-path[type]) = %{version}-%{release}

%description -n python3-jaraco-path+type
Metapackage for python3-jaraco-path type extras.

%description

%package -n     python3-jaraco-path
Summary:        Miscellaneous path functions
%description -n python3-jaraco-path

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir jaraco_path-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jaraco-path usr/lib/python3*/site-packages/jaraco_path* usr/lib64/python3*/site-packages/jaraco_path* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jaraco_path* usr/lib64/python3*/site-packages/jaraco_path* usr/bin/*

%check

%pytest
%files
%files -n python3-jaraco-path -f %{oreon_filedir}/python3-jaraco-path.list

%changelog

%autochangelog
