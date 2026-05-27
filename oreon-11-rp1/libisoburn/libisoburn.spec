%global source0_hash 2b80a6f73dd633a5d243facbe97a15e5c9a07644a5e1a242c219b9375a45f71b

%global pkgname libisoburn

%if 0%{?flatpak}
%global _without_kde 1
%endif

Summary:         Library to enable creation and expansion of ISO-9660 filesystems
Name:            libisoburn
Version:         1.5.6
Release:         9%{?dist}
License:         GPL-2.0-or-later
URL:             https://libburnia-project.org/
Source0:         https://files.libburnia-project.org/releases/%{pkgname}-%{version}.tar.gz
Source1:         https://files.libburnia-project.org/releases/%{pkgname}-%{version}.tar.gz.sig
Source2:         https://keys.openpgp.org/vks/v1/by-fingerprint/44BC9FD0D688EB007C4DD029E9CBDFC0ABC0A854
Source3:         xorriso_extract_iso_image.desktop
Patch0:          libisoburn-1.0.8-multilib.patch
Patch1:          libisoburn-1.5.4-rpath.patch
BuildRequires:   gnupg2
BuildRequires:   gcc, gcc-c++, make, readline-devel, libacl-devel, zlib-devel
%if 0%{?rhel} == 7
BuildRequires:   autoconf, automake, libtool
BuildRequires:   libburn1-devel >= %{version}, libisofs1-devel >= %{version}
Requires:        libburn1 >= %{version}, libisofs1 >= %{version}
%else
%if (0%{?rhel} && "%{name}" != "%{pkgname}")
BuildRequires:   autoconf, automake, libtool
%global variant 1
%endif
BuildRequires:   libburn%{?variant}-devel >= %{version}
BuildRequires:   libisofs%{?variant}-devel >= %{version}
Requires:        libburn%{?variant} >= %{version}
Requires:        libisofs%{?variant} >= %{version}
%endif

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
%if 0%{!?_without_kde:1} && (0%{?fedora} || 0%{?rhel} == 7 || (0%{?rhel} && "%{name}" != "%{pkgname}"))
Requires:        kde-filesystem >= 4
Requires:        kf5-filesystem >= 5
%endif
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires(post):  /sbin/install-info
Requires(preun): /sbin/install-info
%endif
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{pkgname}-%{version}

