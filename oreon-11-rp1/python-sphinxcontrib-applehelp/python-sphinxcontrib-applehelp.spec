%global source0_hash 2f29ef331735ce958efa4734873f084941970894c6090408b079c61b2e1c06d1
Name:           python-sphinxcontrib-applehelp
Version:        2.0.0
Release:        1%{?dist}
Summary:        Sphinx extension for Apple Help output
License:        BSD-2-Clause
URL:            https://www.sphinx-doc.org/
Source0:        https://files.pythonhosted.org/packages/ba/6e/b837e84a1a704953c62ef8776d45c3e8d759876b4a84fe14eba2859106fe/sphinxcontrib_applehelp-2.0.0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.7
Requires:       python3-sphinxcontrib-applehelp = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinxcontrib-applehelp+test
Summary:        Metapackage for python3-sphinxcontrib-applehelp test extras
Requires:       python3-sphinxcontrib-applehelp = %{version}-%{release}
Provides:       python3dist(sphinxcontrib-applehelp[test]) = %{version}-%{release}

%description -n python3-sphinxcontrib-applehelp+test
Metapackage for python3-sphinxcontrib-applehelp test extras.

%package -n       python3-sphinxcontrib-applehelp+lint
Summary:        Metapackage for python3-sphinxcontrib-applehelp lint extras
Requires:       python3-sphinxcontrib-applehelp = %{version}-%{release}
Requires:       python3dist(ruff) == 0.5.5
Provides:       python3dist(sphinxcontrib-applehelp[lint]) = %{version}-%{release}

%description -n python3-sphinxcontrib-applehelp+lint
Metapackage for python3-sphinxcontrib-applehelp lint extras.

%package -n       python3-sphinxcontrib-applehelp+standalone
Summary:        Metapackage for python3-sphinxcontrib-applehelp standalone extras
Requires:       python3-sphinxcontrib-applehelp = %{version}-%{release}
Requires:       python3dist(sphinx) >= 5
Provides:       python3dist(sphinxcontrib-applehelp[standalone]) = %{version}-%{release}

%description -n python3-sphinxcontrib-applehelp+standalone
Metapackage for python3-sphinxcontrib-applehelp standalone extras.

%description
Sphinx extension for Apple Help output.

%package -n python3-sphinxcontrib-applehelp
Requires:       python3dist(sphinx)
Summary:        Sphinx extension for Apple Help output
%description -n python3-sphinxcontrib-applehelp
Sphinx extension for Apple Help output.

%prep

test "$(sha256sum %{SOURCE0} | cut -d ' ' -f 1)" = "%{source0_hash}"
%autosetup -n sphinxcontrib_applehelp-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinxcontrib-applehelp usr/lib/python3*/site-packages/sphinxcontrib_applehelp* usr/lib64/python3*/site-packages/sphinxcontrib_applehelp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinxcontrib_applehelp* usr/lib64/python3*/site-packages/sphinxcontrib_applehelp* usr/bin/*

%check

%pyproject_check_import

%files
%files -n python3-sphinxcontrib-applehelp -f %{oreon_filedir}/python3-sphinxcontrib-applehelp.list
