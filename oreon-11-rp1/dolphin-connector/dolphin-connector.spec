%global source0_hash 6bd0c5de22cdb77b941da3019adbb8c22e68e7fd37e81fa738412a7b54de34f0

Name:           dolphin-connector
Version:        1.2
Release:        44%{?dist}
Summary:        Simple MySQL C API wrapper for C++

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/poetinha/dolphin-connector
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  git clone https://github.com/poetinha/dolphin-connector.git
#  cd dolphin-connector
#  git archive --format=tar --prefix=dolphin-connector-1.2/ v1.2 | gzip >dolphin-connector-1.2.tar.gz
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libtool mariadb-connector-c-devel boost-devel
BuildRequires: make

%description
Dolphin Connector is a simple MySQL C API wrapper for C++.

It is originally designed to be as efficient as is possible,
and makes no use of exceptions.

%package devel
Summary: Development files for Dolphin Connector
Requires: %{name} = %{version}-%{release}
Requires: mariadb-connector-c-devel
Requires: boost-devel

%description devel
Dolphin Connector development package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
./autogen.sh

%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# cleanup
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

rm -f sample/Makefile*

%ldconfig_scriptlets

%files
%doc ChangeLog LICENSE README TODO
%{_libdir}/libdolphinconn.so.*

%files devel
%doc sample
%{_includedir}/dolphinconn
%{_libdir}/libdolphinconn.so

%changelog
%autochangelog
