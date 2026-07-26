%global source0_hash 1765be99f3d83cc57e1ec13a2bb963469b8e91b60239eeaab61d66d7744496e6

%global major_ver 0.1

Name:           gnome-js-common
Version:        %{major_ver}.2
Release:        34%{?dist}
Summary:        Common modules for GNOME JavaScript interpreters

# LGPLv3 part still being clarified with upstream
# Automatically converted from old format: BSD and MIT and LGPLv3 - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND LGPL-3.0-only
URL:            http://ftp.gnome.org/pub/GNOME/sources/%{name}
Source0:        ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{major_ver}/%{name}-%{version}.tar.bz2
# http://git.gnome.org/browse/gnome-js-common/patch/?id=d6ba3133f44ec888af8d64c87822d1bff7c891fe
Patch0:         %{name}-0.1.2-license.patch

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires: make

%description
This package contains some JavaScript modules for use by GNOME
JavaScript extensions, namely GJS and Seed.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .license

%build
# not using standard configure macro. Nothing is compiled,
# make libdir point to %%{_datadir}
%configure --prefix=%{_prefix} --libdir=%{_datadir}
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%files
%doc COPYING ChangeLog
%{_datadir}/gnome-js
%exclude %{_docdir}/gnome_js_common

%files devel
%{_datadir}/pkgconfig/gnome-js-common.pc

%changelog
%autochangelog
