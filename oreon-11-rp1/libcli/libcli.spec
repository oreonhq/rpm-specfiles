%global source0_hash 179f78592f73492c22cc1b544b6f8cb0f6630a2f670430c118b8e084e6562e74

Name: libcli
Version: 1.10.7
Release: 13%{?dist}
Summary: A shared library for a Cisco-like cli
License: LGPL-2.1-or-later
URL: http://sites.dparrish.com/libcli
Source0: https://github.com/dparrish/libcli/archive/V%{version}/%{name}-%{version}.tar.gz

# https://github.com/dparrish/libcli/pull/93
Patch0: calloc.patch

%package devel
Summary: Development files for libcli
Requires: %{name}%{?_isa} = %{version}-%{release}

BuildRequires:  gcc
BuildRequires: make
BuildRequires: libxcrypt-devel
%description
Libcli provides a shared library for including a Cisco-like command-line 
interface into other software. It's a telnet interface which supports 
command-line editing, history, authentication and callbacks for a 
user-definable function tree. 

%description devel
Libcli provides a shared library for including a Cisco-like command-line 
interface into other software. It's a telnet interface which supports 
command-line editing, history, authentication and callbacks for a 
user-definable function tree. 

These are the development files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P 0 -p0

%build

make %{?_smp_mflags}

%install
install -d -p %{buildroot}%{_includedir}
install -p -m 644 libcli*.h %{buildroot}%{_includedir}/
install -d -p %{buildroot}%{_libdir}
install -p -m 755 libcli.so.%{version} %{buildroot}%{_libdir}/
ln -s %{_libdir}/libcli.so.%{version} %{buildroot}%{_libdir}/libcli.so.1.10
ln -s %{_libdir}/libcli.so.1.10 %{buildroot}%{_libdir}/libcli.so

%ldconfig_scriptlets

%files
%doc COPYING
%{_libdir}/*.so.1.10*

%files devel
%doc README.md
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
%autochangelog
