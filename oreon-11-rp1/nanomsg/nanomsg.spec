%global source0_hash 3ffeafa9335245a23a99827e8d389bfce5100610f44ebbe4bfaf47e8192d5939

Name:           nanomsg
Version:        1.2.2
Release:        2%{?dist}
Summary:        Socket library that provides several common communication patterns

License:        MIT
URL:            https://nanomsg.org/
Source0:        https://github.com/nanomsg/nanomsg/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
# For docs only, can be skipped
BuildRequires:  rubygem-asciidoctor

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
# Fix the version number, wrong in version 1.2.2
sed -i 's/1\.2\.1/%{version}/' .version

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license COPYING
%{_bindir}/nanocat
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/nanocat.1*

%files devel
%doc tests
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}-%{version}/
%{_includedir}/%{name}/
%{_defaultdocdir}/%{name}/
%{_mandir}/man3/nn_*.3*
%{_mandir}/man7/nn_*.7*
%{_mandir}/man7/%{name}.7*

%files doc
%doc AUTHORS doc README.md RELEASING SUPPORT

%changelog
%autochangelog
