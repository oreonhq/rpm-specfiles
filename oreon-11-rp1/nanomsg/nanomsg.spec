%global source0_hash fd8f3695484c88f45eac83b7c866e5826e894e102b0d4974be08cb47e18d2ab9
Name:           nanomsg
Version:        1.2.5
Release:        1%{?dist}
Summary:        Socket library that provides several common communication patterns
License:        MIT
URL:            https://nanomsg.org/
Source0:        https://github.com/nanomsg/nanomsg/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  rubygem-asciidoctor
# /oreon:deps
%description
The nanomsg library is a simple high-performance implementation of several
"scalability protocols". These scalability protocols are light-weight messaging
protocols which can be used to solve a number of very common messaging patterns,
such as request/reply, publish/subscribe, surveyor/respondent, and so forth.
These protocols can run over a variety of transports such as TCP, UNIX sockets,
and even WebSocket.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Fix the version number, wrong in version 1.2.5
sed -i 's/1\.2\.1/%{version}/' .version

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n nanomsg-devel -f %{oreon_filedir}/nanomsg-devel.list
%files -n nanomsg-doc -f %{oreon_filedir}/nanomsg-doc.list

%changelog

%autochangelog
