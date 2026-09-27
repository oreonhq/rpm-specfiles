%global source0_hash 2f29ef331735ce958efa4734873f084941970894c6090408b079c61b2e1c06d1

BuildRequires:  python3dist(sphinx)
Name:           python-sphinxcontrib-applehelp
Version:        2.0.0
Release:        1%{?dist}
Summary:        Sphinx extension for Apple Help output
License:        BSD-2-Clause
URL:            https://www.sphinx-doc.org/
Source0:        https://files.pythonhosted.org/packages/ba/6e/b837e84a1a704953c62ef8776d45c3e8d759876b4a84fe14eba2859106fe/sphinxcontrib_applehelp-2.0.0.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
Sphinx extension for Apple Help output.

%package -n python3-sphinxcontrib-applehelp
Requires:       python3dist(sphinx)
Summary:        %{summary}

%description -n python3-sphinxcontrib-applehelp
Sphinx extension for Apple Help output.

%prep
test "$(sha256sum %{SOURCE0} | cut -d ' ' -f 1)" = "%{source0_hash}"
%autosetup -n sphinxcontrib_applehelp-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinxcontrib

%check
%pyproject_check_import

%files -n python3-sphinxcontrib-applehelp -f %{pyproject_files}
%license LICENCE.rst
