%global source0_hash 3eef8eb8a2755da8400e7a4394229475ad4cf1a2f85345720ee1da135a1aec44
Name:             gerbv
Version:          2.10.0
Release:        1%{?dist}
Summary:        Gerber file viewer from the gEDA toolkit
License:          GPL-2.0-only
URL:              https://github.com/gerbv/gerbv
Source0:        https://github.com/gerbv/gerbv/archive/refs/tags/%{name}-%{version}.tar.gz
Patch0:           gerbv-2.10.0-Fix-Fails-GCC15.patch
Requires:         gdk-pixbuf2-modules-extra
# oreon:deps
BuildRequires:  ImageMagick-devel
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-2.0)
# /oreon:deps
%description
Gerber Viewer (gerbv) is a viewer for Gerber files. Gerber files
are generated from PCB CAD system and sent to PCB manufacturers
as basis for the manufacturing process. The standard supported
by gerbv is RS-274X.

gerbv also supports drill files. The format supported are known
under names as NC-drill or Excellon. The format is a bit undefined
and different EDA-vendors implement it different.

gerbv is listed among Fedora Electronic Lab (FEL) packages.

%package      doc
Summary:          Documentation for %{name}
BuildArch:        noarch
%description  doc
Examples and documentation files for %{name}.

%package      devel
Summary:          Header files, libraries and development documentation for %{name}
Requires:         %{name} = %{version}-%{release}
%description  devel
This package contains the header files, libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# use explicit version for compilation and not a git-derived one
sed -i -e "s/m4_esyscmd(utils\/git-version-gen.sh [0-9.]*)/%{version}/" configure.ac

%build

./autogen.sh
%configure                              \
  --enable-unit-mm                      \
  --disable-update-desktop-database     \
  --disable-static   --disable-rpath    \
  CFLAGS="%{build_cflags}"              \
  LDFLAGS="%{build_ldflags}"
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
desktop-file-install --vendor ""               \
    --remove-category Education                \
    --dir %{buildroot}%{_datadir}/applications \
    --delete-original                          \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
%{__rm} -f %{buildroot}%{_libdir}/libgerbv.la
%{__rm} -f  {doc,example}/Makefile*
pushd example/
for dir in * ; do
  [ -d $dir ] && %{__rm} -f $dir/Makefile*
done
popd
pushd doc/
for dir in * ; do
  [ -d $dir ] && %{__rm} -f $dir/Makefile*
done
popd
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gerbv-doc -f %{oreon_filedir}/gerbv-doc.list
%files -n gerbv-devel -f %{oreon_filedir}/gerbv-devel.list

%changelog

%autochangelog
