%global source0_hash 39f29a83744b6332948dc5a3cd30eb3e8bd30fd99b5156d7b1949626d939cf69

Name:           gio-qt
Version:        0.0.12
Release:        %autorelease
Summary:        Gio wrapper for Qt applications 
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core) >= 5.6.3
BuildRequires:  glibmm24-devel
BuildRequires:  cmake >= 3.12.4
BuildRequires:  doxygen
BuildRequires:  qt5-doctools 
# for test
BuildRequires:  pkgconfig(Qt5Test)

%description
This package provides a GIO wrapper class for Qt.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?isa}
Requires:       glibmm24-devel%{?isa}

%description devel
Header files and libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# fix doc path
sed -i 's|qt5/doc|doc/qt5|' CMakeLists.txt

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%cmake -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_qt5_docdir}/%{name}.qch

%changelog
%autochangelog
