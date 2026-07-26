%global source0_hash 07b18037fb0983f6292f5c8d53e2369e9e7a9711df2c9ad50838aacbc8c62f7c

Name:           cxxtools
Version:        3.0
Release:        19%{?dist}
Summary:        A collection of general-purpose C++ classes
Epoch:          1

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ 
URL:            http://www.tntnet.org/cxxtools.html
Source0:        https://github.com/maekitalo/cxxtools/archive/refs/tags/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}-arm.patch
Patch1:         %{name}-%{version}-gcc11.patch
Patch2:         %{name}-%{version}-i686.patch
Patch3:         %{name}-%{version}-ppc64le.patch
# fix error: aggregate 'tm tim' has incomplete type and cannot be defined
Patch4:         %{name}-%{version}-timer.patch
# fix assertion with GLIBCXX_ASSERTIONS (upstream patch)
Patch5:         0001-fix-for-possible-crash-in-cxxtools-Connectable.patch
Patch6:         cxxtools-cxx20.patch

BuildRequires:  make
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
# test requirement:
BuildRequires:  tzdata
Provides:       bundled(md5-polstra)

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
Development files for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{name}-%{version}

# fix spurious executable perm
find -name "*.cpp" -exec chmod -x {} \;
find -name "*.h" -exec chmod -x {} \;

%build
# configure tests try to compile code containing ASMs to a .o file
# In an LTO world, that always works as compilation does not happen until
# link time.  As a result we get the wrong results from configure.
# This can be fixed by using -ffat-lto-objects
# -ffat-lto-objects forces compilation even with LTO.  It is the default
# for F33, but not expected to be enabled by default for F34
%define _lto_cflags -flto=auto -ffat-lto-objects

#aclocal && automake
%configure --disable-static \
%ifarch s390 s390x aarch64
    --with-atomictype=pthread \
%endif
    %{nil}
%make_build

%install
%make_install

# Find and remove all la files
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%%check
    test/alltests

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libcxxtools*.so.*

%files devel
%{_bindir}/cxxtools-config
%{_bindir}/cxxtz
%{_bindir}/siconvert
%{_libdir}/libcxxtools*.so
%{_libdir}/pkgconfig/%{name}-*.pc
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/cxxtools/

%changelog
%autochangelog
