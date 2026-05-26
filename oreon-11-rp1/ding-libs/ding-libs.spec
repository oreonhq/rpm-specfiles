# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 5df2f202f892b4c1a6caf87f0056398a8288b281da9d7e65cd7637978ec20ef3
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name: ding-libs
Version: 0.7.0
Release: 62%{?dist}
Summary: "Ding is not GLib" assorted utility libraries
License: LGPL-3.0-or-later
URL: https://github.com/SSSD/ding-libs/
Source0:        https://github.com/SSSD/ding-libs//releases/download/0.7.0/ding-libs-0.7.0.tar.gz

# If a new upstream release changes some, but not all of these
# version numbers, remember to keep the Release tag in order to
# allow clean upgrades!
%global dhash_version 0.5.0
%global ini_config_version 2.0.0

### Patches ###

### Dependencies ###
# ding-libs is a meta-package that will pull in all of its own
# sub-packages
Obsoletes: libpath_utils <= 0.2.1
Obsoletes: libcollection <= 0.7.0
Obsoletes: libbasicobjects <= 0.1.1
Obsoletes: libref_array <= 0.1.5
Requires: libdhash = %{dhash_version}-%{release}
Requires: libini_config = %{ini_config_version}-%{release}

### Build Dependencies ###

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext-devel
BuildRequires: gcc
BuildRequires: git
BuildRequires: libtool
BuildRequires: m4
BuildRequires: doxygen
BuildRequires: pkgconfig
BuildRequires: check-devel
BuildRequires: make

%description
A meta-package that pulls in libdhash and libini_config.

%package devel
Summary: Development packages for ding-libs
License: LGPL-3.0-or-later

# ding-libs is a meta-package that will pull in all of its own
# sub-packages
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

%files -n libdhash
%doc COPYING COPYING.LESSER
%{_libdir}/libdhash.so.1
%{_libdir}/libdhash.so.1.1.0

%files -n libdhash-devel
%{_includedir}/dhash.h
%{_libdir}/libdhash.so
%{_libdir}/pkgconfig/dhash.pc
%doc dhash/README.dhash
%doc dhash/examples/*.c


##############################################################################
# ini_config
##############################################################################

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

%files -n libini_config
%doc COPYING
%doc COPYING.LESSER
%{_libdir}/libini_config.so.8
%{_libdir}/libini_config.so.8.0.0

%files -n libini_config-devel
%{_includedir}/ini_configobj.h
%{_includedir}/ini_configmod.h
%{_includedir}/ref_array.h
%{_libdir}/libini_config.so
%{_libdir}/pkgconfig/ini_config.pc
%doc ini/doc/html/
%doc refarray/README.ref_array


##############################################################################
# Build steps
##############################################################################

%prep
%oreon_verify_sources
%autosetup -S git

%build
autoreconf -ivf
%configure \
    --disable-static

make %{?_smp_mflags} all docs

%check
make %{?_smp_mflags} check

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Remove .la files created by libtool
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

# Remove the example files from the output directory
# We will copy them directly from the source directory
# for packaging
rm -f \
    $RPM_BUILD_ROOT%{_datadir}/doc/ding-libs/README.* \
    $RPM_BUILD_ROOT%{_datadir}/doc/ding-libs/examples/dhash_example.c \
    $RPM_BUILD_ROOT%{_datadir}/doc/ding-libs/examples/dhash_test.c

# Remove document install script. RPM is handling this
rm -f */doc/html/installdox

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.0-62
- Prepare for Oreon 11 (RP1)
