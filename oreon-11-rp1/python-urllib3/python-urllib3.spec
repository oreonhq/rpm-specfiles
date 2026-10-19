%global source0_hash 63bf2ead4c879426ebf22ef2a781eeb4aa3b4ae798a0435506f8687fd5bb9b63
Name:           python-urllib3
Version:        2.8.0
Release:        1%{?dist}
Summary:        HTTP library with thread-safe connection pooling, file post, and more.
License:        MIT
URL:            https://github.com/urllib3/urllib3/blob/main/CHANGES.rst
Source0:        https://files.pythonhosted.org/packages/source/u/urllib3/urllib3-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatch-vcs) < 0.6.0
BuildRequires:  python3dist(hatch-vcs) >= 0.4.0
BuildRequires:  python3dist(hatchling) < 2
BuildRequires:  python3dist(hatchling) >= 1.27.0
BuildRequires:  python3dist(setuptools-scm) < 11
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-urllib3 = %{version}-%{release}
# /oreon:deps
%package -n       python3-urllib3+brotli
Summary:        Metapackage for python3-urllib3 brotli extras
Requires:       python3-urllib3 = %{version}-%{release}
Requires:       python3dist(brotli) >= 1.2.0
Requires:       python3dist(brotlicffi) >= 1.2.0.0
Provides:       python3dist(urllib3[brotli]) = %{version}-%{release}

%description -n python3-urllib3+brotli
Metapackage for python3-urllib3 brotli extras.

%package -n       python3-urllib3+zstd
Summary:        Metapackage for python3-urllib3 zstd extras
Requires:       python3-urllib3 = %{version}-%{release}
Requires:       python3dist(backports.zstd) >= 1.0.0
Provides:       python3dist(urllib3[zstd]) = %{version}-%{release}

%description -n python3-urllib3+zstd
Metapackage for python3-urllib3 zstd extras.

%package -n       python3-urllib3+socks
Summary:        Metapackage for python3-urllib3 socks extras
Requires:       python3-urllib3 = %{version}-%{release}
Requires:       python3dist(pysocks) >= 1.5.6
Requires:       python3dist(pysocks) < 2.0
Provides:       python3dist(urllib3[socks]) = %{version}-%{release}

%description -n python3-urllib3+socks
Metapackage for python3-urllib3 socks extras.

%package -n       python3-urllib3+h2
Summary:        Metapackage for python3-urllib3 h2 extras
Requires:       python3-urllib3 = %{version}-%{release}
Requires:       python3dist(h2) >= 4
Requires:       python3dist(h2) < 5
Provides:       python3dist(urllib3[h2]) = %{version}-%{release}

%description -n python3-urllib3+h2
Metapackage for python3-urllib3 h2 extras.

%description

%package -n     python3-urllib3
Summary:        HTTP library with thread-safe connection pooling, file post, and more.
%description -n python3-urllib3

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir urllib3-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-urllib3 usr/lib/python3*/site-packages/urllib3* usr/lib64/python3*/site-packages/urllib3* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/urllib3* usr/lib64/python3*/site-packages/urllib3* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-urllib3 -f %{oreon_filedir}/python3-urllib3.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.7.0-1
- Import
