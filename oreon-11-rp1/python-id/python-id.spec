%global source0_hash d0732d624fb46fd4e7bc4e5152f00214450953b9e772c182c1c22964def1a069
Name:           python-id
Version:        1.6.1
Release:        1%{?dist}
Summary:        A tool for generating OIDC identities
License:        Apache-2.0
URL:            https://github.com/di/id
Source0:        https://files.pythonhosted.org/packages/source/i/id/id-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-id = %{version}-%{release}
# /oreon:deps
%package -n       python3-id+test
Summary:        Metapackage for python3-id test extras
Requires:       python3-id = %{version}-%{release}
Provides:       python3dist(id[test]) = %{version}-%{release}

%description -n python3-id+test
Metapackage for python3-id test extras.

%package -n       python3-id+lint
Summary:        Metapackage for python3-id lint extras
Requires:       python3-id = %{version}-%{release}
Requires:       python3dist(ruff) < 0.14.15
Provides:       python3dist(id[lint]) = %{version}-%{release}

%description -n python3-id+lint
Metapackage for python3-id lint extras.

%package -n       python3-id+dev
Summary:        Metapackage for python3-id dev extras
Requires:       python3-id = %{version}-%{release}
Requires:       python3dist(bump) >= 1.3.2
Provides:       python3dist(id[dev]) = %{version}-%{release}

%description -n python3-id+dev
Metapackage for python3-id dev extras.

%description

%package -n     python3-id
Summary:        A tool for generating OIDC identities
# oreon:reqs
Requires:       python3dist(urllib3) < 3
Requires:       python3dist(urllib3) >= 2
# /oreon:reqs
%description -n python3-id

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir id-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-id usr/lib/python3*/site-packages/id* usr/lib64/python3*/site-packages/id* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/id* usr/lib64/python3*/site-packages/id* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-id -f %{oreon_filedir}/python3-id.list

%changelog

%autochangelog
