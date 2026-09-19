%global source0_hash c8cc9694add6ecf121bda050235ffa68d8307a82c85fbdffe69a8eab5be584c2

%define apidocs 1
%define akonadi_version_min 1.12.90

%global akonadi_version %(pkg-config --modversion akonadi 2>/dev/null || echo %{akonadi_version_min})

%if 0%{?fedora} > 23
%global kf5_akonadi 1
%endif

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name:    kdepimlibs
Summary: KDE PIM Libraries
Version: 4.14.10
Release: 49%{?dist}

# http://techbase.kde.org/Policies/Licensing_Policy
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://cgit.kde.org/%{name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/kdepimlibs-%{version}.tar.xz

## upstream patches: KDE/4.14 branch
Patch1: 0001-Output-warnings-when-ItemSync-fails-to-delete-an-ite.patch
Patch2: 0002-missing-camelcase-headers-for-Akonadi-KABC-and-Akona.patch
Patch3: 0003-Optimization-avoid-double-lookup-in-QHash.patch
Patch4: 0004-Fix-build-broken-by-592ae642b6.patch
Patch5: 0005-FindLibical.cmake-using-LINK_LIBRARIES-in-try_run.patch
Patch6: 0006-Adjust-to-cmake-policy-change.patch
Patch7: 0007-Adjust-to-cmake-policy-change.patch
Patch8: 0008-Fix-CMP0022-warnings.patch
Patch9: 0009-Fix-option-name.patch
Patch10: 0010-Add-min-required-cmake-version-fix-clashes-on-target.patch
Patch11: 0011-Remove-use-of-command-creating-un-useful-output.patch
Patch12: 0012-gpgme-CMakeLists.txt-don-t-install-GpgmeppLibraryDep.patch
Patch13: 0013-Remove-use-of-non-existant-file.patch
Patch14: 0014-AgentManager-avoid-recursion-agentTypeAdded-readAgen.patch
Patch15: 0015-Allow-child-dialogs-to-have-a-separate-akonadi-not-s.patch
Patch16: 0016-fix-windows-build.patch
Patch17: 0017-subscriptiondialog.cpp-make-default-size-a-little-la.patch
Patch18: 0018-find-libical-from-the-Config-files-if-possible.patch
Patch19: 0019-also-copy-over-the-USE_ICAL-flags.patch
Patch20: 0020-kio_pop3-Fix-missing-mimetype-warnings.patch
Patch21: 0021-kimap-loginjob.cpp-support-for-GSSAPI-authentication.patch
Patch22: 0022-ItemSync-use-RID-merge-by-default-allow-optional-swi.patch
Patch23: 0023-addtransportdialog.cpp-make-default-size-a-little-la.patch
Patch24: 0024-Fix-ItemSync-merge-type-fallback.patch
Patch25: 0025-incidenceformatter.cpp-allow-links-in-todo-and-journ.patch
Patch26: 0026-Check-response-content-size-before-accessing-it-in-s.patch
Patch27: 0027-icalformat_p.cpp-Fix-heap-use-after-free-in-readICal.patch
Patch28: 0028-Better-error-message-in-case-of-an-ical-parse-error.patch
Patch29: 0029-Speed-up-the-default-Identity-constructor.patch
Patch30: 0030-Use-KSharedConfig-openConfig-kmail2rc-to-try-and-opt.patch
Patch31: 0031-Bug-346060-fix-deferral-time-of-date-only-recurring-.patch
Patch32: 0032-holidays_ua_uk-updated-Ukrainian-holidays.patch
Patch33: 0033-Akonadi-SpecialCollectionsRequestJob-increase-timeou.patch
Patch34: 0034-holiday_de-by_de-remove-Bu-und-Bettag-as-public-holi.patch
Patch35: 0035-akonadi-collectionstatisticsdelegate.cpp-backport.patch

## upstream patches: vendor/intevation/4.14 branch
Patch43: 0043-Backport-avoid-to-transform-as-a-url-when-we-have-a-.patch

## upstreamable patches
Patch51: fix-build-with-ical-3.0.diff

