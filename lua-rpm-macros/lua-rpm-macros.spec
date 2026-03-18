%if 0%{?el8}
# RHEL8's lua-devel ships macros.lua and lua.attr
# skip shipping lua-rpm-macros so we don't conflict
%bcond_with rpm_macros
%else
%bcond_without rpm_macros
%endif

# Versions of lua-devel where the macros were removed
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global lua_conflict 5.4.0-7
%endif
# TODO add new versions if this gets backported

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
# requires RPM >= 4.16
%bcond_without requires_generator
%else
%bcond_with requires_generator
%endif

Name:           lua-rpm-macros
Version:        1
Release:        17%{?dist}
Summary:        The common Lua RPM macros

License:        MIT

# Macros:
Source101:      macros.lua
Source102:      macros.lua-srpm

# RPM requires generator
Source103:      lua.attr

# license text
Source200:      LICENSE

BuildArch:      noarch

# for lua_libdir and lua_pkgdir
Requires:       lua-srpm-macros = %{version}-%{release}

# files were moved from here
%{?lua_conflict:Conflicts: lua-devel < %{lua_conflict}}

%description
This package contains Lua RPM macros.

You should not need to install this package manually as lua-devel requires it.


%package -n lua-srpm-macros
Summary:        RPM macros for building Lua source packages

# For directory structure
Requires:       rpm

%description -n lua-srpm-macros
RPM macros for building Lua source packages.


%prep
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
%endif


%if %{with rpm_macros}
%files
%license LICENSE
%if %{with requires_generator}
%{_fileattrsdir}/lua.attr
%endif
%{rpmmacrodir}/macros.lua
%endif

%files -n lua-srpm-macros
%license LICENSE
%{rpmmacrodir}/macros.lua-srpm


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1-17
- Prepare for Oreon 11 (RP1)
