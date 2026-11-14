# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9628e95df682efdea2cebfbb3cba20c891c5e1eceafdce14076665cbbbe379da
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: cargo2rpm
Version: 0.4.0
Release: 1%{?dist}
Summary: Translation layer between cargo and RPM
License: MIT
URL: https://codeberg.org/rust2rpm/cargo2rpm
Source0: https://files.pythonhosted.org/packages/source/c/cargo2rpm/cargo2rpm-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3
BuildRequires: python3-rpm-macros
Requires: python3
Provides: python3dist(cargo2rpm) = %{version}

%description
Turns cargo metadata into rpm names and dependencies.

%prep
%oreon_sha256
%autosetup -n cargo2rpm-%{version}

%build

%install
mkdir -p %{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}
cp -a cargo2rpm %{buildroot}%{python3_sitelib}/
rm -rf %{buildroot}%{python3_sitelib}/cargo2rpm/tests %{buildroot}%{python3_sitelib}/cargo2rpm/testdata
cat > %{buildroot}%{_bindir}/cargo2rpm <<'EOF'
#!/usr/bin/python3
from cargo2rpm.__main__ import main
raise SystemExit(main())
EOF
chmod 0755 %{buildroot}%{_bindir}/cargo2rpm

%files
%license LICENSE
%{_bindir}/cargo2rpm
%{python3_sitelib}/cargo2rpm/

%changelog
%autochangelog
