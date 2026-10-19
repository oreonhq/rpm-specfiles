%global source0_hash none
Summary:        A set of system configuration and setup files
Name: setup
Version: 2.15.0
Release:        1%{?dist}
License: LicenseRef-Fedora-Public-Domain
URL: https://src.fedoraproject.org/rpms/setup
Source0001: aliases
Source0002: bashrc
Source0003: csh.cshrc
Source0004: csh.login
Source0005: ethertypes
Source0006: filesystems
Source0007: host.conf
Source0008: hosts
Source0009: inputrc
Source0010: networks
Source0011: printcap
Source0012: profile
Source0013: protocols
Source0014: services
Source0015: shells
Source0021: lang.csh
Source0022: lang.sh
Source0031: COPYING
Source0032: uidgid
Source0033: setup.sysusers.conf
Source0034: uidgidlint
Source0035: serviceslint
BuildArch: noarch
Requires: system-release
# oreon:deps
BuildRequires:  /usr/bin/systemd-sysusers
BuildRequires:  bash
BuildRequires:  perl-interpreter
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcsh
# /oreon:deps
%description
The setup package contains a set of important system configuration and
setup files, such as passwd, group, and profile.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
mkdir -p etc/profile.d
cp %{lua: for i=1,15 do print(sources[i]..' ') end} etc/
cp %SOURCE21 %SOURCE22 etc/profile.d/
touch etc/{exports,motd,subgid,subuid,environment,fstab}

mkdir -p docs
cp %SOURCE31 %SOURCE32 docs/

%build

systemd-sysusers --root=./ %SOURCE33
chmod 0400 ./etc/{shadow,gshadow}
%check

bash -n etc/bashrc
bash -n etc/profile
tcsh -f etc/csh.cshrc
tcsh -f etc/csh.login
bash %SOURCE34 docs/uidgid
(cd etc && perl %SOURCE35 ./services)
%install
mkdir -p %{buildroot}/etc
cp -ar etc/* %{buildroot}/etc/
install -D -m0644 %SOURCE33 %{buildroot}%{_sysusersdir}/setup.conf
mkdir -p %{buildroot}/var/log
touch %{buildroot}/etc/environment
touch %{buildroot}/etc/fstab
echo "#Add any required envvar overrides to this file, it is sourced from /etc/profile" >%{buildroot}/etc/profile.d/sh.local
echo "#Add any required envvar overrides to this file, it is sourced from /etc/csh.login" >%{buildroot}/etc/profile.d/csh.local
mkdir -p %{buildroot}/etc/motd.d
mkdir -p %{buildroot}/run/motd.d
mkdir -p %{buildroot}/usr/lib/motd.d
touch %{buildroot}/usr/lib/motd
mkdir -p %{buildroot}%{_tmpfilesdir}
echo "f /run/motd 0644 root root -" >%{buildroot}%{_tmpfilesdir}/%{name}.conf
echo "d /run/motd.d 0755 root root -" >>%{buildroot}%{_tmpfilesdir}/%{name}.conf
chmod 0644 %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}/etc/dnf/protected.d/
echo "setup" >%{buildroot}/etc/dnf/protected.d/setup.conf
mkdir -p %{buildroot}/usr/share/dnf5/libdnf.conf.d/
cat >%{buildroot}/usr/share/dnf5/libdnf.conf.d/protect-setup.conf <<EOF
[main]
protected_packages = setup
EOF
%oreon_autofiles main

%post -p <lua>

-- Throw away useless and dangerous update stuff until rpm will be able to
-- handle it.  See: http://rpm.org/ticket/6
for i, name in ipairs({"passwd", "shadow", "group", "gshadow"}) do
   os.remove("/etc/"..name..".rpmnew")
end
-- Use rpm.spawn() if available (in >= 4.20) but fallback to forking if not.
--
-- Initialize or update /etc/alias.db from /etc/aliases for sendmail, etc.
if posix.access("/usr/bin/newaliases", "x") then
  if rpm.spawn ~= nil then
    rpm.spawn({'/usr/bin/newaliases'}, {stdout='/dev/null'})
  else
    local pid = posix.fork()
    if pid == 0 then
      posix.redirect2null(1)
      posix.exec("/usr/bin/newaliases")
    elseif pid > 0 then
      posix.wait(pid)
    end
  end
end
-- Ensure pre-allocated tmpfiles are created immediately on upgrades.
if posix.access("/usr/bin/systemd-tmpfiles", "x") then
  if rpm.spawn ~= nil then
    rpm.spawn({"/usr/bin/systemd-tmpfiles", "--create"}, {stderr='/dev/null'})
  else
    local pid = posix.fork()
    if pid == 0 then
      posix.redirect2null(2)
      posix.exec("/usr/bin/systemd-tmpfiles", "--create")
    elseif pid > 0 then
      posix.wait(pid)
    end
  end
end
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
