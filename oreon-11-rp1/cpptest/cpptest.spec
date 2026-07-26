%global source0_hash 9e4fdf156b709397308536eb6b921e3aea1f463c6613f9a0c1dfec9614386027

Name:           cpptest
Version:        1.1.2
Release:        30%{?dist}
Summary:        A portable and powerful and simple unit testing framework for C++

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://%{name}.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires: make

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

%files
%doc NEWS COPYING AUTHORS ChangeLog
%{_libdir}/*.so.*
%{_datadir}/doc/cpptest

%files devel
%doc doc/html
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
