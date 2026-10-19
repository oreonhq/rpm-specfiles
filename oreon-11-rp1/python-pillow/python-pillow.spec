%global source0_hash 3b8182a766685eaa002637e28b4ec8d6b18819a0c71f579bf0dbaa5830297cce
Name:           python-pillow
Version:        12.3.0
Release:        1%{?dist}
Summary:        Python Imaging Library _fork_
License:        MIT-CMU
URL:            https://python-pillow.github.io
Source0:        https://files.pythonhosted.org/packages/source/p/pillow/pillow-%{version}.tar.gz
Patch0:         pillow_mingw.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-pillow = %{version}-%{release}
# /oreon:deps
%package -n       python3-pillow+docs
Summary:        Metapackage for python3-pillow docs extras
Requires:       python3-pillow = %{version}-%{release}
Requires:       python3dist(sphinx) >= 8.2
Provides:       python3dist(pillow[docs]) = %{version}-%{release}

%description -n python3-pillow+docs
Metapackage for python3-pillow docs extras.

%package -n       python3-pillow+fpx
Summary:        Metapackage for python3-pillow fpx extras
Requires:       python3-pillow = %{version}-%{release}
Provides:       python3dist(pillow[fpx]) = %{version}-%{release}

%description -n python3-pillow+fpx
Metapackage for python3-pillow fpx extras.

%package -n       python3-pillow+mic
Summary:        Metapackage for python3-pillow mic extras
Requires:       python3-pillow = %{version}-%{release}
Provides:       python3dist(pillow[mic]) = %{version}-%{release}

%description -n python3-pillow+mic
Metapackage for python3-pillow mic extras.

%package -n       python3-pillow+test-arrow
Summary:        Metapackage for python3-pillow test-arrow extras
Requires:       python3-pillow = %{version}-%{release}
Provides:       python3dist(pillow[test-arrow]) = %{version}-%{release}

%description -n python3-pillow+test-arrow
Metapackage for python3-pillow test-arrow extras.

%package -n       python3-pillow+tests
Summary:        Metapackage for python3-pillow tests extras
Requires:       python3-pillow = %{version}-%{release}
Requires:       python3dist(coverage) >= 7.4.2
Requires:       python3dist(trove-classifiers) >= 2024.10.12
Provides:       python3dist(pillow[tests]) = %{version}-%{release}

%description -n python3-pillow+tests
Metapackage for python3-pillow tests extras.

%package -n       python3-pillow+xmp
Summary:        Metapackage for python3-pillow xmp extras
Requires:       python3-pillow = %{version}-%{release}
Provides:       python3dist(pillow[xmp]) = %{version}-%{release}

%description -n python3-pillow+xmp
Metapackage for python3-pillow xmp extras.

%description

%package -n     python3-pillow
Summary:        Python Imaging Library _fork_
%description -n python3-pillow

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pillow-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pillow usr/lib/python3*/site-packages/pillow* usr/lib64/python3*/site-packages/pillow* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pillow* usr/lib64/python3*/site-packages/pillow* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pillow -f %{oreon_filedir}/python3-pillow.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12.1.1-1
- Prepare for Oreon 11 (RP1)
