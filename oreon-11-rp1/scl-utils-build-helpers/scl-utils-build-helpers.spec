%global source0_hash none
%global macrosdir       %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%global rrcdir          %_libexecdir
Name:           scl-utils-build-helpers
Version:        0
Release:        1%{?dist}
Summary:        RPM macros and scripts for SCL maintainers
BuildArch:      noarch
License:        LGPL-2.1-or-later
URL:            https://github.com/sclorg/scl-utils-build-helpers
Source0:        README.md
Source1:        COPYING
Source100:      scl-helper-wrap-bin.sh
Source101:      macros.scl-build-helpers
Requires:       scl-utils-build
# oreon:deps

# /oreon:deps
%description
Several RPM macros and convenience scripts to make the maintenance of packages
for Software Collections easier.  The aim is to move as much duplicated code as
possible into one (dedicated) place.

%prep

%setup -c -T

%build

%install
%global wrap_script %rrcdir/%(basename %SOURCE100)
%global macros %macrosdir/%(basename %SOURCE101)
substitutions=(
    -e 's|@SCRIPT_WRAP@|%wrap_script|g'
    -e 's|@MACROS@|%macros|g'
    -e 's|@GENERATOR@|%name-%version-%release|g'
)
install -p -m 644 %SOURCE0 .
install -p -m 644 %SOURCE1 .
mkdir -p %buildroot%rrcdir
mkdir -p %buildroot%macrosdir
sed "${substitutions[@]}" %{SOURCE100} > %buildroot%wrap_script
sed "${substitutions[@]}" %{SOURCE101} > %buildroot%macros
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
