Summary: imake source code configuration and build system
Name: imake
Version: 1.0.10
Release: 6%{?dist}
License: MIT-open-group AND HPND
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/util/imake-%{version}.tar.xz
Source1: https://www.x.org/pub/individual/util/makedepend-1.0.8.tar.xz
Source2: https://www.x.org/pub/individual/util/gccmakedep-1.0.3.tar.bz2
Source3: https://www.x.org/pub/individual/util/xorg-cf-files-1.0.8.tar.xz
Source4: https://www.x.org/pub/individual/util/lndir-1.0.4.tar.xz
Patch11: imake-1.0.2-abort.patch
Patch12: xorg-cf-files-1.0.8-DEFAULT_SOURCE.patch
# oreon url source checksums begin
%global source0_sha256 75decbcea8d7b354cf36adc9675e53c4790ee3de56a14bd87b42c8e8aad2ecf5
%global source0_file imake-1.0.10.tar.xz
%global source1_sha256 bfb26f8025189b2a01286ce6daacc2af8fe647440b40bb741dd5c397572cba5b
%global source1_file makedepend-1.0.8.tar.xz
%global source2_sha256 b275dcf1f7323ed89e8b36f8fbd5da665d8700005f1779fa5b90a1688bbf2ee4
%global source2_file gccmakedep-1.0.3.tar.bz2
%global source3_sha256 7408955defcfab0f44d1bedd4ec0c20db61914917ad17bfc1f1c9bf56acc17b9
%global source3_file xorg-cf-files-1.0.8.tar.xz
%global source4_sha256 3e3437a9d3bb377755dd04a2c90d4c014d9fe90987ff73450bf5b8d161795e87
%global source4_file lndir-1.0.4.tar.xz
# oreon url source checksums end

BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-proto-devel
BuildRequires: gcc
BuildRequires: gcc-c++
# imake is not functional without cc
Requires:      gcc

Provides: ccmakedep cleanlinks gccmakedep lndir makedepend makeg
Provides: mergelib mkdirhier mkhtmlindex revpath xmkmf

%description
Imake is a deprecated source code configuration and build system which
has traditionally been supplied by and used to build the X Window System
in X11R6 and previous releases.  As of the X Window System X11R7 release,
the X Window system has switched to using GNU autotools as the primary
build system, and the Imake system is now deprecated, and should not be
used by new software projects.  Software developers are encouraged to
migrate software to the GNU autotools system.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/imake-1.0.10.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "75decbcea8d7b354cf36adc9675e53c4790ee3de56a14bd87b42c8e8aad2ecf5" || { echo "oreon: Source0 SHA256 mismatch for imake-1.0.10.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/makedepend-1.0.8.tar.xz; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bfb26f8025189b2a01286ce6daacc2af8fe647440b40bb741dd5c397572cba5b" || { echo "oreon: Source1 SHA256 mismatch for makedepend-1.0.8.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/gccmakedep-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b275dcf1f7323ed89e8b36f8fbd5da665d8700005f1779fa5b90a1688bbf2ee4" || { echo "oreon: Source2 SHA256 mismatch for gccmakedep-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/xorg-cf-files-1.0.8.tar.xz; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7408955defcfab0f44d1bedd4ec0c20db61914917ad17bfc1f1c9bf56acc17b9" || { echo "oreon: Source3 SHA256 mismatch for xorg-cf-files-1.0.8.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/lndir-1.0.4.tar.xz; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3e3437a9d3bb377755dd04a2c90d4c014d9fe90987ff73450bf5b8d161795e87" || { echo "oreon: Source4 SHA256 mismatch for lndir-1.0.4.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -c %{name}-%{version} -a1 -a2 -a3 -a4

# imake patches
pushd %{name}-%{version}
%patch -P 11 -p1 -b .abort
popd
pushd xorg-cf-files-1.0.8
%patch -P 12 -p1 -b .defaultsource
popd

%build
# Build everything
{
   for pkg in imake makedepend gccmakedep lndir xorg-cf-files ; do
      pushd $pkg-*
      case $pkg in
         imake|xorg-cf-files)
            %configure --with-config-dir=%{_datadir}/X11/config
            ;;
         *)
            %configure
            ;;
      esac
      make
      popd
   done
}

%install
# Install everything
{
   for pkg in imake makedepend gccmakedep lndir xorg-cf-files ; do
      pushd $pkg-*
      make install DESTDIR=$RPM_BUILD_ROOT
      popd
   done
}

%files
%{_bindir}/ccmakedep
%{_bindir}/cleanlinks
%{_bindir}/gccmakedep
%{_bindir}/imake
%{_bindir}/lndir
%{_bindir}/makedepend
%{_bindir}/makeg
%{_bindir}/mergelib
%{_bindir}/mkdirhier
%{_bindir}/mkhtmlindex
%{_bindir}/revpath
%{_bindir}/xmkmf
%dir %{_datadir}/X11/config
%{_datadir}/X11/config/*.cf
%{_datadir}/X11/config/*.def
%{_datadir}/X11/config/*.rules
%{_datadir}/X11/config/*.tmpl
#%%dir %%{_mandir}/man1x
%{_mandir}/man1/ccmakedep.1*
%{_mandir}/man1/cleanlinks.1*
%{_mandir}/man1/gccmakedep.1*
%{_mandir}/man1/imake.1*
%{_mandir}/man1/lndir.1*
%{_mandir}/man1/makedepend.1*
%{_mandir}/man1/makeg.1*
%{_mandir}/man1/mergelib.1*
%{_mandir}/man1/mkdirhier.1*
%{_mandir}/man1/mkhtmlindex.1*
%{_mandir}/man1/revpath.1*
%{_mandir}/man1/xmkmf.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.10-6
- Prepare for Oreon 11 (RP1)
