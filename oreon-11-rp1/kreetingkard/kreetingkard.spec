%global source0_hash 88212b524f6c029dbe84e2fa259f3b9f6a28f2beb584803d03c08df663bf8b0b
%define		mainver		0.7.1
%define		baserelease	18
%define		repoid		18105
Name:		kreetingkard
Version:	%{mainver}
Release:        18%{?dist}
Summary:        Japanese greeting card writing software for KDE
License:	GPL-2.0-or-later
URL:		http://linux-life.net/program/cc/kde/app/kreetingkard/
Source0:        http://downloads.sourceforge.jp/%{name}/%{repoid}/%{name}-%{version}.tar.gz
Patch0:		kreetingkard-0.7.1-fix-build-gcc411.patch
Patch1:		kreetingkard-0.7.1-configure-no-std-exit-for-strlcpy-detection.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kdelibs3-devel
BuildRequires:  libjpeg-devel
BuildRequires:  make
# /oreon:deps
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

cp -a %_sysconfdir/profile.d/qt.sh .
sed -i qt.sh -e 's@ppc64le@ppc64le | aarch64 @'
unset QTDIR
source ./qt.sh
touch -r configure \
	config.h.in config.h
%configure
for f in `find . -name Makefile` ; do
	%{__sed} -i.rpath -e 's|^\([A-Z][A-Z]*_RPATH = \).*|\1|' $f
done
%make_build
%install
%{__rm} -rf $RPM_BUILD_ROOT
%make_install
%{__sed} -i -e '/^Pattern/d' \
	$RPM_BUILD_ROOT%{_datadir}/applnk/Office/%{name}.desktop
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
	--add-category Office \
	--delete-original \
	$RPM_BUILD_ROOT%{_datadir}/applnk/Office/%{name}.desktop
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/applnk/
unlink $RPM_BUILD_ROOT%{_defaultdocdir}/HTML/en/%{name}/common
%{__ln_s} -f '../common' $RPM_BUILD_ROOT%{_defaultdocdir}/HTML/en/%{name}/common
for s in 16 32 ; do
	%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/
	%{__install} -cp -m 644 src/cr${s}-app-%{name}.png \
		$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done
%{find_lang} %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
