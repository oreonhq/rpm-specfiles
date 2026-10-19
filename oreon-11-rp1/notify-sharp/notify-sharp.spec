%global source0_hash fb803a2579dda9e67ffea1bc4fe9228fed08419e588d85e7537dfb7a625a3a80
%global commit 28d2f659985241be222c145719ee5d75aa02b9ee
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20130131
%define debug_package %{nil}
Name:           notify-sharp
Version:        0.4.1
Release:        1%{?dist}
Summary:        A C# implementation for Desktop Notifications
License:        MIT
URL:            https://github.com/hyperair/notify-sharp
Source0:        %{name}-git%{shortcommit}.tar.xz
Patch1:		notify-sharp-0.4.1-dbus2.patch
ExclusiveArch: %{mono_arches}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dbus-sharp-glib-devel
BuildRequires:  gnome-sharp-devel
BuildRequires:  gtk-sharp2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mono-devel
BuildRequires:  monodoc-devel
# /oreon:deps
%description
notify-sharp is a C# client implementation for Desktop Notifications,
i.e. notification-daemon. It is inspired by the libnotify API.

Desktop Notifications provide a standard way of doing passive pop-up
notifications on the Linux desktop. These are designed to notify the
user of something without interrupting their work with a dialog box
that they must close. Passive popups can automatically disappear after
a short period of time.

%package devel
Summary:        Development files for notify-sharp
Requires:       %{name} = %{version}-%{release} 
Requires:       pkgconfig
%description devel
Development files for notify-sharp

%package doc
Summary:        Documentation files for notify-sharp
Requires:       %{name} = %{version}-%{release} 
Requires:       monodoc
%description doc
Documentation files for notify-sharp

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}
%patch -P1 -p1 -b .dbus2

sed -i "s#gmcs#mcs#g" configure.ac

%build

autoreconf -vif
%configure --libdir=%{_prefix}/lib --disable-docs
make
%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
test "%{_libdir}" = "%{_prefix}/lib" || mv $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig/*.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n notify-sharp-devel -f %{oreon_filedir}/notify-sharp-devel.list
%files -n notify-sharp-doc -f %{oreon_filedir}/notify-sharp-doc.list

%changelog

%autochangelog
