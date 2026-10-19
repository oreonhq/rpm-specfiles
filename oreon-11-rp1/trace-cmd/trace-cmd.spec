%global source0_hash 2efe103389367e93c764c4a788880ba51018a65dec21b0411965a5f06a6338c1
%global srcversion 3.3.1
Name: trace-cmd
Version: %{srcversion}
Release:        1%{?dist}
License: LGPL-2.1-only AND LGPL-2.1-or-later AND GPL-2.0-only AND GPL-2.0-or-later
Summary:        A user interface to Ftrace
ExcludeArch: %{ix86} %{arm}
URL: http://git.kernel.org/?p=linux/kernel/git/rostedt/trace-cmd.git;a=summary
Source0:        https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/snapshot/trace-cmd-v3.3.1.tar.gz
Source1: trace-cmd.conf
Source2: trace-cmd.service
Source3: 98-trace-cmd.rules
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  audit-libs-devel
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libtracecmd-devel
BuildRequires:  libtraceevent-devel
BuildRequires:  libtracefs-devel
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
# /oreon:deps
%description
trace-cmd is a user interface to Ftrace. Instead of needing to use the
debugfs directly, trace-cmd will handle of setting of options and
tracers and will record into a data file.

%package python3
Summary: Python plugin support for trace-cmd
Requires: trace-cmd%{_isa} = %{version}-%{release}
BuildRequires: python3-devel
%description  python3
Python plugin support for trace-cmd

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-v%{srcversion}
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .

%build

MANPAGE_DOCBOOK_XSL=`rpm -ql docbook-style-xsl | grep manpages/docbook.xsl`
CFLAGS="%{optflags} -D_GNU_SOURCE" LDFLAGS="%{build_ldflags}" BUILD_TYPE=Release \
  make V=9999999999 MANPAGE_DOCBOOK_XSL=$MANPAGE_DOCBOOK_XSL \
  prefix=%{_prefix} libdir=%{_libdir} \
  PYTHON_VERS=python3 all_cmd doc
for i in python/*.py ; do 
    sed -i 's/env python2/python3/g' $i
done
chrpath --delete tracecmd/trace-cmd
%install
make libdir=%{_libdir} prefix=%{_prefix} V=1 DESTDIR=%{buildroot}/ CFLAGS="%{optflags} -D_GNU_SOURCE" LDFLAGS="%{build_ldflags} -z muldefs " BUILD_TYPE=Release install install_doc install_python
find %{buildroot}%{_mandir} -type f | xargs chmod u-x,g-x,o-x
find %{buildroot}%{_datadir} -type f | xargs chmod u-x,g-x,o-x
find %{buildroot}%{_libdir} -type f -iname "*.so" | xargs chmod 0755
mkdir -p -m755 %{buildroot}/%{_sysconfdir}/sysconfig/
mkdir -p -m755 %{buildroot}/%{_unitdir}/
mkdir -p -m755 %{buildroot}/%{_udevrulesdir}/
install -p -m 644 trace-cmd.conf %{buildroot}/%{_sysconfdir}/sysconfig/
install -p -m 644 trace-cmd.service %{buildroot}/%{_unitdir}/
install -p -m 644 98-trace-cmd.rules %{buildroot}/%{_udevrulesdir}/
rm -rf %{buildroot}/%{_docdir}/libtracecmd-doc
rm -rf %{buildroot}/%{_mandir}/man3/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%preun

%systemd_preun %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n trace-cmd-python3 -f %{oreon_filedir}/trace-cmd-python3.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{srcversion}-5
- Prepare for Oreon 11 (RP1)
