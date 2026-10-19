%global source0_hash bbc43aca292369ccc6cbc8a921991ecf2538a3587ab5a116eff06c321d647155
Name:           python-pypdf
Version:        6.19.0
Release:        1%{?dist}
Summary:        A pure-python PDF library capable of splitting, merging, cropping, and transforming PDF files
License:        BSD-3-Clause
URL:            https://github.com/py-pdf/pypdf
Source0:        https://files.pythonhosted.org/packages/source/p/pypdf/pypdf-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 5
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-pypdf = %{version}-%{release}
# /oreon:deps
%package -n       python3-pypdf+crypto
Summary:        Metapackage for python3-pypdf crypto extras
Requires:       python3-pypdf = %{version}-%{release}
Requires:       python3dist(cryptography) > 3.0
Provides:       python3dist(pypdf[crypto]) = %{version}-%{release}

%description -n python3-pypdf+crypto
Metapackage for python3-pypdf crypto extras.

%package -n       python3-pypdf+cryptodome
Summary:        Metapackage for python3-pypdf cryptodome extras
Requires:       python3-pypdf = %{version}-%{release}
Provides:       python3dist(pypdf[cryptodome]) = %{version}-%{release}

%description -n python3-pypdf+cryptodome
Metapackage for python3-pypdf cryptodome extras.

%package -n       python3-pypdf+fonts
Summary:        Metapackage for python3-pypdf fonts extras
Requires:       python3-pypdf = %{version}-%{release}
Provides:       python3dist(pypdf[fonts]) = %{version}-%{release}

%description -n python3-pypdf+fonts
Metapackage for python3-pypdf fonts extras.

%package -n       python3-pypdf+image
Summary:        Metapackage for python3-pypdf image extras
Requires:       python3-pypdf = %{version}-%{release}
Requires:       python3dist(pillow) >= 8.0.0
Provides:       python3dist(pypdf[image]) = %{version}-%{release}

%description -n python3-pypdf+image
Metapackage for python3-pypdf image extras.

%package -n       python3-pypdf+rtl_text
Summary:        Metapackage for python3-pypdf rtl_text extras
Requires:       python3-pypdf = %{version}-%{release}
Provides:       python3dist(pypdf[rtl_text]) = %{version}-%{release}

%description -n python3-pypdf+rtl_text
Metapackage for python3-pypdf rtl_text extras.

%package -n       python3-pypdf+full
Summary:        Metapackage for python3-pypdf full extras
Requires:       python3-pypdf = %{version}-%{release}
Requires:       python3dist(cryptography) > 3.0
Requires:       python3dist(pillow) >= 8.0.0
Provides:       python3dist(pypdf[full]) = %{version}-%{release}

%description -n python3-pypdf+full
Metapackage for python3-pypdf full extras.

%package -n       python3-pypdf+dev
Summary:        Metapackage for python3-pypdf dev extras
Requires:       python3-pypdf = %{version}-%{release}
Provides:       python3dist(pypdf[dev]) = %{version}-%{release}

%description -n python3-pypdf+dev
Metapackage for python3-pypdf dev extras.

%package -n       python3-pypdf+docs
Summary:        Metapackage for python3-pypdf docs extras
Requires:       python3-pypdf = %{version}-%{release}
Provides:       python3dist(pypdf[docs]) = %{version}-%{release}

%description -n python3-pypdf+docs
Metapackage for python3-pypdf docs extras.

%description

%package -n     python3-pypdf
Summary:        A pure-python PDF library capable of splitting, merging, cropping, and transforming PDF files
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.0
# /oreon:reqs
%description -n python3-pypdf

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pypdf-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pypdf usr/lib/python3*/site-packages/pypdf* usr/lib64/python3*/site-packages/pypdf* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pypdf* usr/lib64/python3*/site-packages/pypdf* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pypdf -f %{oreon_filedir}/python3-pypdf.list

%changelog

%autochangelog
