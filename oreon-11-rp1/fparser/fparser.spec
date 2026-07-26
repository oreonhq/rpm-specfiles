%global source0_hash 57ef7f03ea49e3f278a715c094933a0f3da4af9118a5f18de809062292be9833

%global majorversion 4
%global minorversion 5
%global patchversion 2
Name:           fparser
Version:        %{majorversion}.%{minorversion}.%{patchversion}
Release:        %autorelease
Summary:        Function parser library for C++

License:        LGPL-3.0-only
URL:            http://warp.povusers.org/FunctionParser/
Source0:        http://warp.povusers.org/FunctionParser/fparser%{version}.zip
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires: make

# upstream doesn't provide a build system and won't include this patch
Patch0:         fparser.autotools.patch
Patch1:         fparser.includes.patch
Patch2:         fparser.config.patch

%description
This C++ library offers a class which can be used to parse and evaluate a
mathematical function from a string (which might be for example requested
from the user). The syntax of the function string is similar to
mathematical expressions written in C/C++.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1 -n %{name}-%{version}
mkdir m4
autoreconf -f -i

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT/%{_libdir}/*.la

%files
%doc docs/gpl.txt docs/lgpl.txt
%{_libdir}/libfparser-%{majorversion}.%{minorversion}.so

%files devel
%doc docs/fparser.html docs/style.css
%{_includedir}/*
%{_libdir}/libfparser.so
%{_libdir}/pkgconfig/fparser.pc

%changelog
%autochangelog
