%global source0_hash d5b2ac40850ebe3464b499354a213f8944f7cda556f92a00cc3a74e9841bfe52
Name:           cpptest
Version:        2.0.0
Release:        1%{?dist}
Summary:        A portable and powerful and simple unit testing framework for C++
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://%{name}.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
CppTest is a portable and powerful, yet simple, unit testing framework
for handling automated tests in C++. The focus lies on usability and
extendability.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
#%patch0 -p1
%build

export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure --disable-static --enable-doc
make %{?_smp_mflags} V=1
%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles cpptest-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cpptest-devel -f %{oreon_filedir}/cpptest-devel.list

%changelog

%autochangelog
