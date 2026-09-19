%global source0_hash 37ce98b20f542e74f43ccac55ba98f3566f3095ca05c5bbc182b2112b0b7f892

%global forgeurl https://github.com/PixlOne/ipcgull
%global proj_epoc 0

Name:    ipcgull
Version: 0.1
Release: 8%{?dist}
Summary: A GDBus-based IPC library for modern C++
%forgemeta

License: GPL-3.0-or-later
URL:     %{forgeurl}

Source0: %{forgesource}

# Change from static to dynamic lib
Patch0:         ipcgull-shared-lib.patch
Patch1:         ipcgull-include-stdexcept.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libstdc++-devel

%description
Ipcgull is a C++ IPC library that takes advantage of modern C++17 
features to provide a simple interface for developers to handle IPC.

Currently, Ipcgull only supports a D-Bus backend (via GDBus), but this 
is abstracted by the library and can theoretically be replaced. 
However, that is out of scope for this project.

%package devel
Summary: A GDBus-based IPC library for modern C++
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains header files and other files needed to develop
with ipcgull.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
%cmake -DPROJECT_EPOCH=%{proj_epoc}

%build
%{cmake_build}

%install
%{cmake_install}
install -D -pm 755 redhat-linux-build/libipcgull_shared.so.%{version} %{buildroot}%{_libdir}/libipcgull_shared.so.%{version}
install -D -pm 755 redhat-linux-build/libipcgull_shared.so.%{proj_epoc} %{buildroot}%{_libdir}/libipcgull_shared.so.%{proj_epoc}

%files
%{_libdir}/*.so.*

%license LICENSE
%doc README.md

%files devel
%{_libdir}/*.so
%{_includedir}/ipcgull/

%changelog
%autochangelog
