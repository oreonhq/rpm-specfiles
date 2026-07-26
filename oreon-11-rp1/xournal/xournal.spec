%global source0_hash b25898dbd7a149507f37a16769202d69fbebd4a000d766923bbd32c5c7462826

Name:		xournal
Version:	0.4.8.2016
Release:	20%{?dist}
Summary:	Notetaking, sketching, PDF annotation and general journal

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://xournal.sourceforge.net/
Source0:	http://downloads.sourceforge.net/xournal/%{name}-%{version}.tar.gz
Patch0:		xournal-c99-1.patch
Patch1:		xournal-c99-2.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	gtk2-devel >= 2.10.0
BuildRequires:	libgnomecanvas-devel >= 2.4.0
%if 0%{?fedora} > 9 || 0%{?rhel} > 5
BuildRequires:	poppler-glib-devel >= 0.5.4
%else
BuildRequires:	poppler-devel >= 0.5.4
%endif
BuildRequires:	autoconf, automake
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick
BuildRequires:	gettext

Requires:	poppler-utils
Requires:	ghostscript

%description
Xournal is an application for notetaking, sketching, keeping a journal and
annotating PDFs. Xournal aims to provide superior graphical quality (subpixel
resolution) and overall functionality.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

NOCONFIGURE=1 ./autogen.sh

%build
CFLAGS="%optflags -DPACKAGE_LOCALE_DIR=\\\"\"%{_datadir}/locale\"\\\" -DPACKAGE_DATA_DIR=\\\"\"%{_datadir}\"\\\"" %configure
%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"

# xournal icons and mime icons
# create 16x16, 32x32, 64x64, 128x128 icons and copy the 48x48 icon
for s in 16 32 48 64 128 ; do
	%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/
	convert -scale ${s}x${s} \
		pixmaps/%{name}.png \
		$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
	%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/${s}x${s}/mimetypes
	pushd ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/${s}x${s}/mimetypes
	%{__ln_s} ../apps/xournal.png application-x-xoj.png
	%{__ln_s} application-x-xoj.png gnome-mime-application-x-xoj.png
	popd
done

# Desktop entry
%{__install} -p -m 0644 -D pixmaps/xournal.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/xournal.png
desktop-file-install \
	--dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
	xournal.desktop

# GNOME (shared-mime-info) MIME type registration
%{__install} -p -m 0644 -D xournal.xml ${RPM_BUILD_ROOT}%{_datadir}/mime/packages/xournal.xml

# KDE (legacy) MIME type registration
%{__install} -p -m 0644 -D x-xoj.desktop ${RPM_BUILD_ROOT}%{_datadir}/mimelnk/application/x-xoj.desktop

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/xournal
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/icons/hicolor/*x*/mimetypes/application-x-xoj.png
%{_datadir}/icons/hicolor/*x*/mimetypes/gnome-mime-application-x-xoj.png
%{_datadir}/pixmaps/xournal.png
%{_datadir}/applications/xournal.desktop
%{_datadir}/mime/packages/xournal.xml
%{_datadir}/mimelnk/application/x-xoj.desktop
%{_datadir}/xournal/
%doc AUTHORS ChangeLog COPYING

%changelog
%autochangelog
