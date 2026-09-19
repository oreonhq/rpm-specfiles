%global source0_hash 88212b524f6c029dbe84e2fa259f3b9f6a28f2beb584803d03c08df663bf8b0b

%define		mainver		0.7.1
%define		baserelease	18
%define		repoid		18105

Name:		kreetingkard
Version:	%{mainver}
Release:	%{baserelease}%{?dist}
Summary:	Japanese greeting card writing software for KDE

# SPDX confirmed
License:	GPL-2.0-or-later
URL:		http://linux-life.net/program/cc/kde/app/kreetingkard/
Source0:	http://downloads.sourceforge.jp/%{name}/%{repoid}/%{name}-%{mainver}.tar.gz
# From Mandriva
Patch0:		kreetingkard-0.7.1-fix-build-gcc411.patch
# Patch to detect strlcpy on Fedora 39 glibc, by avoiding
# -pedantic error with std::exit
Patch1:		kreetingkard-0.7.1-configure-no-std-exit-for-strlcpy-detection.patch

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	kdelibs3-devel
BuildRequires:	libjpeg-devel

%description
KreetingKard is a tool for making Japanese greeting cards. It allows you to 
make greeting cards easily by choosing a template and changing the words.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .gcc41
%patch -P1 -p1 -b .strlcpy

cp -p configure configure.orig
sed -i configure \
	-e 's|grep klineedit|grep -i klineedit|' \
	-e '\@x_direct_test_function@,\@main@s@int@#include <X11/Intrinsic.h>\nint@' \
	-e 's|\(${x_direct_test_function}\)()|\1(0)|' \
	%{nil}
sed -i configure \
	-e 's|hardcode_libdir_flag_spec=|hardcode_libdir_flag_spec_goodby=|'

%build
# modify qt.sh
# add aarch64 entry to be sure
cp -a %_sysconfdir/profile.d/qt.sh .
sed -i qt.sh -e 's@ppc64le@ppc64le | aarch64 @'
unset QTDIR
# explicitly source
source ./qt.sh

# Don't call autoheader
touch -r configure \
	config.h.in config.h

%configure

# Remove rpath
for f in `find . -name Makefile` ; do
	%{__sed} -i.rpath -e 's|^\([A-Z][A-Z]*_RPATH = \).*|\1|' $f
done

%make_build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%make_install

# Fixing up
# 1. Desktop file treatment
%{__sed} -i -e '/^Pattern/d' \
	$RPM_BUILD_ROOT%{_datadir}/applnk/Office/%{name}.desktop
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
	--add-category Office \
	--delete-original \
	$RPM_BUILD_ROOT%{_datadir}/applnk/Office/%{name}.desktop
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/applnk/

# 2 KDE common symlink to relative
unlink $RPM_BUILD_ROOT%{_defaultdocdir}/HTML/en/%{name}/common
%{__ln_s} -f '../common' $RPM_BUILD_ROOT%{_defaultdocdir}/HTML/en/%{name}/common

# 3 Install icons
for s in 16 32 ; do
	%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/
	%{__install} -cp -m 644 src/cr${s}-app-%{name}.png \
		$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done

# 4. gettext .mo file
%{find_lang} %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc	AUTHORS
%license	COPYING
%doc	README

%{_bindir}/%{name}

%{_datadir}/apps/%{name}/
%{_datadir}/icons/crystalsvg/??x??/*/*.png
%{_datadir}/mimelnk/application/x-%{name}.desktop

%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/??x??/apps/%{name}.png

%{_defaultdocdir}/HTML/en/%{name}/

%changelog
%autochangelog
