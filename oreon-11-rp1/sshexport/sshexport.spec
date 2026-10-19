%global source0_hash db42727d7b7f725a2ef2109e7970ec061e1f9d0af1a1a427cec88543424526f3
%global oldpkg ssh-installkeys
%global python_prg %{__python2}
%global python_ver python2
Name:           sshexport
Version:        2.4
Release:        16%{?dist}
Summary:        Install your SSH keys on remote sites
License:        LicenseRef-Callaway-BSD AND ISC
URL:            http://www.catb.org/~esr/%{name}
Source0:        http://www.catb.org/~esr/%{name}/%{name}-%{version}.tar.gz
Patch0000:      %{name}-2.4-fix_manpage.patch
BuildArch:      noarch
Obsoletes:      %{oldpkg} < 1.10
Provides:       %{oldpkg} = %{version}-%{release}
Provides:       bundled(%{python_ver}-pexpect) = 2.3
# oreon:deps
BuildRequires:  make
BuildRequires:  python2-devel
BuildRequires:  xmlto
# /oreon:deps
%description
This script tries to export SSH public keys to specified sites.
It will walk the user through generating key pairs if it doesn't
find any to export.  It handles all the fiddly details, like
remembering the SSH key file names, updating the authorized_keys
and making sure local and remote permissions are correct.
It tells you what it's doing if it has to change anything.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

# Remove possible prebuilt stuff.
rm -f %{name}.{1,html}

%build

%make_build %{name}.{1,html}
sed 's~^#!.*~#!%{python_prg}~1' < %{name} > %{name}.fix
touch -r %{name}{,.fix}
mv -f %{name}{.fix,}
%install
install -Dpm 0755 {,%{buildroot}%{_bindir}/}%{name}
install -Dpm 0644 {,%{buildroot}%{_mandir}/man1/}%{name}.1
ln -s %{name} %{buildroot}%{_bindir}/%{oldpkg}
ln -s %{name}.1 %{buildroot}%{_mandir}/man1/%{oldpkg}.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
