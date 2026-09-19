%global source0_hash 2d193a091aa95bcebb58b2c33e6b979baca0248f5397a2b6dcae68f4ceb3bec6

Summary:          List packages that have no dependencies (like deborphan)
Name:             rpmorphan
Version:          1.19
Release:          9%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later

BuildArch:        noarch

URL:              http://rpmorphan.sourceforge.net

# Note upstream have the habit of releasing updated tarballs which
# have the same version number (happened with 1.12).
Source0:          http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:    make
BuildRequires:    /usr/bin/pod2man
BuildRequires:    perl-generators

Requires:         perl(Curses::UI)
Requires:         logrotate
Requires:         perl-Tk

%description
rpmorphan finds "orphaned"[1] packages on your system. It determines
which packages have no other packages depending on their installation,
and shows you a list of these packages.  It intends to be clone of
deborphan Debian tools for rpm packages.

It will try to help you to remove unused packages, for example:
* after a distribution upgrade
* when you want to suppress packages after some tests

Several tools are also provided :
* rpmusage - display rpm packages last use date
* rpmdep - display the full dependency of an installed rpm package
* rpmduplicates - find programs with several version installed

Yum offers a program called 'package-cleanup' which you can use to
carry out similar tasks.

[1] Note that orphan is used in the sense of Debian's deborphan, and
is NOT the same as Fedora orphaned packages which are packages that
have no current maintainer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i -e "s|/usr/lib|/usr/share|g" rpm*

%build
# Nothing needed here.

%install
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -m 0644 rpmorphan.logrotate $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/rpmorphan
mv $RPM_BUILD_ROOT/usr/lib/%{name} $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%doc rpmorphan.lsm Authors COPYING Changelog NEWS Todo Readme rpmorphanrc.sample
%{_bindir}/grpmorphan
%{_bindir}/rpmextra
%{_bindir}/rpmextra.pl
%{_bindir}/rpmorphan.pl
%{_bindir}/rpmorphan
%{_bindir}/rpmusage.pl
%{_bindir}/rpmusage
%{_bindir}/rpmdep.pl
%{_bindir}/rpmdep
%{_bindir}/rpmduplicates.pl
%{_bindir}/rpmduplicates
%ghost %config(noreplace) %{_localstatedir}/log/rpmorphan.log
%dir %{_localstatedir}/lib/rpmorphan
%attr(644, root, root)%{_localstatedir}/lib/rpmorphan/keep
%config(noreplace) %{_sysconfdir}/logrotate.d/rpmorphan
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/rpmorphanrc
%{_mandir}/man1/rpmextra.1*
%{_mandir}/man1/rpmorphan.1*
%{_mandir}/man1/rpmusage.1*
%{_mandir}/man1/rpmdep.1*
%{_mandir}/man1/rpmduplicates.1*

%changelog
%autochangelog
