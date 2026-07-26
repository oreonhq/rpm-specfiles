%global source0_hash 1acdf3924fdf6f0da7dec1b586e2780fc8f472552adecf3b0d9f529a01eb52a5

Summary: Enhanced backup plugin for J-Pilot
Name: jpilot-backup
Version: 0.60
Release: 43%{dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source: http://www.jlogday.com/code/jpilot-backup/%{name}-%{version}.tar.gz
Patch0: jpilot-backup-libdir.patch
Patch1: jpilot-backup-configure-c99.patch
URL: http://www.jlogday.com/code/jpilot-backup/
Requires: jpilot >= 0.99.2
BuildRequires:  gcc
BuildRequires: pilot-link-devel
BuildRequires: gtk2-devel
BuildRequires: gdbm-devel
BuildRequires: make

# pilot-link excludes s390 and s390s, as such I must also exclude those arches
ExcludeArch: s390 s390x

%description
Features include multiple archives, automatic backups at user-specified times,
and the ability to specify which databases to backup.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n %{name}-%{version} -q
%patch -P0 -p1 -b .libdir
%patch -P1 -p1 -b .c99

%build
%configure --libdir=/%{_lib}/jpilot/plugins --with-pilot-prefix=%{_prefix}

make %{?_smp_mflags}

%install
make prefix=$RPM_BUILD_ROOT%{_prefix} install

# manually remove the libtool archive
find %{buildroot} -type f -name "*.la" -delete

%files
%doc README README.NFS ChangeLog CREDITS TODO
%license COPYING
%{_libdir}/jpilot/plugins/libbackup.so

%changelog
%autochangelog
