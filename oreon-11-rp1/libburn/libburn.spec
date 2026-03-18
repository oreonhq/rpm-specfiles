%global pkgname libburn

Summary:         Library for reading, mastering and writing optical discs
Name:            libburn
Version:         1.5.6
Release:         8%{?dist}
License:         GPL-2.0-or-later
URL:             https://libburnia-project.org/
Source0:         https://files.libburnia-project.org/releases/%{pkgname}-%{version}.tar.gz
Source1:         https://files.libburnia-project.org/releases/%{pkgname}-%{version}.tar.gz.sig
Source2:         https://keys.openpgp.org/vks/v1/by-fingerprint/44BC9FD0D688EB007C4DD029E9CBDFC0ABC0A854
Patch0:          libburn-0.6.16-multilib.patch
Patch1:          libburn-1.5.4-rpath.patch
Patch2:          https://dev.lovelyhq.com/libburnia/libburn/commit/d537f9dd35282df834a311ead5f113af67d223b3.patch#/libburn-1.5.6-c23.patch
BuildRequires:   gnupg2
BuildRequires:   gcc, make, intltool, gettext
%if 0%{?rhel} && "%{name}" != "%{pkgname}"
BuildRequires:   autoconf, automake, libtool, pkgconfig
%global variant 1
%endif

%description
Libburn is a library by which preformatted data get onto optical media:
CD, DVD and BD (Blu-Ray). It also offers a facility for reading data
blocks from its drives without using the normal block device I/O, which
has advantages and disadvantages. It seems appropriate, nevertheless,
to do writing and reading via same channel. On several Linux systems,
the block device driver needs reloading of the drive tray in order to
make available freshly written data. The libburn read function does not
need such a reload. The code of libburn is independent of cdrecord.

%package         devel
Summary:         Development files for %{name}
Requires:        %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description     devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if 0%{!?_without_doc:1}
%package doc
Summary:         Documentation files for %{name}
BuildArch:       noarch
BuildRequires:   doxygen, graphviz

%description doc
Libburn is a library by which preformatted data get onto optical media:
CD, DVD and BD (Blu-Ray). This package contains the API documentation
for developing applications that use %{name}.
%endif

%package -n      cdrskin%{?variant}
Summary:         Limited cdrecord compatibility wrapper to ease migration to %{name}
Requires:        %{name}%{?_isa} = %{version}-%{release}
Requires(post):  %{?el8:/usr/sbin/}alternatives, coreutils
Requires(preun): %{?el8:/usr/sbin/}alternatives

%description -n cdrskin%{?variant}
A limited cdrecord compatibility wrapper which allows to use some %{name}
features from the command line.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{pkgname}-%{version}

# Rename from libburn to libburn1 for EPEL
%if 0%{?rhel} && "%{name}" != "%{pkgname}"
sed -e 's@libburn_libburn@libburn_libburn1@g' \
    -e 's@libburn/libburn.la@libburn/libburn1.la@g' \
    -e 's@(includedir)/libburn@(includedir)/libburn1@g' \
    -e 's@libburn-1.pc@libburn1-1.pc@g' -i Makefile.am
sed -e 's@libburn-1.pc@libburn1-1.pc@g' -i configure.ac
sed -e 's@burn@burn1@g' libburn-1.pc.in > libburn1-1.pc.in

libtoolize --force
autoreconf --force --install
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

# RHEL ships a cdrskin package already
%if 0%{?rhel} && "%{name}" != "%{pkgname}"
mv -f $RPM_BUILD_ROOT%{_bindir}/cdrskin{,%{?variant}}
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/cdrskin{,%{?variant}}.1
%endif

# Prepare alternatives handling for cdrecord -> cdrskin
touch $RPM_BUILD_ROOT{%{_bindir}/cdrecord,%{_mandir}/man1/cdrecord.1.gz}

%ldconfig_scriptlets

%post -n cdrskin%{?variant}
alternatives --install %{_bindir}/cdrecord cdrecord %{_bindir}/cdrskin%{?variant} 50 \
  --slave %{_mandir}/man1/cdrecord.1.gz cdrecord-cdrecordman %{_mandir}/man1/cdrskin%{?variant}.1.gz

%preun -n cdrskin%{?variant}
if [ $1 -eq 0 ]; then
  alternatives --remove cdrecord %{_bindir}/cdrskin%{?variant}
fi

%files
%license COPYING
%doc AUTHORS COPYRIGHT README
%{_libdir}/%{name}*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc

%if 0%{!?_without_doc:1}
%files doc
%doc doc/html/
%endif

%files -n cdrskin%{?variant}
%ghost %{_bindir}/cdrecord
%{_bindir}/cdrskin%{?variant}
%ghost %{_mandir}/man1/cdrecord.1*
%{_mandir}/man1/cdrskin%{?variant}.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.6-8
- Prepare for Oreon 11 (RP1)
