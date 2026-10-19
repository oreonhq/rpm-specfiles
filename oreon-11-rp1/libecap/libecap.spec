%global source0_hash 7c166d997a079110dcc55e9b81eb70b4d73c08b2bcb986fa81bbf78bb62ec8f4
Name:       libecap
Version:    1.0.1
Release:        1%{?dist}
Summary:        Squid interface for embedded adaptation modules
License:    BSD-2-Clause
URL:        http://www.e-cap.org/
Source0:        https://www.e-cap.org/archive/%{name}-%{version}.tar.gz
Source1:    autoconf.h
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
eCAP is a software interface that allows a network application, such as an 
HTTP proxy or an ICAP server, to outsource content analysis and adaptation to 
a loadable module. For each applicable protocol message being processed, an 
eCAP-enabled host application supplies the message details to the adaptation 
module and gets back an adapted message, a "not interested" response, or a 
"block this message now!" instruction. These exchanges often include message 
bodies.

The adaptation module can also exchange meta-information with the host 
application to supply additional details such as configuration options, a 
reason behind the decision to ignore a message, or a detected virus name.

If you are familiar with the ICAP protocol (RFC 3507), then you may think of 
eCAP as an "embedded ICAP", where network interactions with an ICAP server are 
replaced with function calls to an adaptation module.

%package devel
Summary:    Libraries and header files for the libecap library
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the libraries, include files, and other
resources needed for developing libecap applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/libecap.a
rm -f %{buildroot}%{_libdir}/libecap.la
mv %{buildroot}%{_includedir}/%{name}/common/autoconf.h %{buildroot}%{_includedir}/%{name}/common/autoconf-%{_arch}.h
install -pm644 %{SOURCE1} %{buildroot}%{_includedir}/%{name}/common/autoconf.h
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libecap-devel -f %{oreon_filedir}/libecap-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.1-21
- Import
