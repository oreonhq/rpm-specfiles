# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 437cfdada284e3c10e7439cdbd0c3180d897f5a218cf156ebfcd170df40b3bc9

%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
Name:           python-rpm-generators
Summary:        Dependency generators for Python RPMs
Version:        14
Release:        1%{?dist}

Url:            https://www.python.org/

# Originally the following files were part of RPM, so the license is inherited: GPL-2.0-or-later
# The COPYING file is grabbed from the last commit that changed the files
Source0:        https://raw.githubusercontent.com/rpm-software-management/rpm/102eab50b3d0d6546dfe082eac0ade21e6b3dbf1/COPYING
Source1:        python.attr
Source2:        pythondist.attr
# This was crafted in-place as a fork of python.attr, hence also GPL-2.0-or-later
Source3:        pythonname.attr
# This one is also originally from RPM, but it has its own license declaration: LGPL-2.1-or-later
Source4:        pythondistdeps.py
# This was crafted in-place with the following license declaration:
Source5:        pythonbundles.py

# See individual licenses above Source declarations
# Originally, this was simplified to GPL-2.0-or-later, but "effective license" analysis is no longer allowed
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND (LicenseRef-Oreon-Public-Domain OR LGPL-2.1-or-later OR GPL-2.0-or-later)

BuildArch:      noarch
BuildRequires:  oreon-rpm-macros

%description
%{summary}.

%package -n python3-rpm-generators
Summary:        %{summary}
Requires:       python3-packaging
# We have parametric macro generators, we need RPM 4.16 (4.15.90+ is 4.16 alpha)
Requires:       rpm > 4.15.90-0
# This contains the Lua functions we use:
Requires:       python-srpm-macros >= 3.10-15

%description -n python3-rpm-generators
%{summary}.

%prep
%oreon_sha256

%autosetup -c -T
cp -a %{sources} .

%install
install -Dpm0644 -t %{buildroot}%{_fileattrsdir} *.attr
install -Dpm0755 -t %{buildroot}%{_rpmconfigdir} *.py

%files -n python3-rpm-generators
%license COPYING
%{_fileattrsdir}/python.attr
%{_fileattrsdir}/pythondist.attr
%{_fileattrsdir}/pythonname.attr
%{_rpmconfigdir}/pythondistdeps.py
%{_rpmconfigdir}/pythonbundles.py

