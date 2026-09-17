%global source0_hash 66bfd7e31d2f6756d5a62c3670383cbba02b3cb4c1042950192a801b72a3c9ab

Name:           goffice         
Version:        0.10.57
Release:        4%{?dist}
Summary:        G Office support libraries
License:        GPL-2.0-only AND GPL-3.0-only
URL:            http://projects.gnome.org/gnumeric/index.shtml
Source0:        https://download.gnome.org/sources/%{name}/0.10/%{name}-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.8.7
BuildRequires:  pkgconfig(lasem-0.6) >= 0.6.0
BuildRequires:  pkgconfig(libgsf-1) >= 1.14.24
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.22.0
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  perl(English)
BuildRequires:  perl(IO::Compress::Gzip)

# https://gitlab.gnome.org/GNOME/goffice/-/issues/70
ExcludeArch:    %{ix86}

%description
Support libraries for gnome office

%package devel
Summary:        Libraries and include files for goffice
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for goffice

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure --disable-silent-rules
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install
%find_lang goffice-%{version}
rm $RPM_BUILD_ROOT/%{_libdir}/*.la
rm $RPM_BUILD_ROOT/%{_libdir}/%{name}/%{version}/plugins/*/*.la

%ldconfig_scriptlets

%files -f goffice-%{version}.lang
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_libdir}/*.so.*
%{_libdir}/goffice/
%{_datadir}/goffice/

%files devel
%{_includedir}/libgoffice-0.10/
%{_libdir}/pkgconfig/libgoffice-0.10.pc
%{_libdir}/*.so
%{_datadir}/gtk-doc/html/goffice-0.10/

%changelog
%autochangelog
