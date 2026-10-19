%global source0_hash none
Name:           color-filesystem
Version:        1
Release:        1%{?dist}
Summary:        Color filesystem layout
License:        LicenseRef-Not-Copyrightable
BuildArch:      noarch
Requires:  filesystem
Requires:  rpm       
# oreon:deps

# /oreon:deps
%description
This package provides some directories that are required/used to store color. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# Nothing to prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/color/icc
mkdir -p $RPM_BUILD_ROOT%{_datadir}/color/cmms
mkdir -p $RPM_BUILD_ROOT%{_datadir}/color/settings
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/color/icc
mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d/
cat >$RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d/macros.color<<EOF
%%_colordir %%_datadir/color
%%_syscolordir %%_colordir
%%_icccolordir %%_colordir/icc
%%_cmmscolordir %%_colordir/cmms
%%_settingscolordir %%_colordir/settings
EOF
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1-38
- Prepare for Oreon 11 (RP1)
