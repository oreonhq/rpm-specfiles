%global source0_hash 8c9a80b2af4ec24db4a22dc0e0bc478feed0c476df23a17a2792384222312592
%define         repoid           6183
%define		_default_patch_fuzz	2
Name:           manedit
Version:        1.2.1
Release:        1%{?dist}
Summary:        UNIX Manual Page Editor
License:        GPL-2.0-only
URL:            http://freshmeat.net/projects/manedit/
Source0:        http://freshmeat.net/redir/%{name}/%{repoid}/url_bz%{_default_patch_fuzz}/%{name}-%{version}.tar.bz%{_default_patch_fuzz}
Source1:        manedit.desktop
Source2:        manview.desktop
Patch0:         manedit-0.7.1-makefile.patch
Patch1:         manedit-1.2.1-more-manpages.patch
Patch4:		manedit-1.1.1-fix-compilation.patch
Patch5:		manedit-1.1.1-fix-segv-on-manview.patch
Patch6:		manedit-1.1.1-tmpdir.patch
Patch7:		manedit-1.1.1-fix-segv-on-refresh-with-selected.patch
Requires:       man-db
Requires:	xorg-x11-fonts-ISO8859-15-100dpi
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk+-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
ManEdit is a UNIX manual page editor and viewer, 
it is designed specifically for the editing of the 
UNIX manual page format using an integrated XML interface.

NOTE: This is a gtk+ package and some characters,
especially UTF-8 characters will be garbled.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Base Makefile on FreeBSD style
%{__cp} -p ./manedit/Makefile.FreeBSD ./manedit/Makefile
%patch -P0 -p1 -b .fedora
%patch -P4 -p1 -b .compile
%patch -P1 -p1 -b .manpages
%patch -P5 -p1 -b .segv_manview
%patch -P6 -p1 -b .tmpdir
%patch -P7 -p1 -b .segv_refresh

%build

pushd manedit
%{__make} %{?_smp_mflags} -k \
   CC="gcc -Werror-implicit-function-declaration" \
   OPTFLAGS="$RPM_OPT_FLAGS -DHAVE_GZIP -DHAVE_BZIP2" \
   LDFLAGS="-lz -lbz2"
%{__make} manedit.1.out ; %{__mv} -f manedit.1.out manedit.1
popd
%install
%{__rm} -rf $RPM_BUILD_ROOT
pushd manedit
%{__mkdir_p} $RPM_BUILD_ROOT%{_prefix}
%{__make} install PREFIX=$RPM_BUILD_ROOT%{_prefix}
%{__rm} -f $RPM_BUILD_ROOT%{_bindir}/manwrap
desktop-file-install \
   --dir $RPM_BUILD_ROOT%{_datadir}/applications \
   %{SOURCE1} \
   %{SOURCE2}
for size in 32x32 48x48; do
   %{__install} -D -c -p -m 644 images/icon_manedit_${size}.xpm \
      $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${size}/apps/manedit.xpm
done
for size in 16x16 48x48 ; do
   %{__install} -D -c -p -m 644 images/icon_manedit_viewer_${size}.xpm \
      $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${size}/apps/manedit_viewer.xpm
done
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps/
popd
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
