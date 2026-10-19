%global source0_hash 1d446899697145fc36623d8afdd274066177da9383a6b619c18e8eb1b2ba589a
%define real_name Xdialog
Name: xdialog
Summary:        X11 drop in replacement for cdialog
Version: 2.3.1
Release:        1%{?dist}
License: GPL-1.0-or-later
URL: http://xdialog.free.fr
Source0:        http://%{name}.free.fr/%{real_name}-%{version}.tar.bz2
Patch0: xdialog-2.3.1-nostrip.patch
Patch1: xdialog-2.3.1-secure-fprintf.diff
Patch2: xdialog-2.3.1-configure-c99.patch
Provides: %{real_name} = %{version}-%{release}
Obsoletes: %{real_name} < %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  make
# /oreon:deps
%description
Xdialog is designed to be a drop in replacement for the cdialog program.
It converts any terminal based program into a program with an X-windows
interface. The dialogs are easier to see and use and Xdialog adds even
more functionalities (help button+box, treeview, editbox, file selector,
range box, and much more).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{real_name}-%{version}
iconv -f latin1 -t utf8 ChangeLog > ChangeLog.utf8
touch -c -r ChangeLog ChangeLog.utf8
mv ChangeLog.utf8 ChangeLog
%patch -P0 -p1 -b .nostrip
%patch -P1 -p0 -b .fprintf
%patch -P2 -p1 -b .configure
touch -c -r configure.nostrip configure
touch -c -r configure.in.nostrip configure.in

%build

%configure --with-gtk2
%make_build
sed -i -e 's:%{_datadir}/doc/Xdialog:%{_datadir}/doc/%{name}:g' doc/Xdialog.1
%install
%make_install
rm -rf __dist_html
mkdir -p __dist_html/html
cp -p doc/*.html doc/*.png __dist_html/html
ln -s ../samples __dist_html/html/samples
%find_lang %{real_name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
