%global source0_hash 500eaff50628faa75adb3cd560236a4db498d9e7c52c036b78fa9a57f21805b3
Name:           goffice         
Version:        0.10.62
Release:        1%{?dist}
Summary:        G Office support libraries
License:        GPL-2.0-only AND GPL-3.0-only
URL:            http://projects.gnome.org/gnumeric/index.shtml
Source0:        https://download.gnome.org/sources/%{name}/0.10/%{name}-%{version}.tar.xz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  perl(English)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lasem-0.6)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxslt)
# /oreon:deps
%description
Support libraries for gnome office

%package devel
Summary:        Libraries and include files for goffice
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development libraries for goffice

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n goffice-devel -f %{oreon_filedir}/goffice-devel.list

%changelog

%autochangelog
