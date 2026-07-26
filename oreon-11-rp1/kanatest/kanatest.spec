%global source0_hash 88c764f808381a9a5b996e4e8a5246ac43a7822fafd604135474bdf1b5d46f2a

%global git_snapshot 1

%if 0%{?git_snapshot}
%global git_rev  19dd1a7df9e1cd1c72a47b091ffeac5c0eabb354
%global git_date 20170810
%global git_short %(echo %{git_rev} | cut -c-8)
%global git_version D%{git_date}git%{git_short}
%endif

%global mainver 0.4.10
%global mainrel 0.1

Name:           kanatest
Version:        %{mainver}
Release:        %{mainrel}%{?git_version:.%{?git_version}}%{?dist}.19
Summary:        Hiragana and Katakana drill tool

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://clayo.org/kanatest/
%if 0%{?git_snapshot}
Source0:        %{name}-%{version}-%{?git_version}.tar.bz2
%else
Source0:        http://clayo.org/kanatest/%{name}-%{version}.tar.gz
%endif
# Shell script to create tarball from git scm
Source100:      create-tarball-from-git.sh

BuildRequires:  desktop-file-utils >= 0.9
BuildRequires:  gtk2-devel >= 2.0
BuildRequires:  libxml2-devel
BuildRequires:  gettext
%if 0%{?git_snapshot}
BuildRequires:  automake
BuildRequires:  libtool
%endif
BuildRequires: make
Requires:       font(:lang=ja)
Requires:       hicolor-icon-theme

%description
Kanatest is a simple, GTK 2-based kana drill tool. It offers three drill modes:
hiragana, katakana, and mixed mode. The tester shows random kana characters
and waits until you enter the romaji equivalent in an entry field. At the end,
statistics are provided

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q %{?git_version:-n %{name}-%{version}-%{?git_version}}

sed -i \
	src/Makefile.in \
%if 0%{?git_snapshot}
	src/Makefile.am \
%endif
	-e 's|DISABLE_DEPRECATED|ENABLE_DEPRECATED|g'

%build
%if 0%{?git_snapshot}
bash autogen.sh
%endif

export PLATFORM_CFLAGS="$RPM_OPT_FLAGS -Werror-implicit-function-declaration"
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

%files -f %{name}.lang
%doc README COPYING ChangeLog
%{_bindir}/kanatest
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/kanatest.png
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/22x22/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/scalable/apps/*

%changelog
%autochangelog
