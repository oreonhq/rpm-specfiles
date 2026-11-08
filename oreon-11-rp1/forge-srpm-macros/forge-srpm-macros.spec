# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7b0d7aee291273ae02b661d14330e4e803ab6b673cd4aec39c0a00a5de2b793d

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
# SPDX-License-Identifier: MIT
# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>

%bcond tests 1

Name:           forge-srpm-macros
Version:        0.4.0
Release:        1%{?dist}
Summary:        Macros to simplify packaging of forge-hosted projects

License:        GPL-1.0-or-later
URL:            https://git.sr.ht/~gotmax23/forge-srpm-macros
Source0:        https://git.sr.ht/~gotmax23/forge-srpm-macros/archive/v%{version}.tar.gz#/forge-srpm-macros-%{version}.tar.gz
Source100:      https://files.pythonhosted.org/packages/05/8e/961c0007c59b8dd7729d542c61a4d537767a59645b82a0b521206e1e25c2/pyyaml-6.0.3.tar.gz

BuildArch:      noarch

BuildRequires:  make
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pyyaml
# For %%pytest definition
BuildRequires:  python3-rpm-macros
BuildRequires:  oreon-rpm-macros
%endif

# We require macros and lua defined in redhat-rpm-config
# We constrain this to the version released after the code was split out that
# doesn't contain the same files.
Requires:       redhat-rpm-config >= 266-1


%description
%{summary}.


%prep
%oreon_sha256

%autosetup -n %{name}-v%{version}
find . -type f \( -name '*.lua' -o -name 'macros*' \) -print0 | \
  xargs -0 sed -i \
    -e 's/fedora\.common/oreon.common/g' \
    -e 's/fedora\.srpm/oreon.srpm/g'
sed -i 's|fedora/srpm|oreon/srpm|g' Makefile
mkdir -p rpm/lua/oreon
mv rpm/lua/fedora/srpm rpm/lua/oreon/srpm


%build

%install
%make_build \
    DESTDIR=%{buildroot} \
    RPMMACRODIR=%{_rpmmacrodir} RPMLUADIR=%{_rpmluadir} install


%check
%if %{with tests}
echo "d76623373421df22fb4cf8817020cbb7ef15c725b9d5e45f17e189bfc384190f  %{SOURCE100}" | sha256sum -c -
tar -xzf %{SOURCE100} -C %{_builddir}
export PYTHONPATH="%{_builddir}/pyyaml-6.0.3/lib${PYTHONPATH:+:$PYTHONPATH}"
export MACRO_DIR=%{buildroot}%{_rpmmacrodir}
export MACRO_LUA_DIR="%{buildroot}%{_rpmluadir}"
%pytest
%endif


%files
%license LICENSES/GPL-1.0-or-later.txt
%doc README.md NEWS.md
%{_rpmluadir}/oreon/srpm/forge.lua
%{_rpmmacrodir}/macros.forge
%{_rpmluadir}/oreon/srpm/_forge_util.lua


