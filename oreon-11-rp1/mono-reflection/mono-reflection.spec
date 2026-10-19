%global source0_hash d710ea8d529fbd510427f6b1be832b84a9f63197c20d112a4fac41689255821d
%global debug_package %{nil}
%global gitrev 304d1d
%global gitdate 20110613
Name:		mono-reflection
Version:	1.1
Release:        1%{?dist}
Summary:        Helper library for Mono Reflection support
URL:		https://github.com/jbevain/mono.reflection
License:	MIT
Source0:        %{name}-%{gitdate}git%{gitrev}.tar.bz2
Source1:	mono-reflection.pc
Source2:	mono-reflection-make-git-snapshot.sh
Patch0:		mono-reflection-build.patch
ExclusiveArch: %mono_arches
# oreon:deps
BuildRequires:  make
BuildRequires:  mono-devel
# /oreon:deps
%description
Helper library for Mono Reflection support.

%package devel
Summary:	Development files for Mono.Reflection library
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
%description devel
Development files for Mono.Reflection library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mono-reflection-%{gitdate}
%patch -P0 -p1
chmod -x README
sed -i 's/\r//' README

# Delete bundled DLL
rm -rf Test/target.dll

%build

cp -a /etc/pki/mono/mono.snk Mono.Reflection.snk
make LIBDIR=%{_libdir}
%install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cp -p %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig
sed -i -e 's!@libdir@!%{_libdir}!' $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/mono-reflection.pc
mkdir -p %{buildroot}%{_prefix}/lib/mono/gac/
gacutil -i bin/Mono.Reflection.dll -f -package Mono.Reflection -root %{buildroot}%{_prefix}/lib
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mono-reflection-devel -f %{oreon_filedir}/mono-reflection-devel.list

%changelog

%autochangelog
