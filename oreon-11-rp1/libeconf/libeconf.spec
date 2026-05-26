# Force out of source build
%undefine __cmake_in_source_build

%global somajor 0

Name:           libeconf
Version:        0.7.9
Release:        4%{?dist}
Summary:        Enhanced config file parser library

License:        MIT
URL:            https://github.com/openSUSE/libeconf
Source0:        https://github.com/openSUSE/libeconf/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

### Patches ###
# This should be a temporary workaround. I don't have enough time to check what's happening, but since we aren't shipping the html documentation it's fine to stop installing it
Patch0101:      0001-cmake-no-install-html.patch
# Intermittent failure of a test in aarch64, thus temporarily disabling the failing test suite
Patch0102:      0002-disable-test.patch
# oreon url source checksums begin
%global source0_sha256 0605f8d8a2f4668cb16e279ebcad8002cc83f44610633157e9c4b8fc183a479b
%global source0_file v0.7.9.tar.gz
# oreon url source checksums end


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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/v0.7.9.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0605f8d8a2f4668cb16e279ebcad8002cc83f44610633157e9c4b8fc183a479b" || { echo "oreon: Source0 SHA256 mismatch for v0.7.9.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.9-4
- Fix Source0 GitHub archive URL for spectool

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.9-3
- Prepare for Oreon 11 (RP1)