# Use libisofs1 and libburn1 on EPEL
%if 0%{?rhel} == 7 || (0%{?rhel} && "%{name}" != "%{pkgname}")
sed -e 's@\(libisofs\|libburn\)-1.pc@\11-1.pc@g' -i configure.ac
sed -e 's@\(libisofs\|libburn\)/@\11/@g' -i configure.ac */*.[hc] */*/*.cpp
sed -e 's@\(lisofs\|lburn\)@\11@g' -i Makefile.am
touch NEWS; autoreconf --force --install

# Rename from libisoburn to libisoburn1 for EPEL >= 8
%if 0%{?rhel} >= 8
sed -e 's@libisoburn_libisoburn@libisoburn_libisoburn1@g' \
    -e 's@libisoburn/libisoburn.la@libisoburn/libisoburn1.la@g' \
    -e 's@(includedir)/libisoburn@(includedir)/libisoburn1@g' \
    -e 's@libisoburn-1.pc@libisoburn1-1.pc@g' \
    -e 's@ln -s xorriso@ln -s xorriso%{?variant}@g' -i Makefile.am
sed -e 's@libisoburn-1.pc@libisoburn1-1.pc@g' -i configure.ac
sed -e 's@isoburn@isoburn1@g' libisoburn-1.pc.in > libisoburn1-1.pc.in

libtoolize --force
autoreconf --force --install
%endif
%endif

%build
%configure --disable-static
%make_build
%{!?_without_doc:doxygen doc/doxygen.conf}

%install
%make_install

# Don't install any libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la

# Clean up for later usage in documentation
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}

# Install the KDE service menu handler
%if 0%{!?_without_kde:1} && (0%{?fedora} || 0%{?rhel} == 7 || (0%{?rhel} && "%{name}" != "%{pkgname}"))
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/kde4/services/ServiceMenus/xorriso_extract_iso_image.desktop
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/kservices5/ServiceMenus/xorriso_extract_iso_image.desktop
%endif

# RHEL ships a xorriso package already
%if 0%{?rhel} && "%{name}" != "%{pkgname}"
mv -f $RPM_BUILD_ROOT%{_bindir}/osirrox{,%{?variant}}
mv -f $RPM_BUILD_ROOT%{_bindir}/xorrecord{,%{?variant}}
mv -f $RPM_BUILD_ROOT%{_bindir}/xorriso{,%{?variant}}
mv -f $RPM_BUILD_ROOT%{_bindir}/xorrisofs{,%{?variant}}
mv -f $RPM_BUILD_ROOT%{_bindir}/xorriso-dd-target{,%{?variant}}
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/xorrecord{,%{?variant}}.1
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/xorriso{,%{?variant}}.1
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/xorrisofs{,%{?variant}}.1
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/xorriso-dd-target{,%{?variant}}.1
mv -f $RPM_BUILD_ROOT%{_infodir}/xorrecord{,%{?variant}}.info
mv -f $RPM_BUILD_ROOT%{_infodir}/xorriso{,%{?variant}}.info
mv -f $RPM_BUILD_ROOT%{_infodir}/xorrisofs{,%{?variant}}.info
mv -f $RPM_BUILD_ROOT%{_infodir}/xorriso-dd-target{,%{?variant}}.info
%if 0%{!?_without_kde:1}
sed -e 's@ xorriso @ xorriso%{?variant} @g' \
  -i $RPM_BUILD_ROOT%{_datadir}/{kde4/services,kservices5}/ServiceMenus/xorriso_extract_iso_image.desktop
touch -c -r %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/{kde4/services,kservices5}/ServiceMenus/xorriso_extract_iso_image.desktop
%endif
%endif

# Prepare alternatives handling for cdrecord -> xorrecord and mkisofs -> xorriso
touch $RPM_BUILD_ROOT{%{_bindir}/{cdrecord,mkisofs},%{_mandir}/man1/{cdrecord,mkisofs}.1.gz}

# Some file cleanups
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# Don't ship proof of concept for the moment
rm -f $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_mandir}/man1}/xorriso-tcltk*

%check
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$RPM_BUILD_ROOT%{_libdir}"
cd releng
./run_all_auto -x ../xorriso/xorriso || { cat releng_generated_data/log.*; %{!?flatpak:exit 1;} }

%ldconfig_scriptlets

%post -n xorriso%{?variant}
%if 0%{?rhel} == 7
/sbin/install-info %{_infodir}/xorrecord.info.gz %{_infodir}/dir || :
/sbin/install-info %{_infodir}/xorriso.info.gz %{_infodir}/dir || :
/sbin/install-info %{_infodir}/xorrisofs.info.gz %{_infodir}/dir || :
%endif

alternatives --install %{_bindir}/cdrecord cdrecord %{_bindir}/xorrecord%{?variant} 50 \
  --slave %{_mandir}/man1/cdrecord.1.gz cdrecord-cdrecordman %{_mandir}/man1/xorrecord%{?variant}.1.gz
alternatives --install %{_bindir}/mkisofs mkisofs %{_bindir}/xorrisofs%{?variant} 50 \
  --slave %{_mandir}/man1/mkisofs.1.gz mkisofs-mkisofsman %{_mandir}/man1/xorrisofs%{?variant}.1.gz

%preun -n xorriso%{?variant}
if [ $1 -eq 0 ]; then
%if 0%{?rhel} == 7
  /sbin/install-info --delete %{_infodir}/xorrecord.info.gz %{_infodir}/dir || :
  /sbin/install-info --delete %{_infodir}/xorriso.info.gz %{_infodir}/dir || :
  /sbin/install-info --delete %{_infodir}/xorrisofs.info.gz %{_infodir}/dir || :
  /sbin/install-info --delete %{_infodir}/xorriso-dd-target.info.gz %{_infodir}/dir || :
%endif

  alternatives --remove cdrecord %{_bindir}/xorrecord%{?variant}
  alternatives --remove mkisofs %{_bindir}/xorrisofs%{?variant}
fi

%files
%license COPYING
%doc AUTHORS COPYRIGHT README ChangeLog
%{_libdir}/%{name}*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}*.pc

%if 0%{!?_without_doc:1}
%files doc
%doc doc/html/
%endif

%files -n xorriso%{?variant}
%ghost %{_bindir}/cdrecord
%ghost %{_bindir}/mkisofs
%{_bindir}/osirrox%{?variant}
%{_bindir}/xorrecord%{?variant}
%{_bindir}/xorriso%{?variant}
%{_bindir}/xorrisofs%{?variant}
%{_bindir}/xorriso-dd-target%{?variant}
%ghost %{_mandir}/man1/cdrecord.1*
%ghost %{_mandir}/man1/mkisofs.1*
%{_mandir}/man1/xorrecord%{?variant}.1*
%{_mandir}/man1/xorriso%{?variant}.1*
%{_mandir}/man1/xorrisofs%{?variant}.1*
%{_mandir}/man1/xorriso-dd-target%{?variant}.1*
%{_infodir}/xorrecord%{?variant}.info*
%{_infodir}/xorriso%{?variant}.info*
%{_infodir}/xorrisofs%{?variant}.info*
%{_infodir}/xorriso-dd-target%{?variant}.info*
%if 0%{!?_without_kde:1} && (0%{?fedora} || 0%{?rhel} == 7 || (0%{?rhel} && "%{name}" != "%{pkgname}"))
%{_datadir}/kde4/services/ServiceMenus/xorriso_extract_iso_image.desktop
%{_datadir}/kservices5/ServiceMenus/xorriso_extract_iso_image.desktop
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.6-9
- Prepare for Oreon 11 (RP1)
