%global source0_hash bac3ca7a3f19b67579d7504180ddca788470fb8749889c6bafeea99bdee2da69
Name:           zycore-c
Version:        1.5.2
%global forgeurl https://github.com/zyantific/%{name}
%global commit ba34692d371cde5f45539b5fa26ea11b09721751 
%forgemeta
Release:        1%{?dist}
Summary:        Zyan Core Library for C
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(gtest)
# /oreon:deps
%description
The Zyan Core Library for C is an internal library providing platform
independent types, macros and a fallback for environments without LibC.

%package        devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains the documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

%meson \
    -Ddoc=enabled \
    -Dtests=enabled \
    -Dexamples=enabled \
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n zycore-c-devel -f %{oreon_filedir}/zycore-c-devel.list
%files -n zycore-c-doc -f %{oreon_filedir}/zycore-c-doc.list

%changelog

%autochangelog
