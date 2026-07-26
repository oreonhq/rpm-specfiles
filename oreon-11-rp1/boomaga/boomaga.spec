%global source0_hash e4584f88c66faac9f0b915afbcca7bcdbf2a2a5c910e96c26141ddf5e9982c6d

# https://github.com/Boomaga/boomaga/commit/7f7ad4754b20a1027c5095b660c5229353b64c8d
%global commit0 7f7ad4754b20a1027c5095b660c5229353b64c8d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global modulename %{name}
%global __cmake_in_source_build 1

Name:           boomaga
Version:        3.3.0
Release:        28.git%{shortcommit0}%{?dist}
Summary:        A virtual printer for viewing a document before printing

# Automatically converted from old format: GPLv2 and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-LGPLv2+
URL:            https://www.boomaga.org
Source0:        https://github.com/Boomaga/%{name}/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  poppler-devel
BuildRequires:  poppler-cpp-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  snappy-devel
Requires:       cups
Requires:       shared-mime-info
Requires:       hicolor-icon-theme

%description
Boomaga (BOOklet MAnager) is a virtual printer for viewing a document
before printing it out using the physical printer.
The program is very simple to work with.
Running any program, click "print" and select "Boomaga" to see in several
seconds (CUPS takes some time to respond) the Boomaga window open.
If you print out one more document,
it gets added to the previous one, and you can also print them out as one.
Regardless of whether your printer supports duplex printing or not,
you would be able to easily print on both sides of the sheet.
If your printer does not support duplex printing,
point this out in the settings, and Booklet would ask you to turn
over the pages half way through printing your document.

The program can also help you get your documents prepared a bit
before printing. At this stage Boomaga makes it possible to:

 * Paste several documents together.
 * Print several pages on one sheet.
 * 1, 2, 4, 8 pages per sheet
 * Booklet. Folding the sheets in two, you'll get a book.

%package selinux
Summary:        SELinux policy module supporting boomaga
BuildRequires:  checkpolicy, selinux-policy-devel, hardlink
Requires:       %{name} = %{version}-%{release}
Requires(post): policycoreutils, %{name}
Requires(preun): policycoreutils, %{name}
Requires(postun): policycoreutils

%description selinux
SELinux policy module supporting boomaga

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit0}

# delete unused directories and files
find -name .gitignore -type f -or -name .travis.yml -type f | xargs rm -rfv

sed -i -e 's|find "/usr/local/lib" "/usr/lib" -name|find "/usr/local/lib" "%{_libdir}" -name|' scripts/testBackend.sh

%build
# TODO: Please submit an issue to upstream (rhbz#2380483)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
    -DUSE_QT5=Yes \
    -DCUPS_BACKEND_DIR=%{_cups_serverbin}/backend \
    -DCUPS_FILTER_DIR=%{_cups_serverbin}/filter   \
    -DSELINUX=Yes                                 \
    .
# disable parallel build, is not possible
# make_build
%cmake_build -j1

%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/%{name}/scripts
install -m 755 scripts/installPrinter.sh %{buildroot}%{_datadir}/%{name}/scripts/
chmod +x %{buildroot}%{_datadir}/%{name}/scripts/installPrinter.sh
mkdir -p %{buildroot}/%{_localstatedir}/cache/%{name}

%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%pre
# Start cups if is stopped
if [ "$(systemctl is-active cups.service)" != "active" ]; then
    /bin/systemctl start cups
    sleep 2
fi

%post
# Install the printer to cups backends
if [ $1 = 1 ]; then
    sh %{_datadir}/%{name}/scripts/installPrinter.sh
fi

%preun
# Uninstall the printer
if [ $1 = 0 ] ; then
    lpadmin -x "Boomaga"
fi

%post selinux
for selinuxvariant in %{selinux_variants}
do
   /usr/sbin/semodule -s ${selinuxvariant} -i \
   %{_datadir}/selinux/${selinuxvariant}/%{modulename}.pp &> /dev/null || :
   /sbin/fixfiles -R %{name} restore
done
/sbin/restorecon %{_localstatedir}/cache/%{name} || :

%preun selinux 
if [ "$1" -lt "1" ]; then # Final removal
   /usr/sbin/semodule -r %{name} 2>/dev/null || :
   /sbin/fixfiles -R %{name} restore
fi

%postun selinux
if [ $1 -eq 0 ] ; then
  for selinuxvariant in %{selinux_variants}
  do
     /usr/sbin/semodule -s ${selinuxvariant} -r %{modulename} &> /dev/null || :
  done
  [ -d %{_localstatedir}/cache/%{name} ]  && \
    /sbin/restorecon -R %{_localstatedir}/cache/%{name} &> /dev/null || :
fi

%files -f %{name}.lang
%doc README.md
%license COPYING GPL LGPL
%{_bindir}/%{name}

%{_cups_serverbin}/backend/%{name}
%dir %{_localstatedir}/cache/%{name}

%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.%{name}.service

%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml

%dir %{_datadir}/ppd/%{name}
%{_datadir}/ppd/%{name}/%{name}.ppd

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/scripts
%dir %{_datadir}/%{name}/translations/
%{_datadir}/%{name}/scripts/installPrinter.sh
%{_mandir}/man1/%{name}.1.gz

%files selinux
#doc SELinux/*
%{_datadir}/selinux/*/%{modulename}.pp

%changelog
%autochangelog
