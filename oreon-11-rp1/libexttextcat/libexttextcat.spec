%global source0_hash 6d77eace20e9ea106c1330e268ede70c9a4a89744ddc25715682754eca3368df

Name: libexttextcat
Version: 3.4.6
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.4.6-1
- Prepare for Oreon 11 (RP1)
