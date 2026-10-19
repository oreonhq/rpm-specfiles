%global source1_hash e27fc51e3b2666cc1086e08f55a3ae90c5ecef6f6cbb445a374c74d83bf232bf
%global source0_hash 4d96dfc08da13fe6d6c5c3dd13f5c6ee731b6e023e8e9cfe43894d3e211a27c7
%global pkgname LuaJIT
%global luajit_version_major 2
%global luajit_version_minor 1
%global luajit_version_patch 1767980792
%global luajit_version %{luajit_version_major}.%{luajit_version_minor}.%{luajit_version_patch}
Name:           luajit
Version:        %{luajit_version}
%global apiver %(v=%{version}; echo ${v%.${v#[0-9].[0-9].}})
Release:        1%{?dist}
Summary:        Just-In-Time Compiler for Lua
License:        MIT
URL:            http://luajit.org
Source0:        https://github.com/%{pkgname}/%{pkgname}/archive/refs/heads/v%{apiver}/%{pkgname}-%{version}.tar.gz
Source1:        https://github.com/LuaJIT/LuaJIT-test-cleanup/archive/refs/heads/master/LuaJIT-test-cleanup.tar.gz
Source2:        update_tarball.sh
Patch0: luajit-2.1-make-check.patch
Patch1: luajit-2.1-fedora.patch
Patch2: https://github.com/luajit/luajit/pull/631.patch#/luajit-2.1-s390x-support.patch
ExcludeArch:    riscv64 ppc64 ppc64le
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
LuaJIT implements the full set of language features defined by Lua 5.1.
The virtual machine (VM) is API- and ABI-compatible to the standard
Lua interpreter and can be deployed as a drop-in replacement.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{luajit_version_major}.%{luajit_version_minor} -a1

echo "%{luajit_version_patch}" > .relver

ln -s LuaJIT-test-cleanup-master/bench bench
ln -s LuaJIT-test-cleanup-master/test test

# Enable Lua 5.2 features
sed -i -e '/-DLUAJIT_ENABLE_LUA52COMPAT/s/^#//' src/Makefile

# preserve timestamps (cicku)
sed -i -e '/install -m/s/-m/-p -m/' Makefile

%build

make amalg Q= E=@: PREFIX=%{_prefix} TARGET_STRIP=: \
           CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" \
           MULTILIB=%{_lib} \
           %{?_smp_mflags}
%install
%make_install PREFIX=%{_prefix} \
              MULTILIB=%{_lib}
rm -rf _tmp_html ; mkdir _tmp_html
cp -a doc _tmp_html/html
find %{buildroot} -type f -name *.a -delete -print
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n luajit-devel -f %{oreon_filedir}/luajit-devel.list

%changelog

%autochangelog

