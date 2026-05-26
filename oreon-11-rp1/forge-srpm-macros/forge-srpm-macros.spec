# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 7b0d7aee291273ae02b661d14330e4e803ab6b673cd4aec39c0a00a5de2b793d
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# SPDX-License-Identifier: MIT
# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>

%bcond tests 1

Name:           forge-srpm-macros
Version:        0.4.0
Release:        4%{?dist}
Summary:        Macros to simplify packaging of forge-hosted projects

License:        GPL-1.0-or-later
URL:            https://git.sr.ht/~gotmax23/forge-srpm-macros
Source0:        https://git.sr.ht/~gotmax23/forge-srpm-macros/archive/v0.4.0.tar.gz#/forge-srpm-macros-0.4.0.tar.gz

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
%if (0%{?fedora} >= 40 || 0%{?rhel} >= 10) || 0%{?oreon}
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
%oreon_verify_sources
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.0-4
- Import
