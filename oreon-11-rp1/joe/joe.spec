%global source0_hash 6995b28ee20dcdbbcb5a45a4c110642dc96d67748aea27450c74cdb4dd07cc20
Summary:        An easy to use, modeless text editor
Name: joe
Version: 4.8
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://sourceforge.net/projects/joe-editor/
Source0:        http://downloads.sourceforge.net/joe-editor/joe-%{version}.tar.gz
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Patch0: joe-3.7-joerc.patch
Patch1: joe-3.8-selinux.patch
Patch2: joe-3.8-time.patch
Patch4: joe-3.8-indent-ow.patch
Patch5: joe-3.8-aarch64.patch
Patch6: joe-3.8-format-security.patch
Patch7: joe-4.6-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
Joe is a powerful, easy to use, modeless text editor.
It uses the same WordStar keybindings used in Borland's development
environment.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .joerc
%patch -P1 -p1 -b .selinux
%patch -P2 -p1 -b .time
%patch -P4 -p1 -b .of
%patch -P5 -p1 -b .aarch64
%patch -P6 -p1 -b .format-security
%patch -P7 -p1 -b .c99

iconv -f koi8-r -t utf-8 ./man/ru/joe.1.in >./man/ru/joe.1.in.aux
touch -r ./man/ru/joe.1.in ./man/ru/joe.1.in.aux
mv ./man/ru/joe.1.in.aux ./man/ru/joe.1.in
iconv -f ISO_8859-1 -t UTF-8 ChangeLog > ChangeLog.tmp
touch -r ChangeLog ChangeLog.tmp
mv ChangeLog.tmp ChangeLog

%build

%configure --docdir=%{_pkgdocdir}
make  %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
install -c -m 644 joe/TODO setup.hint $RPM_BUILD_ROOT%{_pkgdocdir}
pushd $RPM_BUILD_ROOT/%{_mandir}/man1
ln -s joe.1 jmacs.1
ln -s joe.1 jpico.1
ln -s joe.1 jstar.1
ln -s joe.1 rjoe.1
popd
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
