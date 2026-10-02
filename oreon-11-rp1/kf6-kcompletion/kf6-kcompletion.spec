%global source1_hash a55e8cf3842560ba5deb3224e7d5a9fcbc437cd0ada92462bfb732cf2b572145

%global source0_hash 96ad9c429ca53b830359c45614ca4c32ed6b759f3023f1b3db1650ba1c19bd58

%global framework kcompletion

%global stable_kf6 stable
%global majmin_ver_kf6 6.30


Name:           kf6-%{framework}
Version:        6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 2 addon with auto completion widgets and classes
# BSD-3-Clause is in the LICENSES folder but goes unused.
License:        CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig


BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6Config) >= %{version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{version}
BuildRequires:  cmake(KF6Codecs) >= %{version}

%description
KCompletion provides widgets with advanced completion support as well as a
lower-level completion class which can be used with your own widgets.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Widgets)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang_kf6 kcompletion6_qt

%files -f kcompletion6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6Completion.so.*
%{_kf6_datadir}/qlogging-categories6/%{framework}.*

%files devel
%{_kf6_includedir}/KCompletion/
%{_kf6_libdir}/libKF6Completion.so
%{_kf6_libdir}/cmake/KF6Completion/
%{_kf6_qtplugindir}/designer/kcompletion6widgets.so


%changelog
%autochangelog
