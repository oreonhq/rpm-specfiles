%global source0_hash 4831474e78079ea37bf21c32476bf719115f8fac00e944b57da321dfccd5fe1c

%if 0%{?rhel}%{?el6}%{?el7}
# see https://fedorahosted.org/fpc/ticket/395
%define _monodir %{_prefix}/lib/mono
%define _monogacdir %{_monodir}/gac
%endif

%global svn_rev 133722
%global debug_package %{nil}

Name:           gnome-keyring-sharp
Version:        1.0.1
Release:        0.46.%{svn_rev}svn%{?dist}
Summary:        Mono implementation of GNOME Keyring

License:        MIT
URL:            http://www.mono-project.com/Libraries#Gnome-KeyRing-Sharp
# Tarfile created from svn snapshot
# svn co -r %{svn-rev} \
#   svn://anonsvn.mono-project.com/source/trunk/gnome-keyring-sharp \
#   gnome-keyring-sharp-%{version}
# tar cjf gnome-keyring-sharp-%{version}-r%{svn_rev}.tar.bz2 --exclude=.svn \
#   gnome-keyring-sharp-%{version}
Source0:        gnome-keyring-sharp-%{version}-r%{svn_rev}.tar.bz2
# Patch to directly p/invoke libgnome-keyring instead of using
# deprecated socket interface taken from upstream bug report:
# https://bugzilla.novell.com/show_bug.cgi?id=589166
Patch1:         gnome-keyring-sharp-1.0.1-new-api.diff
Patch2:         gnome-keyring-sharp-1.0.1-monodoc-dir.patch

# Mono only available on these:
ExclusiveArch:  %mono_arches

BuildRequires:  autoconf automake libtool
BuildRequires:  mono-devel ndesk-dbus-devel monodoc
BuildRequires:  gtk-sharp2-devel libgnome-keyring-devel
BuildRequires: make

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
# sharing violation when doing parallel build
#%{?_smp_mflags}

%install
%make_install
strip $RPM_BUILD_ROOT%{_libdir}/libgnome-keyring-sharp-glue.so
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%doc AUTHORS ChangeLog COPYING README
%{_monodir}/gnome-keyring-sharp-1.0
%{_monogacdir}/Gnome.Keyring
%{_libdir}/libgnome-keyring-sharp-glue.so

%files devel
%{_libdir}/pkgconfig/%{name}-1.0.pc

%files doc
%{_prefix}/lib/monodoc/sources/Gnome.Keyring.*

%changelog
%autochangelog
