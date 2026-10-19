%global source0_hash 8f6af8046ee6b0293b26389d08cb6950c7f7ddfffc1f74eefcb087bd49d44f62
Name:           rsnapshot
Version:        1.5.1
Release:        1%{?dist}
Summary:        Local and remote filesystem snapshot utility
License:        GPL-2.0-or-later
URL:            https://rsnapshot.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       openssh-clients
Requires:       rsync
# oreon:deps
BuildRequires:  /usr/bin/pod2man
BuildRequires:  lvm2
BuildRequires:  make
BuildRequires:  openssh-clients
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  rsync
# /oreon:deps
%description
This is a remote backup program that uses rsync to take backup snapshots of
filesystems.  It uses hard links to save space on disk.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure \
  --with-perl="%{__perl}" \
  --with-rsync="%{_bindir}/rsync" \
  --with-cp="%{__cp}" \
  --with-rm="%{__rm}" \
  --with-ssh="%{_bindir}/ssh" \
  --with-logger="%{_bindir}/logger" \
  --with-du="%{_bindir}/du"
%install
%make_install
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf{.default,}
touch -c -r %{name}.conf.default{.in,} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf
find utils/ -type f -print0 | xargs -r0 chmod 644
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
