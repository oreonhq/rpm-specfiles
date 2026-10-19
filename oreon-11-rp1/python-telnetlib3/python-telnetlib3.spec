%global source0_hash 6fde197ffb71cf26ad27fe2c88694d8364f4b1cc962a37762e0cf7e79b9afaed
Name:           python-telnetlib3
Version:        5.0.1
Release:        1%{?dist}
Summary:        Python Telnet server and client CLI and Protocol library
License:        ISC
URL:            https://github.com/jquast/telnetlib3
Source0:        https://files.pythonhosted.org/packages/source/t/telnetlib3/telnetlib3-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-telnetlib3 = %{version}-%{release}
# /oreon:deps
%package -n       python3-telnetlib3+docs
Summary:        Metapackage for python3-telnetlib3 docs extras
Requires:       python3-telnetlib3 = %{version}-%{release}
Requires:       python3dist(sphinx) > 3
Provides:       python3dist(telnetlib3[docs]) = %{version}-%{release}

%description -n python3-telnetlib3+docs
Metapackage for python3-telnetlib3 docs extras.

%package -n       python3-telnetlib3+extras
Summary:        Metapackage for python3-telnetlib3 extras extras
Requires:       python3-telnetlib3 = %{version}-%{release}
Requires:       python3dist(blessed) >= 1.41
Requires:       python3dist(prettytable) >= 3.17
Requires:       python3dist(prettytable) < 4
Requires:       python3dist(ucs-detect) >= 2
Requires:       python3dist(ucs-detect) < 3
Provides:       python3dist(telnetlib3[extras]) = %{version}-%{release}

%description -n python3-telnetlib3+extras
Metapackage for python3-telnetlib3 extras extras.

%description

%package -n     python3-telnetlib3
Summary:        Python Telnet server and client CLI and Protocol library
# oreon:reqs
Requires:       python3dist(blessed) >= 1.41
Requires:       python3dist(wcwidth) >= 0.6.0
# /oreon:reqs
%description -n python3-telnetlib3

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir telnetlib3-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-telnetlib3 usr/lib/python3*/site-packages/telnetlib3* usr/lib64/python3*/site-packages/telnetlib3* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/telnetlib3* usr/lib64/python3*/site-packages/telnetlib3* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-telnetlib3 -f %{oreon_filedir}/python3-telnetlib3.list

%changelog

%autochangelog
