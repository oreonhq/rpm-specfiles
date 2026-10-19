%global source0_hash 7b40430f8368a9ac130d441d43aa50944b4165c8c44fc49b752836bd8e822b4b
Name:           python-freeqdsk
Version:        0.5.2
Release:        1%{?dist}
Summary:        Read and write G-EQDSK, A-EQDSK, and P-EQDSK file formats
License:        MIT
URL:            https://github.com/freegs-plasma/FreeQDSK
Source0:        https://files.pythonhosted.org/packages/source/f/freeqdsk/freeqdsk-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 65
BuildRequires:  python3dist(setuptools-scm[toml]) >= 8
BuildRequires:  python3dist(wheel) >= 0.29.0
Requires:       python3-freeqdsk = %{version}-%{release}
# /oreon:deps
%package -n       python3-freeqdsk+tests
Summary:        Metapackage for python3-freeqdsk tests extras
Requires:       python3-freeqdsk = %{version}-%{release}
Requires:       python3dist(pytest) >= 3.3.0
Provides:       python3dist(freeqdsk[tests]) = %{version}-%{release}

%description -n python3-freeqdsk+tests
Metapackage for python3-freeqdsk tests extras.

%package -n       python3-freeqdsk+docs
Summary:        Metapackage for python3-freeqdsk docs extras
Requires:       python3-freeqdsk = %{version}-%{release}
Requires:       python3dist(sphinx) >= 5.3
Requires:       python3dist(sphinx-book-theme) >= 0.4.0rc1
Requires:       python3dist(sphinx-autodoc-typehints) >= 1.19
Provides:       python3dist(freeqdsk[docs]) = %{version}-%{release}

%description -n python3-freeqdsk+docs
Metapackage for python3-freeqdsk docs extras.

%package -n       python3-freeqdsk+dev
Summary:        Metapackage for python3-freeqdsk dev extras
Requires:       python3-freeqdsk = %{version}-%{release}
Provides:       python3dist(freeqdsk[dev]) = %{version}-%{release}

%description -n python3-freeqdsk+dev
Metapackage for python3-freeqdsk dev extras.

%description

%package -n python3-freeqdsk
Summary:        Read and write G-EQDSK, A-EQDSK, and P-EQDSK file formats
# oreon:reqs
Requires:       python3dist(fortranformat) >= 2.0
Requires:       python3dist(numpy) >= 1.22
# /oreon:reqs
%description -n python3-freeqdsk

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir freeqdsk-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-freeqdsk usr/lib/python3*/site-packages/freeqdsk* usr/lib64/python3*/site-packages/freeqdsk* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/freeqdsk* usr/lib64/python3*/site-packages/freeqdsk* usr/bin/*

%check

%pytest
%files
%files -n python3-freeqdsk -f %{oreon_filedir}/python3-freeqdsk.list

%changelog

%autochangelog
