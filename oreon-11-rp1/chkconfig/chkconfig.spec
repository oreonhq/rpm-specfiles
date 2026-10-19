%global source0_hash c973a38d46d75ab2b411ab141e4c320a66dc4cc98832c3f2f6c5999531057861
Summary:        A system tool for maintaining the /etc/rc*.d hierarchy
Name: chkconfig
Version: 1.33
Release:        5%{?dist}
License: GPL-2.0-only
URL: https://github.com/fedora-sysv/chkconfig
Source0:        https://github.com/fedora-sysv/chkconfig/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch: 0001-Ignore-alternatives-that-are-binary-identical-to-exi.patch
%global merged_sbin %["%{_sbindir}" == "%{_bindir}"]
Conflicts: initscripts <= 5.30-1
Provides: /sbin/chkconfig
# oreon:deps
BuildRequires:  beakerlib
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  newt-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  popt-devel
# /oreon:deps
%description
Chkconfig is a basic system utility.  It updates and queries runlevel
information for system services.  Chkconfig manipulates the numerous
symbolic links in /etc/rc.d, to relieve system administrators of some
of the drudgery of manually editing the symbolic links.

%package -n ntsysv
Summary: A tool to set the stop/start of system services in a runlevel
Requires: chkconfig = %{version}-%{release}
%description -n ntsysv
Ntsysv provides a simple interface for setting which system services
are started or stopped in various runlevels (instead of directly
manipulating the numerous symbolic links in /etc/rc.d). Unless you
specify a runlevel or runlevels on the command line (see the man
page), ntsysv configures the current runlevel (5 if you're using X).

%package -n alternatives
Summary: A tool to maintain symbolic links determining default commands
%if %{merged_sbin}
Provides: /usr/sbin/alternatives
Provides: /usr/sbin/update-alternatives
Requires: filesystem(unmerged-sbin-symlinks)
%endif
%description -n alternatives
alternatives creates, removes, maintains and displays information about the
symbolic links comprising the alternatives system. It is possible for several
programs fulfilling the same or similar functions to be installed on a single
system at the same time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build RPM_OPT_FLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" MERGED_SBIN=%{merged_sbin}
%install
rm -rf $RPM_BUILD_ROOT
%make_install MANDIR=%{_mandir} SBINDIR=%{_sbindir}
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
ln -s rc.d/init.d $RPM_BUILD_ROOT/etc/init.d
for n in 0 1 2 3 4 5 6; do
    mkdir -p $RPM_BUILD_ROOT/etc/rc.d/rc${n}.d
    ln -s rc.d/rc${n}.d $RPM_BUILD_ROOT/etc/rc${n}.d
done
mkdir -p $RPM_BUILD_ROOT/etc/chkconfig.d
%find_lang %{name}
%oreon_autofiles ntsysv usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles alternatives usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ntsysv -f %{oreon_filedir}/ntsysv.list
%files -n alternatives -f %{oreon_filedir}/alternatives.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.33-5
- Prepare for Oreon 11 (RP1)
