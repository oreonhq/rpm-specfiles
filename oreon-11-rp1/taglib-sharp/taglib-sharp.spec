%global source0_hash a2a74092eddec23a47a1cf2e569e52bb784b6ea26fe640f4fac5959acb4da2a8

%global debug_package %{nil}

Name:    taglib-sharp
Version: 2.1.0.0
Release: 28%{?dist}
Summary: Provides tag reading and writing for Banshee and other Mono apps

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     http://download.banshee-project.org/taglib-sharp/
Source0: http://download.banshee-project.org/taglib-sharp/%{version}/%{name}-%{version}.tar.bz2
# These files are missing from the 2.1.0.0 tarball for some reason.
# Downloaded into Fedora packages git on 2016-01-19
Source1: https://raw.githubusercontent.com/mono/taglib-sharp/master/examples/extractKey.cpp 
Source2: https://raw.githubusercontent.com/mono/taglib-sharp/master/examples/listData.cpp

# Mono only available on these:
ExclusiveArch: %{mono_arches}

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires: mono-devel, monodoc-devel, gnome-sharp-devel, exiv2-devel

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
# building examples is broken
sed -i "s/SUBDIRS = src examples docs/SUBDIRS = src docs/" Makefile.in
# Docs are broken.
%configure --disable-docs
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}%{_datadir}/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/

%files
%doc COPYING
%{_prefix}/lib/mono/gac/*/
%{_prefix}/lib/mono/taglib-sharp/

%files devel
# %%doc %%{_libdir}/monodoc/sources/taglib-sharp-docs*
%{_libdir}/pkgconfig/taglib-sharp.pc

%changelog
%autochangelog
