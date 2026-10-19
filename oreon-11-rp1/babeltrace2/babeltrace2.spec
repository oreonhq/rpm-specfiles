%global source1_hash 8aa272392acd1ba6493ddb7a9a2d51e0c9b5216c66456697dca35574f7c78ef6
%global source0_hash 12833fd234ad679b8bd42b28c07c9141b9f788b3b11ebedec33d2e6c3cb02c9c
Name:           babeltrace2
Version:        2.1.2
Release:        5%{?dist}
Summary:        A trace manipulation toolkit
License:        MIT AND GPL-2.0-only
URL:            https://www.efficios.com/babeltrace
Source0:        https://www.efficios.com/files/babeltrace/babeltrace2-%{version}.tar.bz2
Source1:        https://www.efficios.com/files/babeltrace/babeltrace2-%{version}.tar.bz2.asc
Source2:        gpgkey-7F49314A26E0DE78427680E05F1B2A0789F12B11.gpg
Requires:       libbabeltrace2%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  elfutils-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-g++
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  swig
# /oreon:deps
%description
The Babeltrace 2 project offers a library with a C API, Python 3 bindings, and
a command-line tool which makes it very easy for mere mortals to view,
convert, transform, and analyze traces.

Babeltrace 2 is also the reference parser implementation of the Common Trace
Format (CTF), a very versatile trace format followed by various tracers and
tools such as LTTng and barectf.

%package -n libbabeltrace2
Summary:        A trace manipulation library
%description -n libbabeltrace2
The libbabeltrace2 package contains a library and plugin system to view,
convert, transform, and analyze traces.

%package -n libbabeltrace2-devel
Summary:        Development files for libbabeltrace2
Requires:       libbabeltrace2%{?_isa} = %{version}-%{release} glib2-devel
%description -n libbabeltrace2-devel
The libbabeltrace2-devel package contains the header files and libraries
needed to develop programs that use the libbabeltrace2 trace manipulation
library.

%package -n python3-bt2
Summary:        libbabeltrace2 Python bindings
Requires:       libbabeltrace2%{?_isa} = %{version}-%{release}
%description -n python3-bt2
The python3-bt2 package provides Python 3 bindings for libbabeltrace2.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

autoreconf -vif
export PYTHON=%{__python3}
export PYTHON_CONFIG=%{__python3}-config
%configure --disable-static \
	--enable-python-bindings \
	--enable-python-plugins \
	--enable-debug-info \
	--disable-Werror
make %{?_smp_mflags} V=1
%check

make %{?_smp_mflags} check
%install
make DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete
rm -f %{buildroot}/%{_pkgdocdir}/CONTRIBUTING.adoc
rm -f %{buildroot}/%{_pkgdocdir}/LICENSE
rm -f %{buildroot}/%{_pkgdocdir}/std-ext-lib.md
%ldconfig_scriptlets  -n lib%{name}
%oreon_autofiles libbabeltrace2 usr/*/lib*.so.*
%oreon_autofiles libbabeltrace2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles python3-bt2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libbabeltrace2 -f %{oreon_filedir}/libbabeltrace2.list
%files -n libbabeltrace2-devel -f %{oreon_filedir}/libbabeltrace2-devel.list
%files -n python3-bt2 -f %{oreon_filedir}/python3-bt2.list

%changelog

%autochangelog
