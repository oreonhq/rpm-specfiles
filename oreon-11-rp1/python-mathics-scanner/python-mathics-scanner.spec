%global source0_hash 0424ae0918313640af52a7bbadc91824ca1869eb1ad0e0dd87c784c141326d9a
Name:           python-mathics-scanner
Version:        2.0.0
Release:        1%{?dist}
Summary:        Character Tables and Tokenizer for Mathics and the Wolfram Language.
License:        GPL-3.0-or-later
URL:            https://mathics.org/
Source0:        https://files.pythonhosted.org/packages/source/m/mathics_scanner/mathics_scanner-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mathics-scanner = %{version}-%{release}
# /oreon:deps
%package -n       python3-mathics-scanner+dev
Summary:        Metapackage for python3-mathics-scanner dev extras
Requires:       python3-mathics-scanner = %{version}-%{release}
Provides:       python3dist(mathics-scanner[dev]) = %{version}-%{release}

%description -n python3-mathics-scanner+dev
Metapackage for python3-mathics-scanner dev extras.

%package -n       python3-mathics-scanner+full
Summary:        Metapackage for python3-mathics-scanner full extras
Requires:       python3-mathics-scanner = %{version}-%{release}
Provides:       python3dist(mathics-scanner[full]) = %{version}-%{release}

%description -n python3-mathics-scanner+full
Metapackage for python3-mathics-scanner full extras.

%description

%package -n     python3-mathics-scanner
Summary:        Character Tables and Tokenizer for Mathics and the Wolfram Language.
%description -n python3-mathics-scanner

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir mathics_scanner-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mathics-scanner usr/lib/python3*/site-packages/mathics_scanner* usr/lib64/python3*/site-packages/mathics_scanner* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mathics_scanner* usr/lib64/python3*/site-packages/mathics_scanner* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mathics-scanner -f %{oreon_filedir}/python3-mathics-scanner.list

%changelog

%autochangelog
