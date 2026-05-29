%global source0_hash none

%global ver 1.19
#%%global snap rc1
%global srcver %{ver}%{?snap:-%{snap}}
%global sover 0

Summary:        C library for parsing command line parameters
Name:           popt
Version:        %{ver}%{?snap:~%{snap}}
Release:        10%{?dist}
# COPYING:      MIT text
# po/eo.po:     LicenseRef-Fedora-Public-Domain
# po/fi.po:     MIT AND LicenseRef-Fedora-Public-Domain
# po/lv.po:     MIT AND LicenseRef-Fedora-Public-Domain
# popt.3:       MIT ("the X consortium license, see the file COPYING")
License:        MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/rpm-software-management/popt/
Source0:        http://ftp.rpm.org/popt/releases/popt-1.x/popt-1.19%{?snap:-%{snap}}.tar.gz
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{name}-%{srcver} -p1

%build
%configure %{?_without_static:--disable-static}
%make_build

%install
%make_install

# Multiple popt configurations are possible
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/popt.d/

%find_lang %{name}

%check
make check || (cat tests/*.log; exit 1)

%files -f %{name}.lang
%license COPYING
%{_sysconfdir}/popt.d/
%{_libdir}/libpopt.so.%{sover}*

%files devel
%doc README
%{_libdir}/libpopt.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/popt.h
%{_mandir}/man3/popt.3*

%if 0%{!?_without_static:1}
%files static
%{_libdir}/libpopt.a
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{ver}%{?snap:~%{snap}}-10
- Prepare for Oreon 11 (RP1)
