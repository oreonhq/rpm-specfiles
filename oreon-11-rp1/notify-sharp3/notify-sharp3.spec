%global source0_hash a62ed07850a122e2bb7f2b88b32cf2fa675b60b912c0aeefb23f554ebfb1e56d

%global debug_package %{nil}
%global _docdir_fmt %{name}

Name:           notify-sharp3
Version:        3.0.3
Release:        25%{?dist}
Summary:        A C# implementation for Desktop Notifications

License:        MIT
URL:            https://www.meebey.net/projects/notify-sharp
Source0:        https://www.meebey.net/projects/notify-sharp/downloads/notify-sharp-%{version}.tar.gz

BuildRequires: make
BuildRequires:  mono-devel, gtk-sharp3-devel, gnome-sharp-devel, dbus-sharp-glib-devel
BuildRequires:  autoconf, automake, libtool

BuildRequires:  monodoc-devel
# Mono only available on these:
ExclusiveArch: %{mono_arches}

%description
notify-sharp is a C# client implementation for Desktop Notifications,
i.e. notification-daemon. It is inspired by the libnotify API.

Desktop Notifications provide a standard way of doing passive pop-up
notifications on the Linux desktop. These are designed to notify the
user of something without interrupting their work with a dialog box
that they must close. Passive pop-ups can automatically disappear after
a short period of time.

%package devel
Summary:        Development files for notify-sharp
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development files for notify-sharp

%package doc
Summary:        Documentation files for notify-sharp
Requires:       %{name} = %{version}-%{release}
Requires:       monodoc
BuildArch:      noarch

%description doc
Documentation files for notify-sharp

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn notify-sharp-%{version}

%build
sed -i "s#dbus-sharp-1.0#dbus-sharp-2.0#g" configure.ac
sed -i "s#dbus-sharp-glib-1.0#dbus-sharp-glib-2.0#g" configure.ac
sed -i "s#gmcs#mcs#g" configure.ac
autoreconf --install
%configure --libdir=%{_prefix}/lib --disable-docs
make %{?_smp_mflags}

%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
test "%{_libdir}" = "%{_prefix}/lib" || mv $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig/*.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/

%files
%doc NEWS README AUTHORS
%license COPYING
%{_monogacdir}/notify-sharp/
%{_monodir}/notify-sharp*/

%files devel
%{_libdir}/pkgconfig/notify-sharp*.pc

%files doc

%changelog
%autochangelog
