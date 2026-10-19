%global source0_hash none
Name:           kernel-srpm-macros
Version:        1.0
Release:        1%{?dist}
Summary:        RPM macros that list arches the full kernel is built on
License:        MIT
URL:            https://src.fedoraproject.org/rpms/kernel-srpm-macros
BuildArch:      noarch
Conflicts:      redhat-rpm-config < 205
Conflicts:      kernel-rpm-macros < 205
Source0:        macros.kernel-srpm
Source1:        macros.kmp
Source100:      find-provides.ksyms
Source101:      find-requires.ksyms
Source102:      firmware.prov
Source103:      modalias.prov
Source104:      provided_ksyms.attr
Source105:      required_ksyms.attr
Source106:      modalias.attr
Source200:      kmod.attr
Source300:      kmodtool
Source301:      rpmsort
Source302:      symset-table
Source400: kabi.attr
Source401: kabi.sh
Source500: brp-kmod-set-exec-bit
Source501: brp-kmod-restore-perms
%global rrcdir /usr/lib/rpm/redhat
# oreon:deps

# /oreon:deps
%description
This packages contains the rpm macro that list what arches
the full kernel is built on.
The variable to use is kernel_arches.

%package -n kernel-rpm-macros
Version: 205
Summary: Macros and scripts for building kernel module packages
License:        MIT AND GPL-2.0-or-later
Requires: redhat-rpm-config >= 205
Requires: %{_bindir}/envsubst
Requires: %{_bindir}/xz
Requires: %{_bindir}/find
Requires: %{_bindir}/sed
Requires: %{_bindir}/awk
Requires: %{_bindir}/grep
Requires: %{_bindir}/nm
Requires: %{_bindir}/objdump
Requires: %{_bindir}/readelf
Requires: %{_sbindir}/modinfo
Requires: %{_sbindir}/modprobe
%description -n kernel-rpm-macros
Macros and scripts for building kernel module packages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# Not strictly necessary but allows working on file names instead
# of source numbers in install section
%setup -c -T
cp -p %{sources} .

%build

%install
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d
install -p -m 0644 -t %{buildroot}/%{_rpmconfigdir}/macros.d macros.kernel-srpm
mkdir -p %{buildroot}%{rrcdir}/find-provides.d
mkdir -p %{buildroot}%{_fileattrsdir}
install -p -m 755 -t %{buildroot}%{rrcdir} kmodtool rpmsort symset-table
install -p -m 755 -t %{buildroot}%{rrcdir} find-provides.ksyms find-requires.ksyms
install -p -m 755 -t %{buildroot}%{rrcdir}/find-provides.d firmware.prov modalias.prov
install -p -m 755 -t %{buildroot}%{rrcdir} brp-kmod-restore-perms brp-kmod-set-exec-bit
install -p -m 644 -t %{buildroot}%{_rpmconfigdir}/macros.d macros.kmp
install -p -m 644 -t %{buildroot}%{_fileattrsdir} kmod.attr
install -p -m 644 -t "%{buildroot}%{_fileattrsdir}" kabi.attr
install -p -m 755 -t "%{buildroot}%{_rpmconfigdir}" kabi.sh
install -p -m 644 -t "%{buildroot}%{_fileattrsdir}" provided_ksyms.attr required_ksyms.attr
install -p -m 644 -t "%{buildroot}%{_fileattrsdir}" modalias.attr
%oreon_autofiles kernel-rpm-macros usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kernel-rpm-macros -f %{oreon_filedir}/kernel-rpm-macros.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-28
- Prepare for Oreon 11 (RP1)
