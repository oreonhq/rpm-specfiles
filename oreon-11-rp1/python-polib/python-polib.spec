%global source0_hash f3ef94aefed6e183e342a8a269ae1fc4742ba193186ad76f175938621dbfc26b

Name:           python-polib
Version:        1.2.0
Release:        1%{?dist}
Summary:        Library for manipulating gettext catalogs
License:        MIT
URL:            https://polib.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/10/9a/79b1067d27e38ddf84fe7da6ec516f1743f31f752c6122193e7bce38bdbf/polib-1.2.0.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
Python library for reading and writing gettext PO and MO catalogs.

%package -n python3-polib
Summary:        %{summary}

%description -n python3-polib
Python library for reading and writing gettext PO and MO catalogs.

%prep
test "$(sha256sum %{SOURCE0} | cut -d ' ' -f 1)" = "%{source0_hash}"
%autosetup -n polib-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files polib

%check
%pyproject_check_import

%files -n python3-polib -f %{pyproject_files}
%license LICENSE
%doc README.rst
