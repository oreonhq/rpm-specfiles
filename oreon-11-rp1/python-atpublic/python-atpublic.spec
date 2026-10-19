%global source0_hash 466ef10d0c8bbd14fd02a5fbd5a8b6af6a846373d91106d3a07c16d72d96b63e
%global debug_package %{nil}
Summary:        Decorator for populating a Python module's __all__
License:        Apache-2.0
URL:            https://gitlab.com/warsaw/public
Source0:        https://files.pythonhosted.org/packages/source/a/atpublic/atpublic-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-atpublic = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-atpublic
Summary:        Decorator for populating a Python module's __all__
Requires:       python3-setuptools
%description -n python3-atpublic

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir public-%{version}
%oreon_prep
%build

export ATPUBLIC_BUILD_EXTENSION=1
%pyproject_wheel
%install
export ATPUBLIC_BUILD_EXTENSION=1
%pyproject_install
%oreon_autofiles python3-atpublic usr/lib/python3*/site-packages/atpublic* usr/lib64/python3*/site-packages/atpublic* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/atpublic* usr/lib64/python3*/site-packages/atpublic* usr/bin/*

%check

%pytest
%files
%files -n python3-atpublic -f %{oreon_filedir}/python3-atpublic.list

%changelog

%autochangelog
