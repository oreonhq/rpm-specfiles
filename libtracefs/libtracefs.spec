Name: libtracefs
Version: 1.8.1
Release: 4%{?dist}
License: LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-2.0-only
Summary: Library for access kernel tracefs

URL: https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/
Source0: https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/snapshot/libtracefs-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  xmlto
BuildRequires:  asciidoc
BuildRequires:  pkgconfig(libtraceevent) >= 1.8.0
# The libtracefs is meant to be used by perf, trace-cmd etc. in the future, before it's ready in perf, let's add a conflict
Conflicts: trace-cmd < 2.9.1-6

%description
libtracefs is a library for accessing kernel tracefs

%package devel
Summary: Development headers of %{name}
Requires: %{name}%{_isa} = %{version}-%{release}

%description devel
Development headers of %{name}

%prep
%setup -q

%build
%set_build_flags
# parallel compiling don't always work
make -O -j1 V=1 VERBOSE=1 prefix=%{_prefix} libdir=%{_libdir} all doc

%install
%make_install prefix=%{_prefix} libdir=%{_libdir} install_doc
rm -rf %{buildroot}/%{_libdir}/libtracefs.a

%files
%license LICENSES/LGPL-2.1
%license LICENSES/GPL-2.0
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.8.1
%{_docdir}/libtracefs-doc
%{_mandir}/man1/sqlhist.1.gz
%{_mandir}/man3/libtracefs.3.gz
%{_mandir}/man3/tracefs_*
%files devel
%{_includedir}/tracefs/tracefs.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.1-4
- Prepare for Oreon 11 (RP1)
