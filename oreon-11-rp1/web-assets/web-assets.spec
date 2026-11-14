# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: MIT

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: web-assets
Version: 1
Release: 1%{?dist}
Summary: Shared web asset filesystem layout and devel macros
License: MIT
URL: https://oreonhq.com/
BuildArch: noarch

BuildRequires: oreon-rpm-macros

Provides: web-assets-filesystem = %{version}-%{release}
Provides: web-assets-devel = %{version}-%{release}

%description
Filesystem layout under %%{_datadir}/javascript and macros used by packages
that install shared web assets.

%prep
:

%build
:

%install
mkdir -p %{buildroot}%{_datadir}/javascript
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.web-assets <<'EOF'
%_webassetdir %{_datadir}/javascript
EOF

%files
%dir %{_datadir}/javascript
%{_rpmconfigdir}/macros.d/macros.web-assets

%changelog
%autochangelog
