%global source1_hash 339393fc3bd1a8213fb2bb79b28229e00872445f73d9a04eac527ae2e93359d8

%global source0_hash c3c229944d25294102e4e8a5b49fa0c0f481da9d33f8bec3782e8a53afd47493

%global		framework ktexttemplate

%global stable_kf6 stable
%global majmin_ver_kf6 6.30

Name:		kf6-%{framework}
Version:	6.30.0
Release:        1%{?dist}
Summary:	Separates the structure of documents from their data
License:	CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:		https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig


BuildRequires:	cmake
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	gcc-c++
BuildRequires:	kf6-rpm-macros
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Qml)

%description
The goal of KTextTemplate is to make it easier for application developers to
separate the structure of documents from the data they contain, opening the door
for theming and advanced generation of other text such as code.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version}

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%files
%license LICENSES/*.txt
%{_libdir}/libKF6TextTemplate.so.*
%{_kf6_plugindir}/ktexttemplate
%{_kf6_datadir}/qlogging-categories6/ktexttemplate.categories

%files devel
%{_kf6_includedir}/KTextTemplate
%{_libdir}/cmake/KF6TextTemplate
%{_libdir}/libKF6TextTemplate.so


%changelog
%autochangelog
