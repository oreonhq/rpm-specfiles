%global source0_hash e4584f88c66faac9f0b915afbcca7bcdbf2a2a5c910e96c26141ddf5e9982c6d
%global commit0 7f7ad4754b20a1027c5095b660c5229353b64c8d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global modulename %{name}
%global __cmake_in_source_build 1
Name:           boomaga
Version:        3.3.0
Release:        1%{?dist}
Summary:        A virtual printer for viewing a document before printing
License:        GPL-2.0-only AND LicenseRef-Callaway-LGPLv2+
URL:            https://www.boomaga.org
Source0:        https://github.com/Boomaga/%{name}/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Requires:       cups
Requires:       shared-mime-info
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  checkpolicy
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  hardlink
BuildRequires:  poppler-cpp-devel
BuildRequires:  poppler-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  selinux-policy-devel
BuildRequires:  snappy-devel
# /oreon:deps
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

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
    -DUSE_QT5=Yes \
    -DCUPS_BACKEND_DIR=%{_cups_serverbin}/backend \
    -DCUPS_FILTER_DIR=%{_cups_serverbin}/filter   \
    -DSELINUX=Yes                                 \
    .
%cmake_build -j1
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/%{name}/scripts
install -m 755 scripts/installPrinter.sh %{buildroot}%{_datadir}/%{name}/scripts/
chmod +x %{buildroot}%{_datadir}/%{name}/scripts/installPrinter.sh
mkdir -p %{buildroot}/%{_localstatedir}/cache/%{name}
%find_lang %{name} --with-qt
%oreon_autofiles boomaga-selinux usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%pre

if [ "$(systemctl is-active cups.service)" != "active" ]; then
    /bin/systemctl start cups
    sleep 2
fi
%post

if [ $1 = 1 ]; then
    sh %{_datadir}/%{name}/scripts/installPrinter.sh
fi
%preun

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
%files -f %{oreon_filedir}/main.list
%files -n boomaga-selinux -f %{oreon_filedir}/boomaga-selinux.list

%changelog

%autochangelog
