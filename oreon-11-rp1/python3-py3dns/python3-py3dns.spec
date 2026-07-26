%global source0_hash 195d87111a4f984b787fc076f7a4ad512791f0908a5a4c2a7a084ac059715201

%global modname DNS
%global distname py3dns

Name:               python3-py3dns
Version:            4.0.0
Release:            13%{?dist}
Summary:            Python3 DNS library

# Automatically converted from old format: Python - review is highly recommended.
License:            LicenseRef-Callaway-Python
URL:                https://launchpad.net/py3dns/
Source0:            https://pypi.io/packages/source/p/%{distname}/%{distname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel

%generate_buildrequires
%pyproject_buildrequires

%description
This Python 3 module provides a DNS API for looking up DNS entries from
within Python 3 modules and applications. This module is a simple,
lightweight implementation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{distname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{distname}.egg-info

# Some files are latin-1 encoded but are incorrectly labelled as UTF-8 by
# upstream (see rhbz:620265)
#
# Convert them to actually be UTF-8, preserving the (now-correct) encoding
# declaration (preserving timestamps):
for file in DNS/Lib.py DNS/Type.py ; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%build
%pyproject_wheel

%install
%pyproject_install

# We cannot actually run the tests in koji because they require network access.
#%%check
#PYTHONPATH=$(pwd) %%{__python3} tests/test.py
#PYTHONPATH=$(pwd) %%{__python3} tests/test2.py
#PYTHONPATH=$(pwd) %%{__python3} tests/test4.py
##PYTHONPATH=$(pwd) %%{__python3} tests/test5.py somedomain.com
#PYTHONPATH=$(pwd) %%{__python3} tests/testPackers.py
#PYTHONPATH=$(pwd) %%{__python3} tests/testsrv.py

%files
%doc README.txt README-guido.txt LICENSE CREDITS.txt CHANGES
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{distname}-%{version}*

%changelog
%autochangelog
