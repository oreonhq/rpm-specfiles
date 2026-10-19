%global source0_hash 9e40eeb87f014790531ad41326cc271b930a65962e4b15231b301fc59b29fe31
%global somajor 4
%bcond_with tests
Name:           librist
Version:        0.2.20
Release:        1%{?dist}
Summary:        Library for Reliable Internet Stream Transport (RIST) protocol
License:        BSD-2-Clause and ISC
URL:            https://code.videolan.org/rist/librist
Source0:        https://code.videolan.org/rist/librist/-/archive/v0.2.20/librist-v0.2.20.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libcmocka-devel
BuildRequires:  mbedtls-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libcjson)
# /oreon:deps
%description
A library that can be used to speak the RIST protocol (as defined by Video
Services Forum (VSF) Technical Recommendations TR-06-1 and TR-06-2).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Technical documentation for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains technical documentation for
developing applications that use %{name}.

%package -n     rist-tools
Summary:        User tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n rist-tools
This package contains the user tools for the RIST protocol library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
chmod -x %{buildroot}%{_includedir}/%{name}/*.h
chmod -x docs/*
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -av docs/* %{buildroot}%{_docdir}/%{name}
%oreon_autofiles rist-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

%meson_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n librist-devel -f %{oreon_filedir}/librist-devel.list
%files -n librist-doc -f %{oreon_filedir}/librist-doc.list
%files -n rist-tools -f %{oreon_filedir}/rist-tools.list

%changelog

* Mon Apr 20 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.7-11
- Import from Fedora 43 dist-git for Oreon 11 RP1