%{?kdelibs4_requires}
# for kio_smtp plain/login sasl plugins
Requires: cyrus-sasl-plain

BuildRequires: boost-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: gpgme-devel
BuildRequires: kdelibs4-devel >= 4.14
BuildRequires: openldap-devel
BuildRequires: libical-devel >= 0.33
# workaround libical-3.0/cmake bogosity
%if 0%{?fedora} > 27
BuildRequires: libical-glib-devel
%endif
BuildRequires: pkgconfig(akonadi) >= %{akonadi_version_min}
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(QJson)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(xpm) pkgconfig(xtst)
%if 0%{?fedora}
BuildRequires: prison-devel
%endif

%if 0%{?apidocs}
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: qt4-doc
%endif

# For AutoReq cmake-filesystem
BuildRequires: cmake
BuildRequires: make

%description
Personal Information Management (PIM) libraries for KDE 4.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-gpgme%{?_isa} = %{version}-%{release}
Requires: %{name}-kxmlrpcclient%{?_isa} = %{version}-%{release}
Requires: %{name}-akonadi%{?_isa} = %{version}-%{release}
%if ! 0%{?kf5_akonadi}
# akonadi test file conflicts
Conflicts: kf5-akonadi-devel
%endif
Obsoletes: kdepimlibs4-devel < %{version}-%{release}
Provides:  kdepimlibs4-devel = %{version}-%{release}
Requires: boost-devel
# FindQGpgme expects gpgme-devel to be present too
Requires: gpgme-devel
Requires: kdelibs4-devel
%description devel
Header files for developing applications using %{name}.

%package akonadi
Summary: Akonadi runtime support for %{name}
# https://bugzilla.redhat.com/1063698
Conflicts: kdepim-runtime < 1:4.11.80
# when pkg split occurrs, not sure if this is really needed, but... -- Rex
#Obsoletes: kdepimlibs < 4.2.0-3
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: akonadi%{?_isa} >= %{akonadi_version}
%description akonadi
%{summary}.

%package apidocs
Summary: kdepimlibs API documentation
Requires: kde-filesystem
BuildArch: noarch
%description apidocs
This package includes the kdepimlibs API documentation in HTML
format for easy browsing.

%package kxmlrpcclient
Summary: Simple XML-RPC Client support
# when spilt out
Conflicts: kdepimlibs < 4.9.2-5
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
%description kxmlrpcclient
This library contains simple XML-RPC Client support. It is used mainly
by the egroupware module of kdepim, but is a complete client and is
quite easy to use.

%package gpgme
Summary: C++ bindings/wrapper for gpgme
# when spilt out
Conflicts: kdepimlibs < 4.12.2-2
# enforce minimal gpgme runtime
%global gpgme_version %(gpgme-config --version 2> /dev/null || echo 0)
%if "%{?gpgme_version}" != "0"
Requires: gpgme%{?_isa} >= %{gpgme_version}
%endif
%description gpgme
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build

%if 0%{?fedora} > 23
# workaround for rawhide/gcc6 FTBFS
export CXXFLAGS="%{optflags} -Wno-error=deprecated-declarations -Wno-deprecated-declarations"
%endif

mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} .. 
popd

make %{?_smp_mflags} -C %{_target_platform}

# build apidocs
%if 0%{?apidocs}
export QTDOCDIR=`pkg-config --variable=docdir Qt`
kde4-doxygen.sh --doxdatadir=%{_kde4_docdir}/HTML/en/common .
%endif

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# hack around HTML doc multilib conflicts
for doxy_hack in kcontrol/kresources ; do
pushd %{buildroot}%{_kde4_docdir}/HTML/en/${doxy_hack}
bunzip2 index.cache.bz2
sed -i -e 's!<a name="id[a-z]*[0-9]*"></a>!!g' index.cache
bzip2 -9 index.cache
done
popd

# move devel symlinks
mkdir -p %{buildroot}%{_kde4_libdir}/kde4/devel
pushd %{buildroot}%{_kde4_libdir}
for i in lib*.so
do
  case "$i" in
