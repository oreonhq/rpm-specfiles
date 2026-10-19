%global source0_hash none
%define _kde4_prefix %_prefix
%define _kde4_sysconfdir %_sysconfdir
%define _kde4_libdir %_libdir
%define _kde4_libexecdir %_libexecdir/kde4
%define _kde4_datadir %_datadir
%define _kde4_sharedir %_datadir
%define _kde4_iconsdir %_kde4_sharedir/icons
%define _kde4_configdir %_kde4_sharedir/config
%define _kde4_appsdir %_kde4_sharedir/kde4/apps
%define _kde4_docdir %_kde4_prefix/share/doc
%define _kde4_bindir %_kde4_prefix/bin
%define _kde4_sbindir %_kde4_prefix/sbin
%define _kde4_includedir %_kde4_prefix/include/kde4
%define _kde4_buildtype release
%define _kde4_macros_api 2
%define rpm_macros_dir %{_rpmconfigdir}/macros.d
Summary:        KDE filesystem layout
Name: kde-filesystem
Version: 5
Release:        1%{?dist}
License: LicenseRef-Not-Copyrightable
Obsoletes: kde-filesystem < 4-36
Source1:        teamnames
Source2:        macros.kde4
Source3:        applnk-hidden-directory
Requires:  filesystem
Requires:  rpm
# oreon:deps
BuildRequires:  gawk
# /oreon:deps
%description
This package provides some directories that are required/used by KDE. 

%package -n kde3-filesystem
Summary: Filesystem for KDE 3
Requires: %{name} = %{version}-%{release}
%description -n kde3-filesystem
This package provides some directories that are required/used by KDE 3 applications.

%package -n kde4-filesystem
Summary: Filesystem and RPM macros for KDE 4
Provides: kde4-macros(api) = %{_kde4_macros_api}
Requires: %{name} = %{version}-%{release}
%description -n kde4-filesystem
This package provides some directories that are required/used by KDE 4 applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%build

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/kde/{env,shutdown,kdm}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/{applications/kde,applnk,apps,autostart,config,config.kcfg,emoticons,mimelnk,services,servicetypes,templates,source}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/locolor/{16x16,22x22,32x32,48x48}/{actions,apps,mimetypes}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applnk/{.hidden,Applications,Edutainment,Graphics,Internet,Settings,System,Toys,Utilities}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mimelnk/{all,application,audio,fonts,image,inode,interface,media,message,model,multipart,print,text,uri,video}
mkdir -p $RPM_BUILD_ROOT%{_prefix}/{lib,%{_lib}}/kde3/plugins
mkdir -p $RPM_BUILD_ROOT%{_docdir}/HTML/en
rm -f %{name}.list
for locale in $(grep '=' %{SOURCE1} | awk -F= '{print $1}') ; do
 mkdir -p $RPM_BUILD_ROOT%{_docdir}/HTML/${locale}/common
 mkdir -p $RPM_BUILD_ROOT%{_docdir}/HTML/${locale}/docs/
 ln -s ../common $RPM_BUILD_ROOT%{_docdir}/HTML/${locale}/docs/common
 echo "%lang($locale) %{_docdir}/HTML/$locale/" >> %{name}.list
done
install -p -m644 -D %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/applnk/.hidden/.directory
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm \
         $RPM_BUILD_ROOT%{_kde4_sysconfdir}/kde/{env,shutdown,kdm} \
         $RPM_BUILD_ROOT%{_kde4_includedir} \
         $RPM_BUILD_ROOT%{_kde4_libexecdir} \
         $RPM_BUILD_ROOT%{_kde4_appsdir}/color-schemes \
         $RPM_BUILD_ROOT%{_kde4_appsdir}/solid/actions \
         $RPM_BUILD_ROOT%{_kde4_datadir}/applications/kde4 \
         $RPM_BUILD_ROOT%{_kde4_datadir}/{autostart,wallpapers} \
         $RPM_BUILD_ROOT%{_kde4_configdir} \
         $RPM_BUILD_ROOT%{_kde4_sharedir}/config.kcfg \
         $RPM_BUILD_ROOT%{_kde4_sharedir}/emoticons \
         $RPM_BUILD_ROOT%{_kde4_sharedir}/kde4/services/ServiceMenus \
         $RPM_BUILD_ROOT%{_kde4_sharedir}/kde4/servicetypes \
         $RPM_BUILD_ROOT%{_kde4_sharedir}/templates/.source \
         $RPM_BUILD_ROOT%{_kde4_datadir}/icons/locolor/{16x16,22x22,32x32,48x48}/{actions,apps,mimetypes} \
         $RPM_BUILD_ROOT%{_kde4_docdir}/HTML/en/common
mkdir -p $RPM_BUILD_ROOT%{_kde4_prefix}/{lib,%{_lib}}/kde4/plugins/{gui_platform,styles}
for locale in $(grep '=' %{SOURCE1} | awk -F= '{print $1}') ; do
  mkdir -p $RPM_BUILD_ROOT%{_kde4_docdir}/HTML/${locale}/common
  echo "%lang($locale) %{_kde4_docdir}/HTML/$locale/" >> %{name}.list
done
mkdir -p $RPM_BUILD_ROOT%{rpm_macros_dir}
cat >$RPM_BUILD_ROOT%{rpm_macros_dir}/macros.kde4<<EOF
%%_kde4_prefix %%_prefix
%%_kde4_sysconfdir %%_sysconfdir
%%_kde4_libdir %%_libdir
%%_kde4_libexecdir %%_libexecdir/kde4
%%_kde4_datadir %%_datadir
%%_kde4_sharedir %%_datadir
%%_kde4_iconsdir %%_kde4_sharedir/icons
%%_kde4_configdir %%_kde4_sharedir/config
%%_kde4_appsdir %%_kde4_sharedir/kde4/apps
%%_kde4_docdir %_kde4_prefix/share/doc
%%_kde4_bindir %%_kde4_prefix/bin
%%_kde4_sbindir %%_kde4_prefix/sbin
%%_kde4_includedir %%_kde4_prefix/include/kde4
%%_kde4_buildtype %_kde4_buildtype
%%_kde4_macros_api %_kde4_macros_api
EOF
cat %{SOURCE2} >> $RPM_BUILD_ROOT%{rpm_macros_dir}/macros.kde4
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/plasma-workspace/{env,shutdown}
mkdir -p $RPM_BUILD_ROOT%{_prefix}/{lib,%{_lib}}/kconf_update_bin
mkdir -p $RPM_BUILD_ROOT%{_datadir}/kconf_update
mkdir -p $RPM_BUILD_ROOT%{_datadir}/knsrcfiles
mkdir -p $RPM_BUILD_ROOT%{_datadir}/kpackage/{genericqml,kcms}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/solid/{actions,devices}
%oreon_autofiles kde3-filesystem usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles kde4-filesystem usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kde3-filesystem -f %{oreon_filedir}/kde3-filesystem.list
%files -n kde4-filesystem -f %{oreon_filedir}/kde4-filesystem.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5-7
- Import
