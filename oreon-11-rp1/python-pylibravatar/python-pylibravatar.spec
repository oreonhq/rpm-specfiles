%global source0_hash 43da94c8db459cb4bda5673790433c226644604a5ce79dea208b45562c541483

%global eggname pyLibravatar
%global modname libravatar

Name:               python-pylibravatar
Version:            1.6
Release:            44%{?dist}
Summary:            Python module for Libravatar

# The full text of the license isn't shipped
# https://bugs.launchpad.net/pylibravatar/+bug/1173603
License:            MIT
URL:                http://pypi.python.org/pypi/pyLibravatar
Source0:            http://pypi.python.org/packages/source/p/%{eggname}/%{eggname}-%{version}.tar.gz
# https://code.launchpad.net/~ralph-bean/pylibravatar/tcp-dns/+merge/263157
Patch0:             python-pylibravatar-dns-srv-tcp.patch

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-py3dns
BuildRequires:      python3-setuptools

%global _description\
PyLibravatar is an easy way to make use of the federated Libravatar\
avatar hosting service from within your Python applications.

%description %_description

%package -n python3-pylibravatar
Summary:            Python module for Libravatar

Requires:           python3-py3dns

%description -n python3-pylibravatar
PyLibravatar is an easy way to make use of the federated Libravatar
avatar hosting service from within your Python applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{eggname}-%{version}

%patch -P0

# Correct wrong-file-end-of-line-encoding rpmlint issue
sed -i 's/\r//' README.txt
sed -i 's/\r//' Changelog.txt

# Remove bundled egg-info in case it exists
rm -rf %{eggname}.egg-info

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}

%files -n python3-pylibravatar
# Upstream doesn't ship the license full text
# https://bugs.launchpad.net/pylibravatar/+bug/1173603
%doc README.txt Changelog.txt
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/*%{modname}*
%{python3_sitelib}/%{eggname}-%{version}-*

%changelog
%autochangelog
