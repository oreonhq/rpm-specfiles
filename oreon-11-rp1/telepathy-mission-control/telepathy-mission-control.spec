%global source0_hash 2df8ae3995e919a7670e01aa3568215ef0777e34961ace1cac1c6477cb297a45
%define tp_glib_ver 0.17.5
%global mc_plugindir %{_libdir}/mission-control-plugins.0
Name:           telepathy-mission-control
Version:        5.16.6
Release:        1%{?dist}
Epoch:          1
Summary:        Central control for Telepathy connection manager
License:        LicenseRef-Callaway-LGPLv2
URL:            https://telepathy.freedesktop.org/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:         6.patch
# oreon:deps
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  chrpath
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  telepathy-glib-devel
# /oreon:deps
%description
Mission Control, or MC, is a Telepathy component providing a way for
"end-user" applications to abstract some of the details of connection
managers, to provide a simple way to manipulate a bunch of connection
managers at once, and to remove the need to have in each program the
account definitions and credentials.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
  --disable-static \
  --enable-gtk-doc \
  --with-connectivity=nm
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool
%{make_build}
%install
%{make_install}
mkdir -p %{buildroot}%{mc_plugindir}
chrpath --list   %{buildroot}%{_libexecdir}/mission-control-5 && \
chrpath --delete %{buildroot}%{_libexecdir}/mission-control-5
find %{buildroot} -type f -name "*.la" -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if %{undefined flatpak}
PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "%{?mc_plugindir}" = "$(pkg-config --variable=plugindir mission-control-plugins 2>/dev/null)"
%endif
make check ||:
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n telepathy-mission-control-devel -f %{oreon_filedir}/telepathy-mission-control-devel.list

%changelog

%autochangelog
