%global source0_hash cc2087a964a82d2e50e8161cf458481ededebb7021e4660410cf53248a4c83a3

Name:           libHX
Version:        3.22
Release:        26%{?dist}
Summary:        Useful collection of routines for C and C++ programming

# Automatically converted from old format: LGPLv2 or LGPLv3 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL:            http://sourceforge.net/projects/libhx/
Source0:        http://downloads.sourceforge.net/libhx/libHX-%{version}.tar.xz
Source1:        http://downloads.sourceforge.net/libhx/libHX-%{version}.tar.asc
Source2:        gpgkey-B56B8B9D9915AA8796EDC013DFFF2CDB19FC338D.gpg

BuildRequires:  perl-interpreter gcc-c++
# For source verification with gpgv
BuildRequires:  gpg xz
BuildRequires: make

%description
libHX is a C library (with some C++ bindings available) that provides data
structures and functions commonly needed, such as maps, deques, linked lists,
string formatting and autoresizing, option and config file parsing, type
checking casts and more.

libHX aids in quickly writing up C and C++ data processing programs, by
consolidating tasks that often happen to be open-coded, such as (simple) config
file reading, option parsing, directory traversal, and others, into a library.
The focus is on reducing the amount of time (and secondarily, the amount of
code) a developer has to spend for otherwise implementing such.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

xzcat %{SOURCE0} | gpgv --quiet --keyring %{SOURCE2} %{SOURCE1} -
%setup -q

%build
# Without --docdir=.. package installs docs into ../libhx
%configure --disable-static --disable-silent-rules  \
  --with-pkgconfigdir=%{_libdir}/pkgconfig \
  --docdir=%{_pkgdocdir}
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Install additional docs
install -m 644 README.txt \
  doc/api.txt \
  doc/assorted.txt \
  doc/changelog.txt \
  doc/ux-*.txt \
  $RPM_BUILD_ROOT%{_pkgdocdir}

%ldconfig_scriptlets

%files
%license LICENSE.LGPL2 LICENSE.LGPL3 LICENSE.GPL3
%{_libdir}/libHX_rtcheck.so
%{_libdir}/libHX.so.28
%{_libdir}/libHX.so.28.3.0

%files devel
%{_pkgdocdir}

%dir %{_includedir}/libHX
%{_includedir}/libHX.h
%{_includedir}/libHX/ctype_helper.h
%{_includedir}/libHX/defs.h
%{_includedir}/libHX/deque.h
%{_includedir}/libHX/init.h
%{_includedir}/libHX/io.h
%{_includedir}/libHX/libxml_helper.h
%{_includedir}/libHX/list.h
%{_includedir}/libHX/map.h
%{_includedir}/libHX/misc.h
%{_includedir}/libHX/option.h
%{_includedir}/libHX/proc.h
%{_includedir}/libHX/string.h
%{_includedir}/libHX/wx_helper.hpp
%{_libdir}/libHX.so
%{_libdir}/pkgconfig/libHX.pc

%changelog
%autochangelog
