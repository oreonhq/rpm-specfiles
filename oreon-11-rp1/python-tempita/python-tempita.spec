%global source0_hash cacecf0baa674d356641f1d406b8bff1d756d739c46b869a54de515d08e6fc9c

Name:           python-tempita
Version:        0.5.2
Release:        20%{?dist}
Summary:        A very small text templating language

License:        MIT
URL:            http://pythonpaste.org/tempita/
Source0:        https://pypi.python.org/packages/source/T/Tempita/Tempita-%{version}.tar.gz
Patch0001:      0001-Apply-fixes-required-for-Python-3.patch

BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

%global _description\
Tempita is a small templating language for text substitution.

%description %_description

%package -n python3-tempita
Summary:        A very small text templating language
%{?python_provide:%python_provide python3-tempita}
# Without one of these there's no aes implementation which means there's no way to
# have encrypted cookies.  This is a reduction in features over the python2 version.
# Currently there's no working python3 port for either:
# http://allmydata.org/trac/pycryptopp/ticket/35
# http://lists.dlitz.net/pipermail/pycrypto/2010q2/000253.html
#%if 0%{?fedora}
#Requires: python3-pycryptopp
#%else
#Requires: python3-crypto
#%endif

%description -n python3-tempita
Tempita is a small templating language for text substitution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Tempita-%{version} -p1
# Since Setuptools 58+ upstream removed support for 2to3
sed -i '/use_2to3/d' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-tempita
%{python3_sitelib}/tempita/
%{python3_sitelib}/*.egg-info/

%changelog
%autochangelog
