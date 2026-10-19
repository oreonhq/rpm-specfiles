%global source2_hash 153b53c2bbefa5f5e748ff1d0dd6779e5f2c16b0052a4540a929d5d901f24202
%global source1_hash efb5b495b8c021fd6751619c64827048885258ef4bbe4c310de56c4568132b99
%global source0_hash a977b03dc3686d9fdca600458b1578f9cac2b875609bd5ec21f5ada55f20ec50
%global pkgname libisoburn
%if 0%{?flatpak}
%global _without_kde 1
%endif
Summary:        Library to enable creation and expansion of ISO-9660 filesystems
Name:            libisoburn
Version:         1.5.8.pl02
Release:        1%{?dist}
License:         GPL-2.0-or-later
URL:             https://libburnia-project.org/
Source0:        https://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
Source1:        https://files.libburnia-project.org/releases/%{pkgname}-%{version}.tar.gz.sig
Source2:         https://keys.openpgp.org/vks/v1/by-fingerprint/44BC9FD0D688EB007C4DD029E9CBDFC0ABC0A854
Source3:         xorriso_extract_iso_image.desktop
Patch0:          libisoburn-1.0.8-multilib.patch
Patch1:          libisoburn-1.5.4-rpath.patch
Requires:        libburn%{?variant} >= %{version}
Requires:        libisofs%{?variant} >= %{version}
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  graphviz
BuildRequires:  libacl-devel
BuildRequires:  libburn-devel
BuildRequires:  libisofs-devel
BuildRequires:  make
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Libisoburn is a front-end for libraries libburn and libisofs which
enables creation and expansion of ISO-9660 filesystems on all CD/
DVD/BD media supported by libburn. This includes media like DVD+RW,
which do not support multi-session management on media level and
even plain disk files or block devices. Price for that is thorough
specialization on data files in ISO-9660 filesystem images. And so
libisoburn is not suitable for audio (CD-DA) or any other CD layout
which does not entirely consist of ISO-9660 sessions.

%package devel
Summary:         Development files for %{name}
Requires:        %{name}%{?_isa} = %{version}-%{release}, pkgconfig
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if 0%{!?_without_doc:1}
%package doc
Summary:         Documentation files for %{name}
BuildArch:       noarch
BuildRequires:   doxygen, graphviz
%description doc
Libisoburn is a front-end for libraries libburn and libisofs which
enables creation and expansion of ISO-9660 filesystems on all CD/
DVD/BD media supported by libburn. And this package contains the API
documentation for developing applications that use %{name}.
%endif

%package -n xorriso%{?variant}
Summary:         ISO-9660 and Rock Ridge image manipulation tool
URL:             https://scdbackup.sourceforge.net/xorriso_eng.html
Requires:        %{name}%{?_isa} = %{version}-%{release}
Requires(post):  %{?el8:/usr/sbin/}alternatives, coreutils
Requires(preun): %{?el8:/usr/sbin/}alternatives
%description -n xorriso%{?variant}
Xorriso is a program which copies file objects from POSIX compliant
filesystems into Rock Ridge enhanced ISO-9660 filesystems and allows
session-wise manipulation of such filesystems. It can load management
information of existing ISO images and it writes the session results
to optical media or to filesystem objects. Vice versa xorriso is able
to copy file objects out of ISO-9660 filesystems.

Filesystem manipulation capabilities surpass those of mkisofs. Xorriso
is especially suitable for backups, because of its high fidelity of
file attribute recording and its incremental update sessions. Optical
supported media: CD-R, CD-RW, DVD-R, DVD-RW, DVD+R, DVD+R DL, DVD+RW,
DVD-RAM, BD-R and BD-RE.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{pkgname}-%{lua:print((macros.version:gsub("%.pl%d+$","")))}

# Use libisofs1 and libburn1 on EPEL

%build

%configure --disable-static
%make_build
%{!?_without_doc:doxygen doc/doxygen.conf}
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}
touch $RPM_BUILD_ROOT{%{_bindir}/{cdrecord,mkisofs},%{_mandir}/man1/{cdrecord,mkisofs}.1.gz}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_mandir}/man1}/xorriso-tcltk*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$RPM_BUILD_ROOT%{_libdir}"
cd releng
./run_all_auto -x ../xorriso/xorriso || { cat releng_generated_data/log.*; %{!?flatpak:exit 1;} }
%ldconfig_scriptlets
%post -n xorriso%{?variant}

alternatives --install %{_bindir}/cdrecord cdrecord %{_bindir}/xorrecord%{?variant} 50 \
  --slave %{_mandir}/man1/cdrecord.1.gz cdrecord-cdrecordman %{_mandir}/man1/xorrecord%{?variant}.1.gz
alternatives --install %{_bindir}/mkisofs mkisofs %{_bindir}/xorrisofs%{?variant} 50 \
  --slave %{_mandir}/man1/mkisofs.1.gz mkisofs-mkisofsman %{_mandir}/man1/xorrisofs%{?variant}.1.gz
%preun -n xorriso%{?variant}

if [ $1 -eq 0 ]; then
  alternatives --remove cdrecord %{_bindir}/xorrecord%{?variant}
  alternatives --remove mkisofs %{_bindir}/xorrisofs%{?variant}
fi
%files -f %{oreon_filedir}/main.list
%files -n libisoburn-devel -f %{oreon_filedir}/libisoburn-devel.list
%files -n libisoburn-doc -f %{oreon_filedir}/libisoburn-doc.list
%files -n xorriso -f %{oreon_filedir}/xorriso.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.6-9
- Prepare for Oreon 11 (RP1)
