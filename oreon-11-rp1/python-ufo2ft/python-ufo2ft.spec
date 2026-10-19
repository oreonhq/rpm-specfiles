%global source0_hash 2fea363d651a78fc00c7ef2f94ae5fb0c843bf53cc76c480f7b5227c7fbe3e2d
Name:           python-ufo2ft
Version:        3.9.0
Release:        1%{?dist}
Summary:        A bridge between UFOs and FontTools.
License:        MIT
URL:            https://github.com/googlefonts/ufo2ft
Source0:        https://files.pythonhosted.org/packages/source/u/ufo2ft/ufo2ft-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-ufo2ft = %{version}-%{release}
# /oreon:deps
%package -n       python3-ufo2ft+compreffor
Summary:        Metapackage for python3-ufo2ft compreffor extras
Requires:       python3-ufo2ft = %{version}-%{release}
Requires:       python3dist(compreffor) >= 0.6.0
Provides:       python3dist(ufo2ft[compreffor]) = %{version}-%{release}

%description -n python3-ufo2ft+compreffor
Metapackage for python3-ufo2ft compreffor extras.

%package -n       python3-ufo2ft+cffsubr
Summary:        Metapackage for python3-ufo2ft cffsubr extras
Requires:       python3-ufo2ft = %{version}-%{release}
Provides:       python3dist(ufo2ft[cffsubr]) = %{version}-%{release}

%description -n python3-ufo2ft+cffsubr
Metapackage for python3-ufo2ft cffsubr extras.

%package -n       python3-ufo2ft+dev
Summary:        Metapackage for python3-ufo2ft dev extras
Requires:       python3-ufo2ft = %{version}-%{release}
Provides:       python3dist(ufo2ft[dev]) = %{version}-%{release}

%description -n python3-ufo2ft+dev
Metapackage for python3-ufo2ft dev extras.

%package -n       python3-ufo2ft+pathops
Summary:        Metapackage for python3-ufo2ft pathops extras
Requires:       python3-ufo2ft = %{version}-%{release}
Requires:       python3dist(skia-pathops) >= 0.8.0
Provides:       python3dist(ufo2ft[pathops]) = %{version}-%{release}

%description -n python3-ufo2ft+pathops
Metapackage for python3-ufo2ft pathops extras.

%package -n       python3-ufo2ft+test
Summary:        Metapackage for python3-ufo2ft test extras
Requires:       python3-ufo2ft = %{version}-%{release}
Provides:       python3dist(ufo2ft[test]) = %{version}-%{release}

%description -n python3-ufo2ft+test
Metapackage for python3-ufo2ft test extras.

%description

%package -n     python3-ufo2ft
Summary:        A bridge between UFOs and FontTools.
# oreon:reqs
Requires:       python3dist(booleanoperations) >= 0.9.0
Requires:       python3dist(cffsubr) >= 0.3.0
Requires:       python3dist(fontmath) >= 0.9.4
Requires:       python3dist(fonttools[ufo]) >= 4.61.1
# /oreon:reqs
%description -n python3-ufo2ft

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ufo2ft-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ufo2ft usr/lib/python3*/site-packages/ufo2ft* usr/lib64/python3*/site-packages/ufo2ft* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ufo2ft* usr/lib64/python3*/site-packages/ufo2ft* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ufo2ft -f %{oreon_filedir}/python3-ufo2ft.list

%changelog

%autochangelog
