%global source0_hash 179d934676ad3bd172a5a37cf5c6351b8e9d7816feb3029252e79b30a518a3be
Name:           libusb-compat-0.1
Version:        0.1.9
Release:        1%{?dist}
Summary:        Compatibility shim around libusb-1.0 offering the old 0.1 API
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/libusb/libusb-compat-0.1
Source0:        https://github.com/libusb/libusb-compat-0.1/releases/download/v%{version}/libusb-compat-%{version}.tar.bz2
Patch0:         libusb-config-multilib.patch
Provides:       deprecated()
Provides:       libusb = 1:%{version}-%{release}
Obsoletes:      libusb < 1:%{version}-%{release}
Requires:       libusb1%{?_isa}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libusb1-devel
BuildRequires:  make
# /oreon:deps
%description
This package provides a shim / compatibility layer on top of libusb1
offering the old 0.1 API for applications which do not have been ported
to the new 1.0 API yet. Where ever possible applications really should
use and / or be ported to the new 1.0 API instead of relying on this
compatibility library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      libusb-devel < 1:%{version}-%{release}
%description devel
This package contains the header files, libraries and documentation needed to
develop applications that use libusb-0.1. However new applications should use
libusb-1.0 library instead of this one.

%package        tests-examples
Summary:        Tests and examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libusb-tests-examles = 1:%{version}-%{release}
Obsoletes:      libusb-tests-examles < 1:%{version}-%{release}
%description tests-examples
This package contains tests and examples for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n libusb-compat-%{version}
autoreconf -ivf

%build

%configure --disable-static --enable-examples-build
%make_build
%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/libusb.la
for i in lsusb testlibusb; do
    install -m 755 examples/.libs/$i \
        $RPM_BUILD_ROOT%{_bindir}/libusb-compat-0.1-$i
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

LD_LIBRARY_PATH=libusb/.libs ldd -r $RPM_BUILD_ROOT%{_bindir}/libusb-compat-0.1-lsusb
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-compat-0.1-lsusb
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-compat-0.1-testlibusb
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libusb-compat-0.1-devel -f %{oreon_filedir}/libusb-compat-0.1-devel.list
%files -n libusb-compat-0.1-tests-examples -f %{oreon_filedir}/libusb-compat-0.1-tests-examples.list

%changelog

%autochangelog
