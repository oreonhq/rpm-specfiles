%global source0_hash f55ad340feb5e2d22b999466f5b4a99a55ea09b30fceabe1bf6db678588a4b83
Name:           xmedcon
Version:        0.25.3
Release:        1%{?dist}
Summary:        A medical image conversion utility and library
License:        LGPL-2.1-or-later AND LicenseRef-Callaway-Copyright-only AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD and libtiff
URL:            http://xmedcon.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         xmedcon-configure.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  libtpcimgio-devel
BuildRequires:  libtpcmisc-devel
BuildRequires:  make
BuildRequires:  nifticlib-devel
# /oreon:deps
%description
This project stands for Medical Image Conversion and is released under the
GNU's (L)GPL license. It bundles the C source code, a library, a flexible
command-line utility and a graphical front-end based on the amazing Gtk+
toolkit.

Its main purpose is image conversion while preserving valuable medical
study information. The currently supported formats are: Acr/Nema 2.0,
Analyze (SPM), Concorde/uPET, DICOM 3.0, CTI ECAT 6/7, InterFile 3.3
and PNG or Gif87a/89a towards desktop applications.

%package devel
Summary: Libraries files for (X)MedCon development
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The xmedcon-devel package contains the header and libraries necessary
for developing programs that make use of the (X)MedCon library (libmdc).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Remove the sources of the nifti, since we're using fedora nifti here
rm -rvf ./libs/nifti/
rm -rvf ./libs/tpc/
# Removed the directories, so we stop Makefile from looking for them too
sed -ibackup  -e 's/nifti// ' -e 's/tpc//' libs/Makefile.am

# Hardcoded to lib, so I need to correct it everywhere
# easier with sed rather than a patch
sed -i \
       -e  "s|tpc_prefix/lib|tpc_prefix/%{_lib}|" \
       -e  "s|nifti_prefix/lib|nifti_prefix/%{_lib}|" configure.ac

# usr/etc eh?
sed -i 's|$(prefix)||' etc/Makefile.am

%build

autoreconf --install
%configure --disable-static --disable-rpath --with-nifti-prefix=%{_prefix} --with-tpc-prefix=%{_prefix} --enable-shared --includedir=%{_includedir}/xmedcon
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i 's|@libdir@|$(rpm -E %{_libdir})|' xmedcon-config.in
%make_build
%install
%make_install
mv -v $RPM_BUILD_ROOT/%{_includedir}/*.h $RPM_BUILD_ROOT/%{_includedir}/%{name}/
install -d $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/
install -m 0644 -p etc/%{name}.png -t $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/
desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE1}
appstream-util validate-relax --nonet ${RPM_BUILD_ROOT}%{_datadir}/metainfo/xmedcon.appdata.xml
find $RPM_BUILD_ROOT -name "*.a" -execdir rm -fv '{}' \;
find $RPM_BUILD_ROOT -name "*.la" -execdir rm -fv '{}' \;
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n xmedcon-devel -f %{oreon_filedir}/xmedcon-devel.list

%changelog

%autochangelog
