%global source0_hash 5af7cec3ed77b38e2e9ef91201e69d75100664116669b04a053dfd788d996f12
Name:		bleachbit
Version:	6.0.4
Release:        1%{?dist}
Summary:        Remove sensitive data and free up disk space
License:	GPL-3.0-or-later
URL:		https://www.bleachbit.org/
Source0:        https://github.com/bleachbit/bleachbit/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		no_update.patch
Patch1:		disable_policykit.patch
BuildArch:	noarch
Requires:	gtk3
Requires:	python3-chardet
Requires:	python3-gobject
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-bleachbit = %{version}-%{release}
# /oreon:deps
%description
Delete traces of your computer activity and other junk files to free
disk space and maintain privacy.

With BleachBit, you can free cache, delete cookies, clear Internet
history, shred temporary files, delete logs, and discard junk you didn't
know was there. Designed for Linux and Windows systems, it wipes clean
thousands of applications including Firefox, Internet Explorer, Adobe
Flash, Google Chrome, Opera, Safari, and many more. Beyond simply
deleting files, BleachBit includes advanced features such as shredding
files to prevent recovery, wiping free disk space to hide traces of
files deleted by other applications, and cleaning Web browser profiles
to make them run faster.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Disable update notifications, since package will be updated by DNF or Packagekit.
sed 's/online_update_notification_enabled = True/online_update_notification_enabled = False/g'  --in-place ./bleachbit/__init__.py
# These get installed to %%{_datadir} as non-executable files, and so shouldn't need a shebang at all.
find ./bleachbit/  -type f  -iname '*.py'  -exec sed --regexp-extended '1s|^#! ?/.+$||g' --in-place '{}' +
# Replace any remaining env shebangs, or shebangs calling unversioned or unnecessarily specifically versioned Python, with plain python3.
find ./  -type f  -iname '*.py'  -exec sed --regexp-extended '1s|^#! ?/usr/bin/env python3?$|#!%{_bindir}/python3|g' --in-place '{}' +
find ./  -type f  -iname '*.py'  -exec sed --regexp-extended '1s|^#! ?/usr/bin/python[[:digit:][:punct:]]*$|#!%{_bindir}/python3|g' --in-place '{}' +

# SafeConfigParser class removed from the configparser module in Python 3.12
sed -i -e "s|SafeConfigParser|ConfigParser|" bleachbit/__init__.py

%build

%pyproject_wheel
make -C po local
%make_build delete_windows_files
%install
%make_install prefix=%{_prefix}
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications/ org.bleachbit.BleachBit.desktop
install -Dp org.bleachbit.BleachBit.metainfo.xml %{buildroot}/%{_metainfodir}/
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.bleachbit.BleachBit.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.bleachbit.BleachBit.metainfo.xml
%files

%changelog

%autochangelog
