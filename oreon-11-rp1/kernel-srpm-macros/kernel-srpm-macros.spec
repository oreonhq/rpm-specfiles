%global source0_hash none

Name:           kernel-srpm-macros
Version:        1.0
# when bumping version and resetting release, don't forget to bump version of kernel-rpm-macros as well
Release:        28%{?dist}
Summary:        RPM macros that list arches the full kernel is built on
# This package only exist in Fedora repositories
# The license is the standard (MIT) specified in
# Fedora Project Contribution Agreement
# and as URL we provide dist-git URL
License:        MIT
URL:            https://src.fedoraproject.org/rpms/kernel-srpm-macros
BuildArch:      noarch
# We are now the ones shipping kmod.attr
Conflicts:      redhat-rpm-config < 205
# macros.kmp, kmodtool and rpmsort were moved from kernel-rpm-macros
# to kernel-srpm-macros in 1.0-9/185-9
Conflicts:      kernel-rpm-macros < 205

# Macros
Source0:        macros.kernel-srpm
Source1:        macros.kmp

# Dependency generator scripts
Source100:      find-provides.ksyms
Source101:      find-requires.ksyms
Source102:      firmware.prov
Source103:      modalias.prov
Source104:      provided_ksyms.attr
Source105:      required_ksyms.attr
Source106:      modalias.attr

# Dependency generators & their rules
Source200:      kmod.attr

# Misc helper scripts
Source300:      kmodtool
Source301:      rpmsort
Source302:      symset-table

# kabi provides generator
Source400: kabi.attr
Source401: kabi.sh

# BRPs
Source500: brp-kmod-set-exec-bit
Source501: brp-kmod-restore-perms

%global rrcdir /usr/lib/rpm/redhat


%description
This packages contains the rpm macro that list what arches
the full kernel is built on.
The variable to use is kernel_arches.

%package -n kernel-rpm-macros
Version: 205
Summary: Macros and scripts for building kernel module packages
# rpmsort is GPL-2.0-or-later
License:        MIT AND GPL-2.0-or-later
Requires: redhat-rpm-config >= 205

# for brp-kmod-compress
Requires: %{_bindir}/xz
# for brp-kmod-compress, brp-kmod-set-exec-bit
Requires: %{_bindir}/find
# for find-provides.ksyms, find-requires.ksyms, kmodtool
Requires: %{_bindir}/sed
# for find-provides.ksyms, find-requires.ksyms
Requires: %{_bindir}/awk
Requires: %{_bindir}/grep
Requires: %{_bindir}/nm
Requires: %{_bindir}/objdump
Requires: %{_bindir}/readelf
# for find-requires.ksyms
Requires: %{_sbindir}/modinfo
Requires: %{_sbindir}/modprobe

%description -n kernel-rpm-macros
Macros and scripts for building kernel module packages.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
# Not strictly necessary but allows working on file names instead
# of source numbers in install section
%setup -c -T
cp -p %{sources} .


%build
# nothing to do


%install
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d
install -p -m 0644 -t %{buildroot}/%{_rpmconfigdir}/macros.d macros.kernel-srpm
%if 0%{?rhel} >= 8
  sed -i 's/^%%kernel_arches.*/%%kernel_arches x86_64 s390x ppc64le aarch64 riscv64/' \
    %{buildroot}/%{_rpmconfigdir}/macros.d/macros.kernel-srpm
%endif

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

%files
%{_rpmconfigdir}/macros.d/macros.kernel-srpm
%{_fileattrsdir}/kmod.attr

%files -n kernel-rpm-macros
%{_rpmconfigdir}/macros.d/macros.kmp
%{_rpmconfigdir}/kabi.sh
%{_fileattrsdir}/kabi.attr
%{_fileattrsdir}/modalias.attr
%{_fileattrsdir}/provided_ksyms.attr
%{_fileattrsdir}/required_ksyms.attr
%dir %{rrcdir}/find-provides.d
%{rrcdir}/brp-kmod-restore-perms
%{rrcdir}/brp-kmod-set-exec-bit
%{rrcdir}/symset-table
%{rrcdir}/find-provides.ksyms
%{rrcdir}/find-requires.ksyms
%{rrcdir}/find-provides.d/firmware.prov
%{rrcdir}/find-provides.d/modalias.prov
%{rrcdir}/kmodtool
%{rrcdir}/rpmsort

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-28
- Prepare for Oreon 11 (RP1)
