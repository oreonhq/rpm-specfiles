Summary: A utility for creating TTY dialog boxes
Name: dialog
%global dialogsubversion 20250116
Version: 1.3
Release: 57.%{dialogsubversion}%{?dist}
License: LGPL-2.1-only
URL: https://invisible-island.net/dialog/dialog.html
Source0: https://invisible-mirror.net/archives/dialog/dialog-%{version}-%{dialogsubversion}.tgz
Source1: https://invisible-mirror.net/archives/dialog/dialog-%{version}-%{dialogsubversion}.tgz.asc
Source2: https://invisible-island.net/public/dickey@invisible-island.net-rsa3072.asc
BuildRequires: ncurses-devel gcc gettext findutils libtool gnupg2
BuildRequires: make
Patch2: dialog-multilib.patch
Patch3: dialog-libs.patch

%description
Dialog is a utility that allows you to show dialog boxes (containing
questions or messages) in TTY (text mode) interfaces.  Dialog is called
from within a shell script.  The following dialog boxes are implemented:
yes/no, menu, input, message, text, info, checklist, radiolist, and
gauge.  

Install dialog if you would like to create TTY dialog boxes.

%package devel 
Summary: Development files for building applications with the dialog library
Requires: %{name}%{?_isa} = %{version}-%{release} ncurses-devel

%description devel
Dialog is a utility that allows you to show dialog boxes (containing
questions or messages) in TTY (text mode) interfaces. This package 
contains the files needed for developing applications, which use the 
dialog library.

%prep
%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%setup -q -n dialog-%{version}-%{dialogsubversion}
%patch -P2 -p1 -b .multilib
%patch -P3 -p1 -b .libs

%build
%configure \
	--enable-nls \
	--enable-pc-files \
	--with-libtool \
	--with-libtool-opts="$(for opt in %{?_hardened_ldflags}; do \
				echo -n -Xcompiler $opt ''; done)" \
	--with-ncursesw \
	--includedir=%{_includedir}/dialog
make %{?_smp_mflags}

%install
# prepare packaged samples
rm -rf _samples
mkdir _samples
cp -a samples _samples
rm -rf _samples/samples/install
find _samples -type f -print0 | xargs -0 chmod a-x

make install DESTDIR=$RPM_BUILD_ROOT

chmod 755 $RPM_BUILD_ROOT%{_libdir}/libdialog.so.*.*.*
rm -f $RPM_BUILD_ROOT%{_libdir}/libdialog.{,l}a

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc COPYING dialog.lsm README _samples/samples
%{_bindir}/dialog
%{_libdir}/libdialog.so.15*
%{_mandir}/man1/dialog.*

%files devel
%{_bindir}/dialog-config
%{_includedir}/dialog
%{_libdir}/libdialog.so
%{_libdir}/pkgconfig/dialog.pc
%{_mandir}/man3/dialog.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3-57.
- Prepare for Oreon 11 (RP1)
