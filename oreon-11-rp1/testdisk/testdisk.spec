%global source0_hash f8343be20cb4001c5d91a2e3bcd918398f00ae6d8310894a5a9f2feb813c283f

Summary:	Tool to check and undelete partition, PhotoRec recovers lost files
Summary(pl.UTF8):	Narzędzie sprawdzające i odzyskujące partycje
Summary(fr.UTF8):	Outil pour vérifier et restaurer des partitions
Summary(ru_RU.UTF8): Программа для проверки и восстановления разделов диска
Name:		testdisk
Version:	7.2
Release:	6%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
Source0:	https://www.cgsecurity.org/testdisk-%{version}.tar.bz2
URL:		https://www.cgsecurity.org/wiki/TestDisk
BuildRequires: make
BuildRequires:	desktop-file-utils
BuildRequires:	e2fsprogs-devel
BuildRequires:	libewf-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libuuid-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	ntfs-3g-devel
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qtbase-devel
BuildRequires:	zlib-devel
Obsoletes:	testdisk-doc < 6.12

%description
Tool to check and undelete partition. Works with FAT12, FAT16, FAT32,
NTFS, ext2, ext3, ext4, btrfs, BeFS, CramFS, HFS, JFS, Linux Raid, Linux
Swap, LVM, LVM2, NSS, ReiserFS, UFS, XFS.
PhotoRec is a signature based file recovery utility. It handles more than
440 file formats including JPG, MSOffice, OpenOffice documents.

%description -l pl.UTF8
Narzędzie sprawdzające i odzyskujące partycje. Pracuje z partycjami:
FAT12, FAT16, FAT32, NTFS, ext2, ext3, ext4, btrfs, BeFS, CramFS, HFS, JFS,
Linux Raid, Linux Swap, LVM, LVM2, NSS, ReiserFS, UFS, XFS.
PhotoRec is a signature based file recovery utility. It handles more than
440 file formats including JPG, MSOffice, OpenOffice documents.

%description -l fr.UTF8
TestDisk vérifie et récupère les partitions. Fonctionne avec
FAT12, FAT16, FAT32, NTFS, ext2, ext3, ext4, btrfs, BeFS, CramFS, HFS, JFS,
Linux Raid, Linux Swap, LVM, LVM2, NSS, ReiserFS, UFS, XFS.
PhotoRec utilise un mécanisme de signature pour récupérer des fichiers
perdus. Il reconnait plus de 440 formats de fichiers dont les JPEG, les
documents MSOffice ou OpenOffice.

%description -l ru_RU.UTF8
Программа для проверки и восстановления разделов диска.
Поддерживает следующие типы разделов:
FAT12, FAT16, FAT32, NTFS, ext2, ext3, ext4, btrfs, BeFS, CramFS, HFS, JFS,
Linux Raid, Linux Swap, LVM, LVM2, NSS, ReiserFS, UFS, XFS.
PhotoRec is a signature based file recovery utility. It handles more than
440 file formats including JPG, MSOffice, OpenOffice documents.

%package -n qphotorec
Summary:	Signature based file carver. Recover lost files

%description -n qphotorec
QPhotoRec is a Qt version of PhotoRec. It is a signature based file recovery
utility. It handles more than 440 file formats including JPG, MSOffice,
OpenOffice documents.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
%make_build

%install
%make_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/qphotorec.desktop

%if 0%{?rhel} && 0%{?rhel} < 8
%post -n qphotorec
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun -n qphotorec
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans -n qphotorec
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files
%doc AUTHORS ChangeLog NEWS README.md THANKS
%license COPYING
%doc documentation.html
%{_bindir}/fidentify
%{_bindir}/photorec
%{_bindir}/testdisk
%{_mandir}/man8/fidentify.8*
%{_mandir}/man8/photorec.8*
%{_mandir}/man8/testdisk.8*
%{_mandir}/zh_CN/man8/fidentify.8*
%{_mandir}/zh_CN/man8/photorec.8*
%{_mandir}/zh_CN/man8/testdisk.8*

%files -n qphotorec
%{_bindir}/qphotorec
%{_mandir}/man8/qphotorec.8*
%{_mandir}/zh_CN/man8/qphotorec.8*
%{_datadir}/applications/qphotorec.desktop
%{_datadir}/icons/hicolor/48x48/apps/qphotorec.png
%{_datadir}/icons/hicolor/scalable/apps/qphotorec.svg

%changelog
%autochangelog
