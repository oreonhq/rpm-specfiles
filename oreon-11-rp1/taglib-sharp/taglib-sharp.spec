%global source2_hash 0f0e37e29a5919432dff8e03e608cbea9bae3e483259e8f7211d7dfd1e2ddcf6
%global source1_hash ced3c339474f752db4862e30335542057ec73d6717869878a8319e41851a493b
%global source0_hash a2a74092eddec23a47a1cf2e569e52bb784b6ea26fe640f4fac5959acb4da2a8
%global debug_package %{nil}
Name:    taglib-sharp
Version: 2.1.0.0
Release:        1%{?dist}
Summary:        Provides tag reading and writing for Banshee and other Mono apps
License: LicenseRef-Callaway-LGPLv2+
URL:     http://download.banshee-project.org/taglib-sharp/
Source0:        http://download.banshee-project.org/taglib-sharp/%{version}/%{name}-%{version}.tar.bz2
Source1: https://raw.githubusercontent.com/mono/taglib-sharp/master/examples/extractKey.cpp 
Source2: https://raw.githubusercontent.com/mono/taglib-sharp/master/examples/listData.cpp
ExclusiveArch: %{mono_arches}
# oreon:deps
BuildRequires:  exiv2-devel
BuildRequires:  gcc-c++
BuildRequires:  gnome-sharp-devel
BuildRequires:  make
BuildRequires:  mono-devel
BuildRequires:  monodoc-devel
# /oreon:deps
%description
TagLib# is a FREE and Open Source library for the .NET 2.0 and Mono frameworks 
which will let you tag your software with as much or as little detail as you 
like without slowing you down. It supports a large variety of movie and music 
formats which abstract away the work, handling all the different cases, so all 
you have to do is access file.Tag.Title, file.Tag.Lyrics, or my personal 
favorite file.Tag.Pictures. But don't think all this abstraction is gonna keep 
you from tagging's greatest gems. You can still get to a specific tag type's 
features with just a few lines of code. 

%package devel
Summary: Provides tag reading and writing for Banshee and other Mono apps
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
%description devel
Development files for taglib-sharp.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cp %{SOURCE1} %{SOURCE2} examples/
sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.ac

%build

sed -i "s/SUBDIRS = src examples docs/SUBDIRS = src docs/" Makefile.in
%configure --disable-docs
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}%{_datadir}/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n taglib-sharp-devel -f %{oreon_filedir}/taglib-sharp-devel.list

%changelog

%autochangelog
