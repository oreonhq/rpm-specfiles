%global source0_hash 2abed61bc6d2b9ec498973c0440b8b804b7a72d7144069b5a9209b2ad693a282

Summary:       An fdisk-like partitioning tool for GPT disks
Name:          gdisk
Version:       1.0.10
Release:       5%{?dist}
License:       GPL-2.0-only
URL:           http://www.rodsbooks.com/gdisk/
Source0:       http://downloads.sourceforge.net/gptfdisk/gptfdisk-%{version}.tar.gz
BuildRequires: gcc-c++
BuildRequires: libuuid-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: popt-devel

%description
An fdisk-like partitioning tool for GPT disks. GPT fdisk features a
command-line interface, fairly direct manipulation of partition table
structures, recovery tools to help you deal with corrupt partition
tables, and the ability to convert MBR disks to GPT format.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n gptfdisk-%{version}

%build
make CXXFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64" LDFLAGS="%{build_ldflags}"

%install
for f in gdisk sgdisk cgdisk fixparts ; do 
    install -D -p -m 0755 $f %{buildroot}%{_sbindir}/$f
    install -D -p -m 0644 $f.8 %{buildroot}%{_mandir}/man8/$f.8
done

%check
make test

%files
%license COPYING
%doc NEWS README
%{_sbindir}/gdisk
%{_sbindir}/cgdisk
%{_sbindir}/sgdisk
%{_sbindir}/fixparts
%{_mandir}/man8/gdisk.8*
%{_mandir}/man8/cgdisk.8*
%{_mandir}/man8/sgdisk.8*
%{_mandir}/man8/fixparts.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.10-5
- Prepare for Oreon 11 (RP1)
