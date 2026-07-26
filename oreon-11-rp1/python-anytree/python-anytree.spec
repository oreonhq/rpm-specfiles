%global source0_hash 3f0f93f355a91bc3e6245319bf4c1d50e3416cc7a35cc1133c1ff38306bbccab

%global modname anytree

Name:           python-anytree
Version:        2.8.0
Release:        24%{?dist}
Summary:        Powerful and Lightweight Python Tree Data Structure

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.io/project/anytree
Source0:        %pypi_source %{modname}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Powerful and Lightweight Python Tree Data Structure with various plugins.

%package -n python3-anytree
Summary:        Powerful and Lightweight Python Tree Data Structure

%description -n python3-anytree
Powerful and Lightweight Python Tree Data Structure with various plugins.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{modname}-%{version}
rm -r %{modname}.egg-info
# Prohibit that the file LICENSE will be installed in usr from the python setup
sed -e "/LICENSE/d" -i setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-anytree
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*

%changelog
%autochangelog
