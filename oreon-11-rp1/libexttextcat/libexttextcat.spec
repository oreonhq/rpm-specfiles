%global source0_hash 93eb89fd4fc8f565806354e100e778b3ac9a24e5fc04c24e6a83fb1e9b6c9d59

Name: libexttextcat
Version: 3.4.8
Release: %autorelease
Summary: Text categorization library

License: BSD-3-Clause
URL: https://wiki.documentfoundation.org/Libexttextcat
Source:        http://dev-www.libreoffice.org/src/libexttextcat/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: make

%description
%{name} is an N-Gram-Based Text Categorization library primarily
intended for language guessing.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Tool for creating custom document fingerprints
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
The %{name}-tools package contains the createfp program that allows
you to easily create your own document fingerprints.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%configure --disable-silent-rules --disable-static --disable-werror
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la

%check
make check

%ldconfig_scriptlets

%files
%doc ChangeLog README*
%license LICENSE
%{_libdir}/%{name}*.so.*
%{_datadir}/%{name}

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/vala/vapi/libexttextcat.vapi

%files tools
%{_bindir}/createfp

%changelog
%autochangelog
