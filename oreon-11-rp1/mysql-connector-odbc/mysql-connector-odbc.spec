%global source0_hash 109f17e4e0320735829b729b64a7e8654071e2f7957745868286ee96de16e054
Name:           mysql-connector-odbc
Version:        9.6.0
Release:        1%{?dist}
Summary:        ODBC driver for MySQL
License:        LicenseRef-Callaway-GPLv2-with-exceptions
URL:            https://dev.mysql.com/downloads/connector/odbc/
Source0:        https://cdn.mysql.com/Downloads/Connector-ODBC/9.6/%{name}-%{version}-src.tar.gz
Patch0:         myodbc-64bit.patch
Patch3:         mysql-connector-odbc-rpath.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libzstd-devel
BuildRequires:  mysql-devel
BuildRequires:  unixODBC-devel
# /oreon:deps
%description
An ODBC (rev 3) driver for MySQL, for use with unixODBC.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-src
%patch -P0 -p1
%patch -P3 -p1

%build

%cmake \
        -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
        -DCMAKE_BUILD_TYPE=RelWithDebinfo \
        -DWITH_UNIXODBC=YES \
        -DRPM_BUILD=YES \
        -DMYSQLCLIENT_STATIC_LINKING=OFF \
        -DDISABLE_GUI=YES \
        -DBUILD_SHARED_LIBS=OFF
cmake -B %_vpath_builddir -LAH -N
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_bindir}/myodbc-installer
find %{buildroot}/usr/ -maxdepth 1 -type f -delete
ln -sf libmyodbc9w.so %{buildroot}%{_libdir}/libmyodbc9.so
mkdir %{buildroot}%{_libdir}/unixODBC
mv %{buildroot}%{_libdir}/libmyodbc*.so %{buildroot}%{_libdir}/unixODBC/
rm -rf %{buildroot}/usr/test
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
