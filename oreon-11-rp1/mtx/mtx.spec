%global source0_hash 0261c5e90b98b6138cd23dadecbc7bc6e2830235145ed2740290e1f35672d843
Name: mtx
Version: 1.3.12
Release:        1%{?dist}
Summary:        SCSI media changer control program
License: GPL-2.0-only
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: %{name}-1.3.12-destdir.patch
Patch1: %{name}-1.3.12-argc.patch
Patch2: %{name}-1.3.12-bool.patch
URL: https://github.com/mtx-org/mtx
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The MTX program controls the robotic mechanism in autoloaders and tape
libraries such as the HP SureStore DAT 40x6, Exabyte EZ-17, and
Exabyte 220. This program is also reported to work with a variety of
other tape libraries and autochangers from ADIC, Tandberg/Overland,
Breece Hill, HP, and Seagate.

If you have a backup tape device capable of handling more than one
tape at a time, you should install MTX.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.12-37
- Import
