%global source0_hash 4f18ddae154e793e46eeab727c59ef1c0c0c2b744e7b94219710d76f530629ae
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: lua
Version: 5.4.8
Release: 1%{?dist}
Summary: Lua programming language
License: MIT
URL: https://www.lua.org/
Source0: https://www.lua.org/ftp/lua-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: readline-devel
BuildRequires: patchelf
%endif

%description
Lua is a programming language.

%package devel
Summary: Lua programming language
Requires: lua%{?_isa} = %{version}-%{release}

%description devel
Lua is a programming language.

%prep
%oreon_sha256
%autosetup -n lua-%{version} -p1

%build
make linux MYCFLAGS="%{_oreon_cflags} -fPIC" MYLDFLAGS="%{_oreon_ldflags}"
gcc -shared -Wl,-soname,liblua-5.4.so -o liblua-5.4.so $(find src -name '*.o' ! -name lua.o ! -name luac.o) -lm -ldl %{_oreon_ldflags}

%install
make install INSTALL_TOP=%{buildroot}%{_prefix} INSTALL_LIB=%{buildroot}%{_libdir} INSTALL_MAN=%{buildroot}%{_mandir}/man1
cp -a liblua-5.4.so %{buildroot}%{_libdir}/
ln -sf liblua-5.4.so %{buildroot}%{_libdir}/liblua.so
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license README

%files devel -f %{_builddir}/%{name}-devel.files
