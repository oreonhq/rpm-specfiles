%global source0_hash 9ce947acbb1984946f9145c976e42e6984f99b98fb414dd7354a290af6d4ff04

Name:           Qt-Advanced-Docking-System
Summary:        Advanced Docking System for Qt
Version:        5.1.1
Release:        1%{?dist}
License:        LGPL-2.1-or-later AND BSL-1.0 AND Apache-2.0
URL:            https://github.com/githubuser0xFFFF/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Quick)

# Required on lower Fedora Versions (41?)
BuildRequires:  qt6-qtbase-private-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DADS_VERSION=%{version}
%cmake_build

%install
%cmake_install
# Already included by rpm
rm -rfv %{buildroot}%{_prefix}/license/ads
rm -rfv %{buildroot}%{_datadir}/ads/license

%files
%license LICENSE gnu-lgpl-v2.1.md
%doc README.md
%{_libdir}/libqtadvanceddocking-qt6.so.%{version}
%{_libdir}/libqtadvanceddocking-qt6.so.5*

%files devel
%{_includedir}/qtadvanceddocking-qt6/
%{_libdir}/cmake/qtadvanceddocking-qt6/
%{_libdir}/libqtadvanceddocking-qt6.so

%changelog
%autochangelog
