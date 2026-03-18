# SPDX-License-Identifier: MIT
# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>

%bcond tests 1

Name:           forge-srpm-macros
Version:        0.4.0
Release:        4%{?dist}
Summary:        Macros to simplify packaging of forge-hosted projects

License:        GPL-1.0-or-later
URL:            https://git.sr.ht/~gotmax23/forge-srpm-macros
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pyyaml
# For %%pytest definition
BuildRequires:  python3-rpm-macros
%endif

# We require macros and lua defined in redhat-rpm-config
# We constrain this to the version released after the code was split out that
# doesn't contain the same files.
%if (0%{?fedora} >= 40 || 0%{?rhel} >= 10)
Requires:       redhat-rpm-config >= 266-1
%elif 0%{?fedora} == 39
Requires:       redhat-rpm-config >= 265-1
%else
# For testing purposes on older releases,
# we can depend on any version of redhat-rpm-config.
Requires:       redhat-rpm-config
%endif


%description
%{summary}.


%prep
%autosetup -n %{name}-v%{version}


%build
%if %{defined el9}
%make_build epel9-build
%endif


%install
%make_build \
    DESTDIR=%{buildroot} \
    RPMMACRODIR=%{_rpmmacrodir} RPMLUADIR=%{_rpmluadir} %{?el9:epel9-}install


%check
%if %{with tests}
export MACRO_DIR=%{buildroot}%{_rpmmacrodir}
export MACRO_LUA_DIR="%{buildroot}%{_rpmluadir}"
%pytest
%endif


%files
%license LICENSES/GPL-1.0-or-later.txt
%doc README.md NEWS.md
%if %{undefined el9}
%{_rpmluadir}/fedora/srpm/forge.lua
%{_rpmmacrodir}/macros.forge
%else
%{_rpmluadir}/fedora/srpm/forge_epel.lua
%{_rpmmacrodir}/macros.zzz-forge_epel
%endif
%{_rpmluadir}/fedora/srpm/_forge_util.lua


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.0-4
- Prepare for Oreon 11 (RP1)
