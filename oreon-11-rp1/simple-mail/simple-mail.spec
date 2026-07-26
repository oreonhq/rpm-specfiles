%global source0_hash d4a46b5c3f706669ffb3c9e4d2ff5e2bd892eda639f80784d862fa94a2082eb2

%global somajor 0

Name:           simple-mail
Version:        3.1.0
Release:        4%{?dist}
Summary:        SMTP Client Library for Qt

License:        LGPL-2.1-only
URL:            https://github.com/cutelyst/simple-mail
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.5
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  xz
BuildRequires:  cmake(Qt5Core) >= 5.5.0
BuildRequires:  cmake(Qt5Network) >= 5.5.0
BuildRequires:  cmake(Qt5Widgets) >= 5.5.0

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

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libSimpleMail3Qt5.so.%{somajor}
%{_libdir}/libSimpleMail3Qt5.so.%{version}

%files devel
%{_includedir}/simplemail3-qt5/
%{_libdir}/cmake/SimpleMail3Qt5/
%{_libdir}/libSimpleMail3Qt5.so
%{_libdir}/pkgconfig/SimpleMail3Qt5.pc

%changelog
%autochangelog
