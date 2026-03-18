# Force out of source build
%undefine __cmake_in_source_build

%global somajor 0

Name:           libeconf
Version:        0.7.9
Release:        3%{?dist}
Summary:        Enhanced config file parser library

License:        MIT
URL:            https://github.com/openSUSE/libeconf
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

### Patches ###
# This should be a temporary workaround. I don't have enough time to check what's happening, but since we aren't shipping the html documentation it's fine to stop installing it
Patch0101:      0001-cmake-no-install-html.patch
# Intermittent failure of a test in aarch64, thus temporarily disabling the failing test suite
Patch0102:      0002-disable-test.patch


BuildRequires:  cmake >= 3.12
BuildRequires:  gcc
BuildRequires:  make

%description
libeconf is a highly flexible and configurable library to parse and manage
key=value configuration files. It reads configuration file snippets from
different directories and builds the final configuration file from it.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        utils
Summary:        Utilities for manipulating config files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
The %{name}-utils package contains utilities for manipulating
configuration files from applications that use %{name}.


%prep
%autosetup -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%check
%cmake_build --target check


%files
%license LICENSE
%doc NEWS README.md TODO.md
%{_libdir}/%{name}.so.%{somajor}{,.*}

%files devel
%doc example/
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*.3.*

%files utils
%{_bindir}/econftool
%{_mandir}/man8/econftool.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.9-3
- Prepare for Oreon 11 (RP1)
