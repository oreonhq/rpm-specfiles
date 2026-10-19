%global source0_hash 61f0ea345f63d28ab2ff0dc352c22271661b66bf09642db3a4049ac9dbdb0f8d
Name: libatasmart
Version: 0.19
Release:        32%{?dist}
Summary:        ATA S.M.A.R.T. Disk Health Monitoring Library
Source0:        https://0pointer.de/public/libatasmart-%{version}.tar.xz
Patch0:        libatasmart-0.19-wd-fix.patch
License: LGPL-2.1-or-later
Url: http://git.0pointer.de/?p=libatasmart.git;a=summary
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-devel
# /oreon:deps
%description
A small and lightweight parser library for ATA S.M.A.R.T. hard disk
health monitoring.

%package devel
Summary: Development Files for libatasmart Client Development
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: vala
%description devel
Development Files for libatasmart Client Development

%ldconfig_scriptlets

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libatasmart-0.19
%oreon_prep
%build

%configure --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT \( -name *.a -o -name *.la \) -exec rm {} \;
rm $RPM_BUILD_ROOT%{_docdir}/libatasmart/README
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libatasmart-devel -f %{oreon_filedir}/libatasmart-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.19-32
- Import
