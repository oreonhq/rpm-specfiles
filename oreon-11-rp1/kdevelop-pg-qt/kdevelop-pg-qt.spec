Name:           kdevelop-pg-qt
Summary:        A parser generator
Version:        2.4.0
Release:        3%{?dist}
License:        LGPL-2.0-only AND GPL-3.0-or-later AND CC0-1.0 AND LGPL-2.0-or-later AND (GPL-2.0-or-later WITH Bison-exception-2.2) AND BSD-3-Clause
URL:            http://techbase.kde.org/Development/KDevelop-PG-Qt_Introduction
Source0:        https://download.kde.org/stable/kdevelop-pg-qt/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)

# For AutoReq cmake-filesystem
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
KDevelop-PG-Qt is a parser generator written in readable source-code and
generating readable source-code. Its syntax was inspired by AntLR. It
implements the visitor-pattern and uses the Qt library. That is why it
is ideal to be used in Qt-/KDE-based applications like KDevelop.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%files 
%doc AUTHORS README
%license LICENSES/*
%{_bindir}/kdev-pg-qt

%files devel
%{_includedir}/KDevelopPGQt/
%{_libdir}/cmake/KDevelop-PG-Qt/
%{_libdir}/cmake/KDevelopPGQt/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.0-3
- Prepare for Oreon 11 (RP1)
