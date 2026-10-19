%global source0_hash 2cbcebb0f22e48fdc9e9fac6215eaf70344b3a07a7f9b8dfbf657ede1f26b38d
%define python_binding 0
%define ruby_binding 0
Name:           tomoe
Version:        0.6.0
Release:        59%{?dist}
Summary:        Handwritten input system for Japanese and Chinese
License:        LGPL-2.1-or-later
URL:            http://tomoe.sourceforge.jp/
Source0:        %{name}-stripped-%{version}.tar.gz
Source1:        strip.sh
Patch0:         tomoe-0.6.0-multiarch-conflict.patch
Patch1:         tomoe-0.6.0-bz502662.patch
Patch2:         tomoe-0.6.0-fixes-glib-includes.patch
Patch3:         tomoe-0.6.0-fixes-set-parse-error.patch
Patch4:         tomoe-strerror.patch
%if %{python_binding}
%endif
%if %{ruby_binding}
%endif
# oreon:deps
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl(XML::Parser)
BuildRequires:  python3
# /oreon:deps
%description
A program which does Japanese handwriting recognition.

%package devel
Summary:    Tomoe development files
Requires:   %{name} = %{version}-%{release}
%description devel
The tomoe-devel package includes the header files for the tomoe package.
Install this package if you want to develop programs which use tomoe.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0 -b .multiarch-conflict
%patch -P1 -p0 -b .bz502662
%patch -P2 -p1 -b .glib
%patch -P3 -p1 -b .compile
%patch -P4 -p1 -b .strerror

%build

./autogen.sh
%configure --disable-static --enable-gtk-doc
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
%if !%{ruby_binding}
rm -f $RPM_BUILD_ROOT%{_libdir}/ruby/site_ruby/*/tomoe.rb $RPM_BUILD_ROOT%{_libdir}/ruby/site_ruby/*/*-linux/*
%endif
chmod 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/xml2est.rb
find ${RPM_BUILD_ROOT}%{_libdir} -name '*.la' | xargs rm
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tomoe-devel -f %{oreon_filedir}/tomoe-devel.list

%changelog

%autochangelog
