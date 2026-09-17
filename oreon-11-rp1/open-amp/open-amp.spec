%global source0_hash 0ff5e3d716b2d55be95539d756f721865b274f59509aeedf0d6a49086b1064e3

Name:		open-amp
Version:	2025.10.0
Release:	%autorelease
Summary:	Open Asymmetric Multi Processing (OpenAMP) framework project
License:	BSD-3-Clause OR BSD-2-Clause
URL:		https://github.com/OpenAMP/open-amp/
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	libmetal-devel
BuildRequires:	libsysfs-devel

%description
The OpenAMP framework provides software components that enable development of
software applications for Asymmetric Multiprocessing (AMP) systems.

%package libs
Summary:	Libaries for OpenAMP
Obsoletes:	open-amp <= 2025.04.0
Provides:	open-amp
%description libs
Libaries for OpenAMP baremetal, and RTOS environments.

%package devel
Summary:	Development files for OpenAMP
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development file for OpenAMP
baremetal, and RTOS environments.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
	-DCMAKE_INCLUDE_PATH=%{_includedir}/libmetal/ \
	-DCMAKE_LIBRARY_PATH=%{_libdir} \
	-DWITH_STATIC_LIB=OFF

%cmake_build

%install
%cmake_install

%files libs
%license LICENSE.md
%doc README.md
%{_libdir}/libopen_amp.so.1
%{_libdir}/libopen_amp.so.1.*

%files devel
%{_includedir}/openamp/
%{_libdir}/libopen_amp.so

%changelog
%autochangelog
