%global source0_hash 21ebba447cf1cf6f1adac6a97d0389a2c44d6fda52fc29cbfa50392d1f11c026
Name: ding-libs
Version: 0.7.0
Release:        1%{?dist}
Summary:        "Ding is not GLib" assorted utility libraries
License: LGPL-3.0-or-later
URL: https://github.com/SSSD/ding-libs/
Source0:        https://codeload.github.com/SSSD/ding-libs/tar.gz/%{version}#/ding-libs-%{version}.tar.gz
%global dhash_version 0.5.0
%global ini_config_version 2.0.0
Obsoletes: libpath_utils <= 0.2.1
Obsoletes: libcollection <= 0.7.0
Obsoletes: libbasicobjects <= 0.1.1
Obsoletes: libref_array <= 0.1.5
Requires: libdhash = %{dhash_version}-%{release}
Requires: libini_config = %{ini_config_version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
A meta-package that pulls in libdhash and libini_config.

%package devel
Summary: Development packages for ding-libs
License: LGPL-3.0-or-later
Obsoletes: libpath_utils-devel <= 0.2.1
Obsoletes: libcollection-devel <= 0.7.0
Obsoletes: libbasicobjects-devel <= 0.1.1
Obsoletes: libref_array-devel <= 0.1.5
Requires: libdhash-devel = %{dhash_version}-%{release}
Requires: libini_config-devel = %{ini_config_version}-%{release}
%description devel
A meta-package that pulls in development libraries for
libdhash and libini_config.

##############################################################################
# dhash
##############################################################################

%package -n libdhash
Summary: Dynamic hash table
License: LGPL-3.0-or-later
Version: %{dhash_version}
%description -n libdhash
A hash table which will dynamically resize to achieve optimal storage & access
time properties

%package -n libdhash-devel
Summary: Development files for libdhash
Requires: libdhash = %{dhash_version}-%{release}
License: LGPL-3.0-or-later
Version: %{dhash_version}
%description -n libdhash-devel
A hash table which will dynamically resize to achieve optimal storage & access
time properties

%ldconfig_scriptlets -n libdhash

%package -n libini_config
Summary: INI file parser for C
License: LGPL-3.0-or-later
Obsoletes: libpath_utils <= 0.2.1
Obsoletes: libcollection <= 0.7.0
Obsoletes: libbasicobjects <= 0.1.1
Obsoletes: libref_array <= 0.1.5
Version: %{ini_config_version}
%description -n libini_config
Library to process config files in INI format

%package -n libini_config-devel
Summary: Development files for libini_config
License: LGPL-3.0-or-later
Obsoletes: libpath_utils-devel <= 0.2.1
Obsoletes: libcollection-devel <= 0.7.0
Obsoletes: libbasicobjects-devel <= 0.1.1
Obsoletes: libref_array-devel <= 0.1.5
Requires: libini_config = %{ini_config_version}-%{release}
Version: %{ini_config_version}
%description -n libini_config-devel
Library to process config files in INI format

%ldconfig_scriptlets -n libini_config

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -ivf
%configure \
    --disable-static
make %{?_smp_mflags} all docs
%check

make %{?_smp_mflags} check
%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f \
    $RPM_BUILD_ROOT%{_datadir}/doc/ding-libs/README.* \
    $RPM_BUILD_ROOT%{_datadir}/doc/ding-libs/examples/dhash_example.c \
    $RPM_BUILD_ROOT%{_datadir}/doc/ding-libs/examples/dhash_test.c
rm -f */doc/html/installdox
%oreon_autofiles libdhash usr/*/lib*.so.*
%oreon_autofiles libdhash-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libini_config usr/*/lib*.so.*
%oreon_autofiles libini_config-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ding-libs-devel -f %{oreon_filedir}/ding-libs-devel.list
%files -n libdhash -f %{oreon_filedir}/libdhash.list
%files -n libdhash-devel -f %{oreon_filedir}/libdhash-devel.list
%files -n libini_config -f %{oreon_filedir}/libini_config.list
%files -n libini_config-devel -f %{oreon_filedir}/libini_config-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.0-62
- Prepare for Oreon 11 (RP1)
