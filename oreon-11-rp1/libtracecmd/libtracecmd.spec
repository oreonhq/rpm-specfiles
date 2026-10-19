%global source0_hash 55b5039a792d3fd5c6995fc1738136821fc7d1aded59220e9fefbc7d35213d95
Name: libtracecmd
Version: 1.5.2
Release:        6%{?dist}
License: LGPL-2.1-only AND LGPL-2.1-or-later AND GPL-2.0-only AND GPL-2.0-or-later
Summary:        A library for reading tracing instances stored in a trace file
URL: https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/
Source0:        https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/snapshot/trace-cmd-libtracecmd-%{version}.tar.gz
ExcludeArch: %{ix86} %{arm}
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  chrpath
BuildRequires:  doxygen
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  json-c-devel
BuildRequires:  libtraceevent-devel
BuildRequires:  libtracefs-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  xmlto
# /oreon:deps
%description
A library containing functions for getting information and reading
tracing instances stored in a trace file that can be used without the
trace-cmd application.

%package -n libtracecmd-devel
Summary: Development files for libtracecmd
Requires: libtracecmd%{_isa} = %{version}-%{release}
%description -n libtracecmd-devel
Development files of the libtracecmd library

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir trace-cmd-libtracecmd-%{version}
%oreon_prep
%build

MANPAGE_DOCBOOK_XSL=`rpm -ql docbook-style-xsl | grep manpages/docbook.xsl`
CFLAGS="%{optflags} -D_GNU_SOURCE" LDFLAGS="%{build_ldflags}" BUILD_TYPE=Release \
  make V=9999999999 MANPAGE_DOCBOOK_XSL=$MANPAGE_DOCBOOK_XSL \
  prefix=%{_prefix} libdir=%{_libdir} %{?_smp_mflags}\
  PYTHON_VERS=python3 libs doc
%install
make libdir=%{_libdir} prefix=%{_prefix} V=1 DESTDIR=%{buildroot}/ CFLAGS="%{optflags} -D_GNU_SOURCE" LDFLAGS="%{build_ldflags} -z muldefs " BUILD_TYPE=Release install_libs install_doc
find %{buildroot}%{_mandir} -iname trace-cmd\* -exec rm -rf {} \;
rm -rf %{buildroot}/%{_docdir}/trace-cmd
chrpath --delete %{buildroot}/%{_libdir}/libtracecmd.so*
%oreon_autofiles libtracecmd-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libtracecmd-devel -f %{oreon_filedir}/libtracecmd-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.2-6
- Prepare for Oreon 11 (RP1)
