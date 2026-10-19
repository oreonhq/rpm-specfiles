%global source0_hash dfadcba64512f9e3037358b5ccfa264aa4db9e91343e8ff84588000a63fa2905
%global debug_package %{nil}
Name:		cdcollect
Version:	0.6.0
Release:        48%{?dist}
Summary:        Simple CD/DVD catalog for GNOME
License:	GPL-2.0-or-later
URL:		http://cdcollect.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		cdcollect-libdir.patch
Patch1:		cdcollect-0.6.0.patch
Patch2:		cdcollect-0.6.0-sqlite.patch
Requires:	mono-core >= 1.1.17, gtk-sharp2 >= 2.8.0, gnome-sharp
Requires:	sqlite >= 3.3.5, mono-data-sqlite
Requires(pre):	GConf2
Requires(post):	GConf2
Requires(preun):GConf2
ExclusiveArch: %{mono_arches}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gnome-sharp-devel
BuildRequires:  gtk-sharp2-devel
BuildRequires:  make
BuildRequires:  mono-data-sqlite
BuildRequires:  mono-devel
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(strict)
BuildRequires:  sqlite-devel
# /oreon:deps
%description
CDCollect is a simple CD/DVD catalog for GNOME written in C# using Mono
and GTK#. All data are stored in a sqlite database.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1 -b .sqlite

%build

%configure --disable-schemas-install
make %{?_smp_mflags}
%install
%make_install
desktop-file-install --remove-category="Application" \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%pre

if [ "$1" -gt 1 ]; then
	export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
	gconftool-2 --makefile-uninstall-rule \
		%{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :
fi
%post

export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
	%{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
%preun

if [ "$1" -eq 0 ]; then
	export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
	gconftool-2 --makefile-uninstall-rule \
		%{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
