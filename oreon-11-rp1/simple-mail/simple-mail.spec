%global source0_hash d4a46b5c3f706669ffb3c9e4d2ff5e2bd892eda639f80784d862fa94a2082eb2
%global somajor 0
Name:           simple-mail
Version:        3.1.0
Release:        4%{?dist}
Summary:        SMTP Client Library for Qt
License:        LGPL-2.1-only
URL:            https://github.com/cutelyst/simple-mail
Source0:        https://github.com/cutelyst/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  xz
# /oreon:deps
%description
simple-mail is a small library written for Qt 5 (C++11 version)
that allows application to send complex emails (plain text, html,
attachments, inline files, etc.) using the Simple Mail Transfer
Protocol (SMTP).

%package devel
Summary:        SMTP Client Library for Qt - Development Files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Header and development files for libsimplemail-qt5.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n simple-mail-devel -f %{oreon_filedir}/simple-mail-devel.list

%changelog

%autochangelog
