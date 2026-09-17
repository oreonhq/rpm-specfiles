%global source0_hash dc45d12e85deee67c2da103188a05b0e59e8d55ff9e6f48c6b7d988f39ee1b53

Name:           docparser
Version:        1.0.25
Release:        %autorelease
Summary:        A document parser library ported from document2html

License:        LGPL-3.0-or-later AND CC-BY-4.0 AND CC0-1.0 AND MIT
URL:            https://github.com/linuxdeepin/docparser
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(tinyxml2)
BuildRequires:  pkgconfig(libmagic)
# test dependencies
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Dtk6Core)

%description
This file content analysis library is provided for the full-text search function
of document management.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
sed -i 's|Debug|RelWithDebInfo|' CMakeLists.txt

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_bindir}/{docparser_test,docparser_autotest}

%check
%{_vpath_builddir}/tests/docparser_autotest

%files
%license LICENSES/*
%doc README.md
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
