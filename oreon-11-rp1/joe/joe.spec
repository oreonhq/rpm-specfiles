%global source0_hash 495a0a61f26404070fe8a719d80406dc7f337623788e445b92a9f6de512ab9de

Summary: An easy to use, modeless text editor
Name: joe
Version: 4.6
Release: 24%{?dist}
License: GPL-2.0-or-later
URL: http://sourceforge.net/projects/joe-editor/
Source: http://downloads.sourceforge.net/joe-editor/joe-%{version}.tar.gz

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Patch0: joe-3.7-joerc.patch
Patch1: joe-3.8-selinux.patch
Patch2: joe-3.8-time.patch
Patch4: joe-3.8-indent-ow.patch
Patch5: joe-3.8-aarch64.patch
Patch6: joe-3.8-format-security.patch
# https://sourceforge.net/p/joe-editor/mercurial/merge-requests/3/
Patch7: joe-4.6-c99.patch

BuildRequires: gcc make
BuildRequires: ncurses-devel libselinux-devel

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

# This is automatically compressed afterwards...
pushd $RPM_BUILD_ROOT/%{_mandir}/man1
ln -s joe.1 jmacs.1
ln -s joe.1 jpico.1
ln -s joe.1 jstar.1
ln -s joe.1 rjoe.1
popd

%files
%license COPYING
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/*
%{_bindir}/*
%dir /etc/joe
%config(noreplace) /etc/joe/*
%{_mandir}/man1/*
%{_mandir}/ru/man1/*
%{_datadir}/%{name}
%exclude %{_datadir}/applications/j*desktop

%changelog
%autochangelog
