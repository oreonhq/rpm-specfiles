%global source0_hash 82c128d97a68600518b8e3e65ef4d5b123c57f3d5dfa977c7ff733c0fdf80f73
Name:           libzeitgeist
Version:        0.3.18
Release:        1%{?dist}
Summary:        Client library for applications that want to interact with the Zeitgeist daemon
License:        LGPL-2.1-or-later
URL:            https://launchpad.net/libzeitgeist
Source0:        http://launchpad.net/%{name}/0.3/%{version}/+download/%{name}-%{version}.tar.gz
Patch0:         %{name}-disable-log-test.patch
Patch1:         %{name}-tests-glib-2.40-envnull.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
# /oreon:deps
%description
This project provides a client library for applications that want to interact
with the Zeitgeist daemon. The library is written in C using glib and provides
an asynchronous GObject oriented API.

%package        devel
Summary:        Development files for %{name}%{?_isa}
License:        LGPL-2.1-or-later AND GPL-3.0-only
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
make V=1 %{?_smp_mflags}
%check

make check
%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
install -d -p -m 755 %{buildroot}%{_datadir}/vala/vapi
install -D -p -m 644 bindings/zeitgeist-1.0.{vapi,deps} %{buildroot}%{_datadir}/vala/vapi
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -fr %{buildroot}%{_defaultdocdir}/%{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libzeitgeist-devel -f %{oreon_filedir}/libzeitgeist-devel.list

%changelog

%autochangelog
