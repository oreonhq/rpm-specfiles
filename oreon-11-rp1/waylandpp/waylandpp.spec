%global source0_hash 49c362fa5db28ab5472968215b88f1fbe3a7b7f57818dde722fd7d38997d940a

Name:           waylandpp
Version:        1.0.1
Release:        3%{?dist}
Summary:        Wayland C++ bindings

# waylandpp includes part of Wayland under MIT, wayland-scanner++ is GPLv3+
# Automatically converted from old format: BSD and MIT and GPLv3+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND GPL-3.0-or-later
URL:            https://github.com/NilsBrause/%{name}/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  mesa-libEGL-devel
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)

%description
Wayland is an object oriented display protocol, which features request and
events. Requests can be seen as method calls on certain objects, whereas events
can be seen as signals of an object. This makes the Wayland protocol a perfect
candidate for a C++ binding.

The goal of this library is to create such a C++ binding for Wayland using the
most modern C++ technology currently available, providing an easy to use C++ API
to Wayland.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
The %{name}-doc package contains development documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake -DCMAKE_INSTALL_DOCDIR=%{_defaultdocdir}/%{name}-doc/
%cmake_build

%install
%cmake_install

# Drop LaTeX documentation (HTML documentation is already built)
rm -r $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-doc/latex/

%check
%ctest

%files
%doc README.md
%license LICENSE
%{_libdir}/*.so.*

%files devel
%doc example/
%{_bindir}/wayland-scanner++
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/%{name}/
%{_mandir}/man3/*.3.*

%files doc
%doc README.md
%license LICENSE
%{_defaultdocdir}/%{name}-doc/*

%changelog
%autochangelog
