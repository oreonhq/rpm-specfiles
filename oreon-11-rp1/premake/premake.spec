%global source0_hash b6b6aa786934a86510f6b567219e5b74b5181aabb9db12181f44f8dd6c5ba1cb
%global debug_package %{nil}
%global forgeurl https://github.com/premake/premake-core
%global date 20251127
%global commit e38ef3f7d23b24984228ce605f7885ec32f7958d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%forgemeta
Name:           premake
Version:        5.0.0
Release:        1%{?dist}
Summary:        Cross-platform build configuration tool
License:        BSD-3-Clause
URL:            https://premake.github.io/
Source0:        %{forgeurl}/archive/%{commit}/%{name}-core-%{commit}.tar.gz
ExcludeArch:    s390x
# oreon:deps
BuildRequires:  compat-lua-devel
BuildRequires:  gcc
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  readline-devel
# /oreon:deps
%description
Premake is a command line utility which reads a scripted definition of a
software project, then uses it to perform build configuration tasks or generate
project files for toolsets like Visual Studio, Xcode, and GNU Make. Premake's
scripts are little Lua programs, so the sky's the limit!

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

make -f Bootstrap.mak linux
%install
install -pDm 755 bin/release/premake5 %{buildroot}/%{_bindir}/premake5
install -pDm 644 packages/debian/premake.1 %{buildroot}%{_mandir}/man1/premake5.1
%oreon_autofiles main

%check

%ifnarch aarch64 s390x riscv64
bin/release/premake5 test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
