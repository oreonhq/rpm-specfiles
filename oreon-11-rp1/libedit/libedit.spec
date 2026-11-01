%global source0_hash 432d5e7ea8b0116dd39f2eca7bc11d0eed77faa6b77ea526ace89907c23ea4a0
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libedit
Version: 3.1
Release: 1%{?dist}
Summary: BSD editline and history library
License: BSD-3-Clause
URL: https://thrysoee.dk/editline/
Source0: https://thrysoee.dk/editline/libedit-20260512-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: ncurses-devel
%endif

%description
Libedit is a command line editing and history library, the BSD alternative
to GNU readline.

%package devel
Summary: Development files for libedit
Requires: libedit%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libedit)

%description devel
Headers and libraries for developing against libedit.

%prep
%oreon_sha256
%autosetup -n libedit-20260512-%{version} -p1

%build
%oreon_configure --disable-static --disable-examples
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_mandir}/man3/history.3*
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
