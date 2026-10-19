%global source0_hash 525f6970eb818f822db75c1526b3122b1af078affa572dce303de37df5c7b088
ExcludeArch:    %{ix86}
%global build_type_safety_c 0
Name:       wcstools
Version:    3.9.7
Release:        1%{?dist}
Summary:        Software utilities to display and manipulate the WCS of a FITS image
License:    GPL-2.0-or-later
URL:        http://tdc-www.harvard.edu/wcstools
Source0:        http://tdc-www.harvard.edu/software/wcstools/%{name}-%{version}.tar.gz
Patch:      wcstools-3.9.7_rename-libwcs-to-libwcstools.patch
Patch:      wcstools-3.9.7_rename-binaries.patch
Patch:      fix_gcc15-c++23.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Wcstools is a set of software utilities, written in C, which create,
display and manipulate the world coordinate system of a FITS or IRAF
image, using specific keywords in the image header which relate pixel
position within the image to position on the sky.  Auxiliary programs
search star catalogs and manipulate images.

%package libs
Summary:    Wcstools shared library
License:    LGPL-2.0-or-later AND LGPL-2.1-only
%description libs
Shared library necessary to run wcstools and programs based on libwcs.

%package devel
Summary:    Libraries, includes, etc. used to develop an application with wcstools
License:    LGPL-2.0-or-later AND LGPL-2.1-only
Requires:   %{name}-libs%{_isa} = %{version}-%{release}
%description devel
This are the files needed to develop an application using wcstools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix wrong FSF address in source headers
# asked upstream by mail to fix this
grep -rl '59 Temple Place, Suite 330, Boston, MA  02111-1307  USA' --include=*.{c,h} | xargs -i@ sed -i 's/59 Temple Place, Suite 330, Boston, MA  02111-1307  USA/51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA./g' @

%build

%make_build
%install
%{__mkdir_p} %{buildroot}%{_libdir}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_includedir}/wcs
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__install} -p bin/* %{buildroot}%{_bindir}
%{__cp} -a libwcs/*.so* %{buildroot}%{_libdir}
%{__install} -p -m 644 libwcs/*.h %{buildroot}%{_includedir}/wcs
%{__install} -p -m 644 man/man1/* %{buildroot}%{_mandir}/man1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n wcstools-libs -f %{oreon_filedir}/wcstools-libs.list
%files -n wcstools-devel -f %{oreon_filedir}/wcstools-devel.list

%changelog

%autochangelog
