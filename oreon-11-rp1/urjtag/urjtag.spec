%global source0_hash b0a2eaa245513af096dc4d770109832335c694c6c12aa5e92fefae8685416f1c
%global without_python3 1
Name:           urjtag
Version:        2021.03
Release:        1%{?dist}
Summary:        A tool for communicating over JTAG with flash chips and CPUs
License:        GPL-2.0-or-later
URL:            http://urjtag.org
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Patch0:         %{name}-fixarm.patch
%global py3_prefix python3
# oreon:deps
BuildRequires:  (python3-setuptools if python3-devel >= 3.12)
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libftdi-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  swig
# /oreon:deps
%description
UrJTAG aims to create an enhanced, modern tool for communicating
over JTAG with flash chips, CPUs, and many more.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        -n %{py3_prefix}-%{name}
%{?python_provide:%python_provide %{py3_prefix}-%{name}}
Summary:        Python bindings for %{name}
Requires:       %{name} = %{version}-%{release}
%description    -n %{py3_prefix}-%{name}
Python bindings and examples for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p2 -b .armfix

%build

%configure --enable-jedec-exp --enable-stapl --enable-bsdl --enable-svf --disable-static --enable-shared
%{__make} %{?_smp_mflags} V=1
pushd bindings/python/
%py3_build
%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a
%find_lang %{name}
pushd bindings/python/
%py3_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n urjtag-devel -f %{oreon_filedir}/urjtag-devel.list
%files -n python3-urjtag -f %{oreon_filedir}/python3-urjtag.list

%changelog

%autochangelog
