%global source0_hash 8f6af8046ee6b0293b26389d08cb6950c7f7ddfffc1f74eefcb087bd49d44f62

Name:           rsnapshot
Version:        1.5.1
Release:        3%{?dist}
Summary:        Local and remote filesystem snapshot utility
License:        GPL-2.0-or-later
URL:            https://rsnapshot.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  lvm2
BuildRequires:  make
BuildRequires:  openssh-clients
BuildRequires:  perl-generators
BuildRequires:  rsync
BuildRequires:  %{_bindir}/pod2man

# For running %%check
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
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)

Requires:       openssh-clients
Requires:       rsync

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

# Rename the installed .default config file to a usable name
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf{.default,}

# Reset timestamp of .default config file to pre-%%configure
touch -c -r %{name}.conf.default{.in,} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

# Change the perms on the utils/ files so rpm doesn't pick up their dependencies
find utils/ -type f -print0 | xargs -r0 chmod 644

%check
%{__make} test

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%doc %{name}.conf.default utils/
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/%{name}-diff
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-diff.1*

%changelog
%autochangelog
