%global source0_hash 0261c5e90b98b6138cd23dadecbc7bc6e2830235145ed2740290e1f35672d843

Name: mtx
Version: 1.3.12
Release: 37%{?dist}
Summary: SCSI media changer control program
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
Source0:        http://downloads.sourceforge.net/mtx/mtx-1.3.12.tar.gz
# http://mtx.opensource-sw.net/bugs/view.php?id=9
Patch0: %{name}-1.3.12-destdir.patch
# http://mtx.opensource-sw.net/bugs/view.php?id=13
# https://bugzilla.redhat.com/show_bug.cgi?id=538403
Patch1: %{name}-1.3.12-argc.patch
# update for GCC 15 / C23
Patch2: %{name}-1.3.12-bool.patch
#URL: http://mtx.sourceforge.net/
URL: https://github.com/mtx-org/mtx
BuildRequires: make
BuildRequires: gcc


%description
The MTX program controls the robotic mechanism in autoloaders and tape
libraries such as the HP SureStore DAT 40x6, Exabyte EZ-17, and
Exabyte 220. This program is also reported to work with a variety of
other tape libraries and autochangers from ADIC, Tandberg/Overland,
Breece Hill, HP, and Seagate.

If you have a backup tape device capable of handling more than one
tape at a time, you should install MTX.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%patch -P0 -p2 -b .destdir
%patch -P1 -p2 -b .argc
%patch -P2 -p1 -b .bool

# remove exec permission
chmod a-x contrib/config_sgen_solaris.sh contrib/mtx-changer


%build
%configure
%make_build


%install
%make_install


%files
%doc CHANGES COMPATABILITY contrib FAQ LICENSE
%doc mtx.doc mtxl.README.html README TODO
%{_mandir}/man1/*
%{_sbindir}/*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.12-37
- Import
