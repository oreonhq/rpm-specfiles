%global source0_hash 1dc35dd997e1938a97489fa1f349ee16889f9de8901a2c7af46184468dc90598
Name:		libad9361-iio
URL:		https://github.com/analogdevicesinc/libad9361-iio
Version:	0.3
Release:        1%{?dist}
License:	LGPL-2.1-or-later
Summary:        IIO AD9361 library for filter design and handling, multi-chip sync and more
Source0:        https://github.com/analogdevicesinc/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libiio-devel
# /oreon:deps
%description
IIO AD9361 library which manages multi-chip sync (on platforms (FMCOMMS5)
where multiple AD9361 devices are used) and can create AD9361 specific FIR
filters on the fly.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
%description devel
Development files for %{name}.

%package doc
Summary:	Documentation files for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DINSTALL_LIB_DIR=%{_libdir}
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_docdir}/ad93610-doc __docs
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

cd %{_vpath_builddir}
%make_build test
%files -f %{oreon_filedir}/main.list
%files -n libad9361-iio-devel -f %{oreon_filedir}/libad9361-iio-devel.list
%files -n libad9361-iio-doc -f %{oreon_filedir}/libad9361-iio-doc.list

%changelog

%autochangelog
