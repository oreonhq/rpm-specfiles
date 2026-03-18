# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_of_Additional_RPM_Macros
%global macrosdir       %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

%global rrcdir          %_libexecdir

Summary: Multilib packaging helpers
Name: multilib-rpm-config
Version: 1
Release: 30%{?dist}
License: GPL-2.0-or-later

# TODO: resolve directly in rpm/redhat-rpm-config (instead of this hack).
# Note that to avoid FTBFS against plain RHEL6, we can't put this hack before
# License tag.
%{!?_licensedir:%global license %%doc}

URL: https://fedoraproject.org/wiki/PackagingDrafts/MultilibTricks

BuildRequires: gcc

Source0: multilib-fix
Source1: macros.ml
Source2: README
Source3: COPYING
Source4: multilib-library
Source5: multilib-info

BuildArch: noarch

# Most probably we want to move everything here?
Requires: redhat-rpm-config

%description
Set of tools (shell scripts, RPM macro files) to help with multilib packaging
issues.


%prep
%setup -c -T
install -m 644 %{SOURCE2} %{SOURCE3} .


%build
%global ml_fix %rrcdir/multilib-fix
%global ml_info %rrcdir/multilib-info

lib_sed_pattern='/@LIB@/ {
    r %{SOURCE4}
    d
}'

sed -e 's|@ML_FIX@|%ml_fix|g' \
    -e 's|@ML_INFO@|%ml_info|g' \
    %{SOURCE1} > macros.multilib
sed -e "$lib_sed_pattern" \
    %{SOURCE0} > multilib-fix
sed -e "$lib_sed_pattern" \
    %{SOURCE5} > multilib-info


%install
mkdir -p %{buildroot}%{rrcdir}
mkdir -p %{buildroot}%{macrosdir}
install -m 644 -p macros.multilib %{buildroot}/%{macrosdir}
install -m 755 -p multilib-fix %{buildroot}/%{ml_fix}
install -m 755 -p multilib-info %{buildroot}/%{ml_info}


%check
mkdir tests ; cd tests
ml_fix="sh `pwd`/../multilib-fix --buildroot `pwd`"
capable="sh `pwd`/../multilib-info --multilib-capable"

mkdir template
cat > template/main.c <<EOF
#include "header.h"
int main () { call (); return 0; }
EOF
cat > template/header.h <<EOF
#include <stdio.h>
void call (void) { printf ("works!\n"); }
EOF

cp -r template basic
gcc ./basic/main.c
./a.out

pwd
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


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1-30
- Prepare for Oreon 11 (RP1)
