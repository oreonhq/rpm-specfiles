%global source0_hash 4c681d38d127ee3950a29bce9aa7aa8a2abe3b4d915f7a0c88e526999c1a46f2

Name:           gtkimageview
Version:        1.6.4
Release:        36%{?dist}
Summary:        Simple image viewer widget

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://trac.bjourne.webfactional.com
# To download directly, use this URL:
# Source0:        http://trac.bjourne.webfactional.com/attachment/wiki/WikiStart/gtkimageview-%{version}.tar.gz?format=raw
Source0:        gtkimageview-%{version}.tar.gz
# Fix FTBFS. https://bugzilla.redhat.com/show_bug.cgi?id=1307603
Patch0:         gtkimageview-1.6.4-no-werror.patch

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel >= 2.8.0
BuildRequires:  gtk-doc >= 1.0
BuildRequires:  pkgconfig
BuildRequires: make

%description
GtkImageView is a simple image viewer widget for GTK. It makes writing image
viewing and editing applications easy.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .no-werror

%build
%configure --disable-static
make %{?_smp_mflags}
make %{?_smp_mflags} check

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc COPYING README
%{_libdir}/*.so.*

%files devel
%doc %{_datadir}/gtk-doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gtkimageview.pc

%changelog
%autochangelog
