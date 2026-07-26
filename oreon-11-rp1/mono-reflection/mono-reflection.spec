%global source0_hash d710ea8d529fbd510427f6b1be832b84a9f63197c20d112a4fac41689255821d

%global debug_package %{nil}
%global gitrev 304d1d
%global gitdate 20110613

Name:		mono-reflection
Version:	0.1
Release:	0.34.%{gitdate}git%{gitrev}%{?dist}
Summary:	Helper library for Mono Reflection support
URL:		https://github.com/jbevain/mono.reflection
License:	MIT
# No source tarball, source from git:
# git clone https://github.com/jbevain/mono.reflection.git
# Use ./mono-reflection-make-git-snapshot.sh script to reproduce
Source0:	mono-reflection-%{gitdate}git%{gitrev}.tar.bz2
Source1:	mono-reflection.pc
Source2:	mono-reflection-make-git-snapshot.sh
Patch0:		mono-reflection-build.patch
BuildRequires: make
BuildRequires:	mono-devel

# Mono only available on these:
ExclusiveArch: %mono_arches

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
# Use the mono system key instead of generating our own here.
cp -a /etc/pki/mono/mono.snk Mono.Reflection.snk
make LIBDIR=%{_libdir}

%install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cp -p %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig
sed -i -e 's!@libdir@!%{_libdir}!' $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/mono-reflection.pc
mkdir -p %{buildroot}%{_prefix}/lib/mono/gac/
gacutil -i bin/Mono.Reflection.dll -f -package Mono.Reflection -root %{buildroot}%{_prefix}/lib

%files
%doc README
%{_prefix}/lib/mono/gac/Mono.Reflection/
%{_prefix}/lib/mono/Mono.Reflection/

%files devel
%{_libdir}/pkgconfig/mono-reflection.pc

%changelog
%autochangelog
