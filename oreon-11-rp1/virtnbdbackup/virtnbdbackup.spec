%global source0_hash 52338a8192b8b6350338b053008ce6e3e9ae8f766044f59f91c426abb62320c9

Name:           virtnbdbackup
Version:        2.46
Release:        1%{?dist}
Summary:        Backup utility for libvirt
License:        GPL-3.0-or-later
URL:            https://github.com/abbbi/%{name}
Source0:        https://github.com/abbbi/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils, sed
BuildRequires:  python3-devel
BuildRequires:  python3-libnbd >= 1.5.5
Requires:       nbdkit-python-plugin
Requires:       nbdkit-server
Requires:       openssh-clients
Requires:       python3-libnbd >= 1.5.5
Requires:       qemu-img

%description
Backup utility for libvirt, using the latest changed block tracking features.
Create online, thin provisioned full and incremental or differential backups
of your kvm/qemu virtual machines.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# move nbdkit plugin from bindir (also see install)
sed -i 's@{installDir}\(/{pluginFileName}\)@%{_datadir}\1@' libvirtnbdbackup/map/requirements.py

# remove unneeeded shebangs from modules
find libvirtnbdbackup -type f -name \*.py -exec sed -i '1{/^#!/d}' '{}' +

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files libvirtnbdbackup

mkdir %{buildroot}%{_datadir}
mv %{buildroot}%{_bindir}/virtnbd-nbdkit-plugin %{buildroot}%{_datadir}
chmod -x %{buildroot}%{_datadir}/virtnbd-nbdkit-plugin

mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 man/*.1 %{buildroot}%{_mandir}/man1

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.md Changelog
%license LICENSE
%{_datadir}/virtnbd*
%{_bindir}/virtnbd*
%{_mandir}/man1/virtnbd*

%changelog
%autochangelog
