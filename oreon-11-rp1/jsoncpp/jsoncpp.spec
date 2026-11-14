# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f93b6dd7ce796b13d02c108bc9f79812245a82e577581c4c9aabe57075c90ea2

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global jsondir json
%global sover 26

Name:           jsoncpp
Version:        1.9.6
Release:        1%{?dist}
Summary:        JSON library implemented in C++
License:        MIT OR LicenseRef-Public-Domain
URL:            https://github.com/open-source-parsers/jsoncpp
Source0:        https://github.com/open-source-parsers/jsoncpp/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  cmake >= 3.1
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3-devel

%description
%{name} is an implementation of a JSON (http://json.org) reader and writer in
C++. JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It is easy for humans to read and write. It is easy for machines to parse and
generate.

%package        devel
Summary:        Development headers and library for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       pkgconfig(jsoncpp) = %{version}

%description    devel
This package contains the development headers and library for %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  hardlink

%description    doc
This package contains the documentation for %{name}.

%prep
%oreon_sha256
%autosetup -p1
doxygen -s -u doc/doxyfile.in
sed -i -e 's!^DOT_FONTNAME.*=.*!DOT_FONTNAME =!g' doc/doxyfile.in

%build
%cmake \
  -DBUILD_STATIC_LIBS:BOOL=OFF \
  -DBUILD_OBJECT_LIBS:BOOL=OFF \
  -DJSONCPP_WITH_CMAKE_PACKAGE:BOOL=ON \
  -DJSONCPP_WITH_EXAMPLE:BOOL=OFF \
  -DJSONCPP_WITH_PKGCONFIG_SUPPORT:BOOL=ON \
  -DJSONCPP_WITH_POST_BUILD_UNITTEST:BOOL=OFF \
  -DJSONCPP_WITH_STRICT_ISO:BOOL=ON \
  -DJSONCPP_WITH_TESTS:BOOL=ON \
  -DPYTHON_EXECUTABLE:STRING="%{__python3}"
%cmake_build

cp -p %{__cmake_builddir}/version .
%{__python3} doxybuild.py --with-dot --doxygen /usr/bin/doxygen
rm -f version

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}
install -pm 0644 README.md %{buildroot}%{_docdir}/%{name}

mkdir -p %{buildroot}%{_docdir}/%{name}/html
cp -a dist/doxygen/jsoncpp-api-html-/* %{buildroot}%{_docdir}/%{name}/html
find %{buildroot}%{_docdir} -type d -print0 | xargs -0 chmod -c 0755
find %{buildroot}%{_docdir} -type f -print0 | xargs -0 chmod -c 0644
hardlink -cfv %{buildroot}%{_docdir}/%{name}

%check
%global _smp_mflags -j1
%ctest

%ldconfig_scriptlets

%files
%license AUTHORS LICENSE
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README.md
%exclude %{_docdir}/%{name}/html
%{_libdir}/lib%{name}.so.%{sover}*
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{jsondir}
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%license %{_datadir}/licenses/%{name}
%doc %{_docdir}/%{name}

%changelog
%autochangelog
