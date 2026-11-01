%global source0_hash e87aae032bf07c26f85ac0ed3250998c37621d95f8bd748b31f15b33c45ee995
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: flex
Version: 2.6.4
Release: 1%{?dist}
Summary: Fast lexical analyzer generator
License: BSD-3-Clause-flex
URL: https://github.com/westes/flex
Source0: https://github.com/westes/flex/releases/download/v%{version}/flex-%{version}.tar.gz

Provides: flex-devel = %{version}-%{release}
Provides: flex-static = %{version}-%{release}
Requires: m4

BuildRequires: oreon-rpm-macros
BuildRequires: m4
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: patchelf
%endif

%description
flex generates scanners: programs that recognize lexical patterns in
text.

%prep
%oreon_sha256
%autosetup -n flex-%{version} -p1

%build
export CFLAGS="${CFLAGS:-} -D_GNU_SOURCE"
%oreon_configure --disable-nls --disable-shared --disable-bootstrap
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
ln -sf flex %{buildroot}%{_bindir}/lex
rm -rf %{buildroot}%{_datadir}/doc/flex
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
