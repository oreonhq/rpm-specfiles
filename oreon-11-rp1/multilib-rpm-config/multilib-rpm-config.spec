# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ee830f5bbfab3187510513a0a723176a4f0709c06a5876f54d6282ffda2cf89d
%global commit 8f007caf419811c533b41d0e9c65e3c81f5d72f4
%global mlurl https://src.fedoraproject.org/rpms/multilib-rpm-config/raw/%{commit}/f
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%global rrcdir %_libexecdir

Name: multilib-rpm-config
Version: 1
Release: 31%{?dist}
Summary: Multilib packaging helpers
License: GPL-2.0-or-later
URL: https://src.fedoraproject.org/rpms/multilib-rpm-config
Source0: %{mlurl}/multilib-fix
Source1: %{mlurl}/macros.ml
Source2: %{mlurl}/README
Source3: %{mlurl}/COPYING
Source4: %{mlurl}/multilib-library
Source5: %{mlurl}/multilib-info
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
Requires: redhat-rpm-config

%description
Shell scripts and RPM macros for multilib header packaging.

%prep
%oreon_sha256
echo cce8ea8b3bc3b7c143c99303b2ab9b19bfa2ee6a33681ee19c7eea255740a2ea %{SOURCE1} > sources.sha256
echo 063ad35ea4d5d4cc2d8cb5b11bd896c7f33475e08131a028ac8b2bb6ab1941cd %{SOURCE2} >> sources.sha256
echo 8177f97513213526df2cf6184d8ff986c675afb514d4e68a404010521b880643 %{SOURCE3} >> sources.sha256
echo 6fdcaf11ecefe58525a9f1da8159bf2364b7b84a331c5b33a7642c3742dcbaaf %{SOURCE4} >> sources.sha256
echo 782895c542382e8629bac2575b23f295936d28656400a74910651664cd4e9f5d %{SOURCE5} >> sources.sha256
sha256sum -c sources.sha256
%setup -c -T
install -m 644 %{SOURCE2} %{SOURCE3} .

%build
%global ml_fix %rrcdir/multilib-fix
%global ml_info %rrcdir/multilib-info
lib_sed_pattern='/@LIB@/ {
    r %{SOURCE4}
    d
}'
sed -e 's|@ML_FIX@|%ml_fix|g' -e 's|@ML_INFO@|%ml_info|g' %{SOURCE1} > macros.multilib
sed -e "$lib_sed_pattern" %{SOURCE0} > multilib-fix
sed -e "$lib_sed_pattern" %{SOURCE5} > multilib-info

%install
mkdir -p %{buildroot}%{rrcdir}
mkdir -p %{buildroot}%{macrosdir}
install -m 644 -p macros.multilib %{buildroot}/%{macrosdir}
install -m 755 -p multilib-fix %{buildroot}/%{ml_fix}
install -m 755 -p multilib-info %{buildroot}/%{ml_info}

%check
mkdir tests
cd tests
ml_fix="sh `pwd`/../multilib-fix --buildroot `pwd`"
capable="sh `pwd`/../multilib-info --multilib-capable"
mkdir template
cat > template/main.c <<'EOF'
#include "header.h"
int main () { call (); return 0; }
EOF
cat > template/header.h <<'EOF'
#include <stdio.h>
void call (void) { printf ("works!\n"); }
EOF
cp -r template basic
gcc ./basic/main.c
./a.out
if `$capable`; then
    cp -r template really-works
    $ml_fix --file /really-works/header.h
    gcc really-works/main.c
    ./a.out
    test -f really-works/header-*.h
fi
cp -r template other_arch
$ml_fix --file /other_arch/header.h --arch ppc64
test -f other_arch/header-*.h
cp -r template other_arch_fix
$ml_fix --file /other_arch_fix/header.h --arch ppc64p7
test -f other_arch_fix/header-ppc64.h
cp -r template aarch64-no-change
$ml_fix --file /aarch64-no-change/header.h --arch aarch64
test ! -f aarch64-no-change/header-*.h
test `$capable --arch x86_64` = true
test `$capable --arch aarch64` = false
test `$capable --arch ppc64p7` = true

%files
%license COPYING
%doc README
%{rrcdir}/*
%{macrosdir}/*