# conflicts with qgppme
    libqgpgme.so)
      linktarget=`readlink "$i"`
      rm -f "$i"
      ln -sf "../../$linktarget" "kde4/devel/$i"
      ;;
# conflicts with kdelibs3
    libkabc.so | libkresources.so)
      linktarget=`readlink "$i"`
      rm -f "$i"
      ln -sf "../../$linktarget" "kde4/devel/$i"
      ;;
# conflicts with kdepim3 (compat)
    libkcal.so)
      linktarget=`readlink "$i"`
      rm -f "$i"
      ln -sf "../../$linktarget" "kde4/devel/$i"
      ;;
  esac
done
popd

# install apidocs
%if 0%{?apidocs}
mkdir -p %{buildroot}%{_kde4_docdir}/HTML/en
cp -prf kdepimlibs-%{version}%{?alphatag}-apidocs %{buildroot}%{_kde4_docdir}/HTML/en/kdepimlibs-apidocs
find %{buildroot}%{_kde4_docdir}/HTML/en/ -name 'installdox' -exec rm -fv {} ';'
%endif

## unpackaged files
# conflicts with kf5-akonadi-mime
rm -fv %{buildroot}%{_kde4_datadir}/config.kcfg/specialmailcollections.kcfg
# conflicts with kf5-kmailtransport, mostly harmless, so can remove unconditionally
rm -fv %{buildroot}%{_kde4_datadir}/config.kcfg/mailtransport.kcfg
%if 0%{?kf5_akonadi}
# conflicts with kf5-akonadi-devel
rm -fv %{buildroot}%{_kde4_bindir}/akonaditest
rm -fv %{buildroot}%{_kde4_bindir}/akonadi2xml
rm -frv %{buildroot}%{_kde4_appsdir}/akonadi_knut_resource/
rm -fv %{buildroot}%{_kde4_libdir}/kde4/akonadi_knut_resource.so
rm -fv %{buildroot}%{_kde4_datadir}/akonadi/agents/knutresource.desktop
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING*
%{_kde4_appsdir}/kabc/
%{_kde4_datadir}/config.kcfg/recentcontactscollections.kcfg
%{_kde4_datadir}/config.kcfg/resourcebase.kcfg
%{_kde4_datadir}/kde4/services/*
%{_kde4_datadir}/kde4/servicetypes/*
%{_kde4_libdir}/libkabc.so.4*
%{_kde4_libdir}/libkabc_file_core.so.4*
%{_kde4_libdir}/libkblog.so.4*
%{_kde4_libdir}/libkcal.so.4*
%{_kde4_libdir}/libkcalcore.so.4*
%{_kde4_libdir}/libkcalutils.so.4*
%{_kde4_libdir}/libkholidays.so.4*
%{_kde4_libdir}/libkimap.so.4*
%{_kde4_libdir}/libkldap.so.4*
%{_kde4_libdir}/libkmbox.so.4*
%{_kde4_libdir}/libkmime.so.4*
%{_kde4_libdir}/libkontactinterface.so.4*
%{_kde4_libdir}/libkpimidentities.so.4*
%{_kde4_libdir}/libkpimtextedit.so.4*
%{_kde4_libdir}/libkpimutils.so.4*
%{_kde4_libdir}/libkresources.so.4*
%{_kde4_libdir}/libktnef.so.4*
%{_kde4_libdir}/libmicroblog.so.4*
%{_kde4_libdir}/libsyndication.so.4*
%{_kde4_libdir}/kde4/kabc_directory.so
%{_kde4_libdir}/kde4/kabc_file.so
%{_kde4_libdir}/kde4/kabc_ldapkio.so
%{_kde4_libdir}/kde4/kabc_net.so
%{_kde4_libdir}/kde4/kabcformat_binary.so
%{_kde4_libdir}/kde4/kcal_local.so
%{_kde4_libdir}/kde4/kcal_localdir.so
%{_kde4_libdir}/kde4/kcm_kresources.so
%{_kde4_libdir}/kde4/kio_imap4.so
%{_kde4_libdir}/kde4/kio_ldap.so
%{_kde4_libdir}/kde4/kio_mbox.so
%{_kde4_libdir}/kde4/kio_nntp.so
%{_kde4_libdir}/kde4/kio_pop3.so
%{_kde4_libdir}/kde4/kio_sieve.so
%{_kde4_libdir}/kde4/kio_smtp.so
%{_kde4_libdir}/kde4/plugins/designer/kholidayswidgets.so
%{_kde4_docdir}/HTML/en/kcontrol/
%{_kde4_docdir}/HTML/en/kioslave/
%{_kde4_appsdir}/libkholidays/
%{_kde4_datadir}/mime/packages/kdepimlibs-mime.xml

%exclude %{_kde4_datadir}/kde4/services/kcm_mailtransport.desktop
%exclude %{_kde4_datadir}/kde4/services/akonadicontact_actions.desktop

%post akonadi -p /sbin/ldconfig
%postun akonadi -p /sbin/ldconfig

%files akonadi
%{_kde4_libdir}/libakonadi-calendar.so.4*
%{_kde4_libdir}/libakonadi-contact.so.4*
%{_kde4_libdir}/libakonadi-kabc.so.4*
%{_kde4_libdir}/libakonadi-kcal.so.4*
%{_kde4_libdir}/libakonadi-kde.so.4*
%{_kde4_libdir}/libakonadi-kmime.so.4*
%{_kde4_libdir}/libakonadi-notes.so.4*
%{_kde4_libdir}/libakonadi-socialutils.so.4*
%{_kde4_libdir}/libakonadi-xml.so.4*
%{_kde4_appsdir}/akonadi/
%{_kde4_appsdir}/akonadi-kde/
%{_kde4_libdir}/libkalarmcal.so.2*
%{_kde4_libdir}/libmailtransport.so.4*
%{_kde4_libdir}/kde4/akonadi_serializer_socialfeeditem.so
%{_kde4_libdir}/kde4/kcm_mailtransport.so
%{_kde4_libdir}/kde4/kcm_akonadicontact_actions.so
%{_kde4_libdir}/kde4/plugins/designer/akonadiwidgets.so
%{_kde4_appsdir}/kconf_update/mailtransports.upd
%{_kde4_appsdir}/kconf_update/migrate-transports.pl
%{_kde4_datadir}/kde4/services/kcm_mailtransport.desktop
%{_kde4_datadir}/kde4/services/akonadicontact_actions.desktop
%{_kde4_datadir}/mime/packages/x-vnd.akonadi.socialfeeditem.xml

%files devel
%if 0%{?fedora} < 24
# Conflicts: kf5-akonadi-devel
%{_kde4_bindir}/akonadi2xml
# akonadi-testing bits
%{_kde4_bindir}/akonaditest
%{_kde4_appsdir}/akonadi_knut_resource/
%{_kde4_libdir}/kde4/akonadi_knut_resource.so
%{_kde4_datadir}/akonadi/agents/knutresource.desktop
%endif
%{_datadir}/dbus-1/interfaces/org.kde.KResourcesManager.xml
%{_datadir}/dbus-1/interfaces/org.kde.pim.IdentityManager.xml
%{_kde4_appsdir}/cmake/modules/*
%{_kde4_includedir}/*
%{_kde4_libdir}/kde4/devel/lib*.so
%{_kde4_libdir}/lib*.so
%{_kde4_libdir}/cmake/KdepimLibs*
%{_kde4_libdir}/gpgmepp/

%if 0%{?apidocs}
%files apidocs
%{_kde4_docdir}/HTML/en/kdepimlibs-apidocs/
%endif

%ldconfig_scriptlets gpgme

%files gpgme
%{_kde4_libdir}/libgpgme++-pth*.so.2*
%{_kde4_libdir}/libgpgme++.so.2*
%{_kde4_libdir}/libqgpgme.so.1*

%ldconfig_scriptlets kxmlrpcclient

%files kxmlrpcclient
%doc kxmlrpcclient/README 
%{_kde4_libdir}/libkxmlrpcclient.so.4*

%changelog
%autochangelog
