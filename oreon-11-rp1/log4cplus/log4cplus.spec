%global source0_hash 6fc6b1b392921b048dcb0a71b5a1b46e9956bff710d288bdc9c4fc689f1a5f0b
%global source1_hash dc85f6425858b856e8435caad51c28ba3dc7d7d202a3436865218d8ac7a01586
%global source2_hash 1f176e33776225088cdb6a3e3d3fb3869a0c5624b001340382c0cc500dd70a6a

#%%global prever rc3

Name: log4cplus
Version: 2.2.0.1
Release: %autorelease
Summary: Logging Framework for C++

%define VER %(echo %{version} | tr . _)

# Threadpool is Zlib
# catch/* is BSL-1.0
License: (BSD-2-Clause OR Apache-2.0) AND Zlib AND BSL-1.0
URL: https://github.com/log4cplus/log4cplus
Source0: https://github.com/log4cplus/log4cplus/releases/download/REL_%{VER}/%{name}-%{version}%{?prever:-%{prever}}.tar.xz
Source1: https://github.com/log4cplus/log4cplus/releases/download/REL_%{VER}/%{name}-%{version}%{?prever:-%{prever}}.tar.xz.sig
Source2: https://github.com/wilx.gpg

%description
log4cplus is a simple to use C++ logging API providing thread-safe, flexible,
and arbitrarily granular control over log management and configuration. It is
modeled after the Java log4j API.

%package devel
Summary: Development files for log4cplus C++ logging framework
Requires: %{name} = %{version}-%{release}
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: gnupg2

%description devel
This package contains headers and libraries needed to develop applications
using log4cplus logging framework.

%package static
Summary: Static development files for log4cplus C++ logging framework
Requires: %{name}-devel = %{version}-%{release}

%description static
This package contains static libraries needed to develop applications
using log4cplus logging framework.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
%if 0%{?fedora}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%setup -q %{?prever:-n %{name}-%{version}-%{prever}}

%build
%configure --enable-static
make %{?_smp_mflags}


%install
%make_install

rm -f $RPM_BUILD_ROOT/%{_libdir}/liblog4cplus*.la

%ldconfig_scriptlets

%files
%doc LICENSE README.md ChangeLog
%{_libdir}/liblog4cplus*-2.2.so.11*

%files devel
%dir %{_includedir}/log4cplus
%dir %{_includedir}/log4cplus/boost
%dir %{_includedir}/log4cplus/config
%dir %{_includedir}/log4cplus/helpers
%dir %{_includedir}/log4cplus/internal
%dir %{_includedir}/log4cplus/spi
%dir %{_includedir}/log4cplus/thread
%dir %{_includedir}/log4cplus/thread/impl
%{_libdir}/lib*.so
%{_includedir}/log4cplus/*.h*
%{_includedir}/log4cplus/boost/*.h*
%{_includedir}/log4cplus/config/*.h*
%{_includedir}/log4cplus/helpers/*.h*
%{_includedir}/log4cplus/internal/*.h*
%{_includedir}/log4cplus/spi/*.h*
%{_includedir}/log4cplus/thread/*.h*
%{_includedir}/log4cplus/thread/impl/*.h*
%{_libdir}/pkgconfig/log4cplus.pc

%files static
%{_libdir}/lib*.a


%changelog
%autochangelog
