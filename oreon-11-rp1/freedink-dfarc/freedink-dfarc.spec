%global source0_hash a51124ecd11eeca0f1d16732ef58ee690e2fa2db06cc0ec2a5b61b41f8b0e8fa

Name:		freedink-dfarc
Version:	3.14
Release:	22%{?dist}
Summary:	Frontend and .dmod installer for GNU FreeDink

License:	GPL-3.0-or-later
URL:		http://www.gnu.org/software/freedink/
Source0:	ftp://ftp.gnu.org/gnu/freedink/dfarc-%{version}.tar.gz
ExcludeArch:    s390x

BuildRequires:  gcc-c++
%if 0%{?suse_version}
BuildRequires:	bzip2, wxWidgets-devel >= 3, intltool, gettext
BuildRequires:	desktop-file-utils, update-desktop-files
%else
BuildRequires:	bzip2-devel, wxGTK-devel, intltool, desktop-file-utils
%endif
BuildRequires: make
Requires:	xdg-utils

%description
DFArc makes it easy to play and manage the Dink Smallwood game and
it's numerous Dink Modules (or D-Mods).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n dfarc-%{version}

%build
# Don't install desktop files, use %%post instead
%configure --disable-desktopfiles
%make_build

%install
%make_install
%find_lang dfarc
desktop-file-validate %{buildroot}/%{_datadir}/applications/%name.desktop
%if 0%{?suse_version}
%suse_update_desktop_file -i %name
%endif

%files -f dfarc.lang
%doc AUTHORS COPYING NEWS README THANKS TODO TRANSLATIONS.txt ChangeLog
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/mime/packages/*
%{_datadir}/pixmaps/*
# Don't include system directories, only added files:
%{_datadir}/icons/hicolor/32x32/mimetypes/*
%{_mandir}/man1/*

%changelog
%autochangelog
