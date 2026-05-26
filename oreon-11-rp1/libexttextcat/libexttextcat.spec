Name: libexttextcat
Version: 3.4.6
Release: %autorelease
Summary: Text categorization library

License: BSD-3-Clause
URL: https://wiki.documentfoundation.org/Libexttextcat
Source: http://dev-www.libreoffice.org/src/libexttextcat/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 6d77eace20e9ea106c1330e268ede70c9a4a89744ddc25715682754eca3368df
%global source0_file libexttextcat-3.4.6.tar.xz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libexttextcat-3.4.6.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6d77eace20e9ea106c1330e268ede70c9a4a89744ddc25715682754eca3368df" || { echo "oreon: Source0 SHA256 mismatch for libexttextcat-3.4.6.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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
