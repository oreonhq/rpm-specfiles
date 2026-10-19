%global source0_hash 856cbed2b4ccd5127f61c4997a30e642d414247970f69932f25b4b5a81b18d3f
Name:           wordgrinder
Version:        0.8
Release:        1%{?dist}
Summary:        A command line word processor
License:        MIT
URL:            http://cowlark.com/wordgrinder
%global pkgid   %{name}-%{version}
Source0:        https://github.com/davidgiven/%{name}/archive/%{name}-%{version}.tar.gz
Requires:       ncurses-libs lua-filesystem
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libXft-devel
BuildRequires:  lua
BuildRequires:  lua-devel
BuildRequires:  lua-filesystem
BuildRequires:  lua-libs
BuildRequires:  make
BuildRequires:  minizip-devel
BuildRequires:  ncurses-devel
BuildRequires:  ninja-build
BuildRequires:  zlib-devel
# /oreon:deps
%description
WordGrinder is a Unicode-aware character cell word processor that runs in a
terminal (or a Windows console). It is designed to get the hell out of your way
and let you get some work done.

WordGrinder is a word processor for processing words. It is not WYSIWYG. It is
not point and click. It is not a desktop publisher. It is not a text editor. It
does not do fonts and it barely does styles. What it does do is words. It's
designed for writing text. It gets out of your way and lets you type

%package x11
Summary: X11 version of WordGrinder
Requires: %name = %version-%release
Requires: libX11
%description x11
An X11 version of the WordGrinder word processor.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

###############################################################################
%build

PREFIX=$RPM_BUILD_ROOT/%{_prefix} OBJDIR=$RPM_BUILD_ROOT/tmp WANT_STRIPPED_BINARIES=no make %{?_smp_mflags}
%install
make install PREFIX=$RPM_BUILD_ROOT/%{_prefix}
install -D -m 0644 %{_builddir}/%{name}-%{version}/extras/wordgrinder.desktop %{buildroot}%{_datadir}/applications/wordgrinder.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post x11

update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
touch --no-create %{_datadir}/mime/packages &>/dev/null || :
%postun x11

update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    update-mime-database %{_datadir}/mime &> /dev/null || :
fi
%posttrans x11

gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :
%files -f %{oreon_filedir}/main.list
%files -n wordgrinder-x11 -f %{oreon_filedir}/wordgrinder-x11.list

%changelog

%autochangelog
