%global source0_hash 4831474e78079ea37bf21c32476bf719115f8fac00e944b57da321dfccd5fe1c
%global svn_rev 133722
%global debug_package %{nil}
Name:           gnome-keyring-sharp
Version:        1.0.1
Release:        1%{?dist}
Summary:        Mono implementation of GNOME Keyring
License:        MIT
URL:            http://www.mono-project.com/Libraries#Gnome-KeyRing-Sharp
Source0:        %{name}-%{version}-r%{svn_rev}.tar.bz2
Patch1:         gnome-keyring-sharp-1.0.1-new-api.diff
Patch2:         gnome-keyring-sharp-1.0.1-monodoc-dir.patch
ExclusiveArch:  %mono_arches
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk-sharp2-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mono-devel
BuildRequires:  monodoc
BuildRequires:  ndesk-dbus-devel
# /oreon:deps
%description
gnome-keyring-sharp is a fully managed implementation of libgnome-keyring.

When the gnome-keyring-daemon is running, you can use this to retrive/store
confidential information such as passwords, notes or network services user
information.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files
for developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       monodoc
%description    doc
The %{name}-doc package contains documentation
for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p0 -F 2 -b .new-api
%patch -P2 -p1 -b .monodoc-dir
sed -i "s#gmcs#mcs#g" configure.ac

%build

autoreconf -f -i
%configure --disable-static
make
%install
%make_install
strip $RPM_BUILD_ROOT%{_libdir}/libgnome-keyring-sharp-glue.so
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gnome-keyring-sharp-devel -f %{oreon_filedir}/gnome-keyring-sharp-devel.list
%files -n gnome-keyring-sharp-doc -f %{oreon_filedir}/gnome-keyring-sharp-doc.list

%changelog

%autochangelog
