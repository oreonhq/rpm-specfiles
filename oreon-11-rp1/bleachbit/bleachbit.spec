%global source0_hash 6d32db1200fd6e89f0fa822e01ce8eaac9749e84788970b0f562d77b271db629

# EPEL7 changes for Python and metainfodir
%if 0%{?rhel} && 0%{?rhel} < 8
%global __python %{__python3}
%global _metainfodir %{_datadir}/metainfo
%endif

Name:		bleachbit
Version:	4.6.0
Release:	8%{?dist}
Summary:	Remove sensitive data and free up disk space

License:	GPL-3.0-or-later
URL:		https://www.bleachbit.org/
Source:		https://github.com/bleachbit/bleachbit/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:		no_update.patch
# https://github.com/bleachbit/bleachbit/issues/950
Patch1:		disable_policykit.patch

BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libappstream-glib
BuildRequires:	make
BuildRequires:	python3-devel
%if 0%{?rhel}  &&  0%{?rhel} < 8
BuildRequires:	python3-rpm-macros
%endif
BuildRequires:	pkgconfig(systemd)

Requires:	gtk3
Requires:	python3-chardet
%if 0%{?rhel}  &&  0%{?rhel} < 8
Requires:	python36-gobject
%else
Requires:	python3-gobject
%endif

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

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

make -C po local
# Remove Windows-specific functionality.
%make_build delete_windows_files

%install
%make_install prefix=%{_prefix}

desktop-file-install --dir=%{buildroot}/%{_datadir}/applications/ org.bleachbit.BleachBit.desktop
install -Dp org.bleachbit.BleachBit.metainfo.xml %{buildroot}/%{_metainfodir}/

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.bleachbit.BleachBit.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.bleachbit.BleachBit.metainfo.xml

%files -f %{name}.lang
%doc README* doc
%license COPYING
%{_bindir}/bleachbit
%{_datadir}/applications/org.bleachbit.BleachBit.desktop
%{_datadir}/bleachbit
%{_datadir}/pixmaps/bleachbit.png
%{_metainfodir}/org.bleachbit.BleachBit.metainfo.xml

%changelog
%autochangelog
