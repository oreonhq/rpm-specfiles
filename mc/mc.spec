# NOTE: disabled sftp (needs to be ported to use libssh instead of libssh2)
%bcond gpm %[!(0%{?rhel} >= 10)]
%bcond slang 1

Summary:	User-friendly text console file manager and visual shell
Name:		mc
Epoch:		1
Version: 	4.8.33
Release:	3%{?dist}
License:	GPL-3.0-or-later
URL:		https://midnight-commander.org/
Source:		http://ftp.midnight-commander.org/mc-%{version}.tar.xz
Patch:		%{name}-spec.syntax.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	gettext-devel
%if %{with gpm}
BuildRequires:	gpm-devel
%endif
BuildRequires:	groff-base
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gmodule-2.0)	>= 2.30
#BuildRequires:	pkgconfig(libssh2)	>= 1.2.8
BuildRequires:	%[%{?with_slang}?"pkgconfig(slang) >= 2.0":"ncurses-devel"]
Suggests:	mc-python

%description
Midnight Commander is a visual shell much like a file manager, only with
many more features. It is a text mode application, but it also includes
mouse support. Midnight Commander's best features are its ability to FTP,
view tar and zip files, and to poke into RPMs for specific files.

%package python
Summary:	Midnight Commander s3+ and UC1541 EXTFS backend scripts
BuildArch:	noarch
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python3-boto

%description python
Midnight Commander s3+ and UC1541 EXTFS backend scripts.

%prep
%autosetup -p1

%build
%__sed -i "s,PREV_MC_VERSION=\"unknown\",PREV_MC_VERSION=\"%{version}\"," version.sh
%configure \
	PYTHON=%__python3 \
	--disable-rpath \
	--disable-vfs-sftp \
	--enable-charset \
	--enable-largefile \
	--enable-vfs-cpio \
	--enable-vfs-extfs \
	--enable-vfs-shell \
	--enable-vfs-ftp \
	--enable-vfs-sfs \
	--enable-vfs-tar \
	--with%{!?with_gpm:out}-gpm-mouse \
	--with-screen=%[%{?with_slang}?"slang":"ncurses"] \
	--with-x \
	%{nil}
%make_build

%install
%make_install

%__install contrib/mc.{sh,csh} -Dt %{buildroot}%{_sysconfdir}/profile.d

%find_lang %{name} --with-man

%files -f %{name}.lang
%license doc/COPYING
%doc doc/FAQ doc/NEWS doc/README
/etc/profile.d/*
%dir %{_sysconfdir}/mc
%config(noreplace) %{_sysconfdir}/mc/*
%{_bindir}/*
%dir %{_libexecdir}/mc
%attr(755,root,root) %{_libexecdir}/mc/cons.saver
%{_libexecdir}/mc/mc*
%{_libexecdir}/mc/extfs.d
%{_libexecdir}/mc/ext.d
%{_libexecdir}/mc/shell
%{_datadir}/mc
%{_mandir}/man1/*
%exclude %{_libexecdir}/mc/extfs.d/{s3+,uc1541}

%files python
%{_libexecdir}/mc/extfs.d/{s3+,uc1541}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.8.33-3
- Prepare for Oreon 11 (RP1)
