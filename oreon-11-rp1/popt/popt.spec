%global source0_hash c25a4838fc8e4c1c8aacb8bd620edb3084a3d63bf8987fdad3ca2758c63240f9
%global ver 1.19
%global srcver %{ver}%{?snap:-%{snap}}
%global sover 0
Summary:        C library for parsing command line parameters
Name:           popt
Version:        %{ver}%{?snap:~%{snap}}
Release:        1%{?dist}
License:        MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/rpm-software-management/popt/
Source0:        http://ftp.rpm.org/%{name}/releases/%{name}-1.x/%{name}-%{ver}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
# /oreon:deps
%description
Popt is a C library for parsing command line parameters. Popt was
heavily influenced by the getopt() and getopt_long() functions, but
it improves on them by allowing more powerful argument expansion.
Popt can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments. Popt allows command line
arguments to be aliased via configuration files and includes utility
functions for parsing arbitrary strings into argv[] arrays using
shell-like rules.

%package devel
Summary:        Development files for the popt library
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}, pkgconfig
%description devel
The popt-devel package includes header files and libraries necessary
for developing programs which use the popt C library. It contains the
API documentation of the popt library, too.

%if 0%{!?_without_static:1}
%package static
Summary:        Static library for parsing command line parameters
License:        MIT
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description static
The popt-static package includes static libraries of the popt library.
Install it if you need to link statically with libpopt.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{srcver} -p1

%build

%configure %{?_without_static:--disable-static}
%make_build
%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/popt.d/
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check || (cat tests/*.log; exit 1)
%files -f %{oreon_filedir}/main.list
%files -n popt-devel -f %{oreon_filedir}/popt-devel.list
%files -n popt-static -f %{oreon_filedir}/popt-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{ver}%{?snap:~%{snap}}-10
- Prepare for Oreon 11 (RP1)
