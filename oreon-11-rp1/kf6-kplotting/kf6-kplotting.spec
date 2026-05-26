%undefine __cmake_in_source_build

%global framework kplotting

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:           kf6-%{framework}
Version:        6.24.0
Release:	6%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon for plotting
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
# oreon url source checksums begin
%global source0_sha256 398cea5da5fb5b505eb34582ec5c318abec75b8c40af98b50f7cf9b6d8a0fecf
%global source0_file kplotting-6.24.0.tar.xz
# oreon url source checksums end

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# Fedora
BuildRequires:  kf6-rpm-macros
Requires:       kf6-filesystem

# KDE Frameworks
BuildRequires:  extra-cmake-modules >= %{version}

# Other
BuildRequires:  pcre2-devel
BuildRequires:  perl-interpreter

# Qt
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6UiPlugin)

%description
KPlotting provides classes to do plotting.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/kplotting-6.24.0.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "398cea5da5fb5b505eb34582ec5c318abec75b8c40af98b50f7cf9b6d8a0fecf" || { echo "oreon: Source0 SHA256 mismatch for kplotting-6.24.0.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6Plotting.so.*

%files devel
%{_kf6_includedir}/KPlotting/
%{_kf6_libdir}/libKF6Plotting.so
%{_kf6_libdir}/cmake/KF6Plotting/
%{_kf6_qtplugindir}/designer/kplotting6widgets.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- inline cmake --build (no qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

