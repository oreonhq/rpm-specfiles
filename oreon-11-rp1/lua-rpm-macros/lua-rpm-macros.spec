%global source0_hash none
%if 0%{?el8}
%bcond_with rpm_macros
%else
%bcond_without rpm_macros
%endif
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global lua_conflict 5.4.0-7
%endif
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%bcond_without requires_generator
%else
%bcond_with requires_generator
%endif
Name:           lua-rpm-macros
Version:        1
Release:        17%{?dist}
Summary:        The common Lua RPM macros
License:        MIT
Source101:      macros.lua
Source102:      macros.lua-srpm
Source103:      lua.attr
Source200:      LICENSE
BuildArch:      noarch
Requires:       lua-srpm-macros = %{version}-%{release}
%{?lua_conflict:Conflicts: lua-devel < %{lua_conflict}}
# oreon:deps

# /oreon:deps
%description
This package contains Lua RPM macros.

You should not need to install this package manually as lua-devel requires it.

%package -n lua-srpm-macros
Summary:        RPM macros for building Lua source packages
Requires:       rpm
%description -n lua-srpm-macros
RPM macros for building Lua source packages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c -T
cp -a %{sources} .
%if %{without rpm_macros}
rm macros.lua
%endif

%build

%install
mkdir -p %{buildroot}%{rpmmacrodir}
install -pm 644 macros.* %{buildroot}%{rpmmacrodir}/
%if %{with requires_generator}
install -Dpm 0644 lua.attr %{buildroot}/%{_fileattrsdir}/lua.attr
%oreon_autofiles lua-srpm-macros usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%if %{with rpm_macros}
%files -f %{oreon_filedir}/main.list
%files -n lua-srpm-macros -f %{oreon_filedir}/lua-srpm-macros.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1-17
- Prepare for Oreon 11 (RP1)
%endif
