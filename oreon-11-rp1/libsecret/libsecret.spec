%global source0_hash 142948339c5b971d8f6a8c7099521f6fd319b6fe73d2694b4e6d3310ed28b6e6
%ifarch %{valgrind_arches}
%global has_valgrind 1
%endif
%bcond_without gnutls
Name:           libsecret
Version:        0.21.8.2
%global release_version 0.21
Release:        1%{?dist}
Summary:        Library for storing and retrieving passwords and other secrets
License:        LGPL-2.1-or-later AND Apache-2.0 AND (GPL-2.0-or-later OR TGPPL-1.0) AND LicenseRef-Fedora-Public-Domain AND GCR-docs
URL:            https://wiki.gnome.org/Projects/Libsecret
Source0:        https://download.gnome.org/sources/%{name}/%{release_version}/%{name}-%{version}.tar.xz
%if %{with gnutls}
%else
%endif
%if 0%{?has_valgrind}
%endif
Provides:       bundled(egglib)
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  dbus
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  python3-devel
BuildRequires:  vala
# /oreon:deps
%description
libsecret is a library for storing and retrieving passwords and other secrets.
It communicates with the "Secret Service" using DBus. gnome-keyring and
KSecretService are both implementations of a Secret Service.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     gi-docgen-fonts
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        mock-service
Summary:        Python mock-service files from %{name}
Requires:       (%{name} = %{version}-%{release} if %{name})
BuildArch:      noarch
%description    mock-service
The %{name}-mock-service package contains testing Python files from %{name},
for testing of other similar tools, such as the Python SecretStorage package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Use system valgrind headers instead
%if 0%{?has_valgrind}
rm -rf build/valgrind/
%endif

%build

%meson \
%if %{with gnutls}
-Dcrypto=gnutls \
%else
-Dcrypto=libgcrypt \
%endif
%{nil}
%meson_build
%install
%meson_install
%find_lang libsecret
mkdir -p %{buildroot}%{_datadir}/libsecret/mock
cp -a libsecret/mock/*.py %{buildroot}%{_datadir}/libsecret/mock/
cp -a libsecret/mock-service*.py %{buildroot}%{_datadir}/libsecret/
%py_byte_compile %{python3} %{buildroot}%{_datadir}/libsecret/mock/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libsecret-devel -f %{oreon_filedir}/libsecret-devel.list
%files -n libsecret-mock-service -f %{oreon_filedir}/libsecret-mock-service.list

%changelog

%autochangelog
