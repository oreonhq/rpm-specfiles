%global source0_hash 3b397446b609fe86ab35d767cfe26340ac9163a64dbccf6c25aa6a9fbe57dccc
%define lc_name %(echo "%{name}" | tr '[:upper:]' '[:lower:]')
Name:		DisplayCAL
Version:	3.9.16
Release:        8%{?dist}
Summary:        Display calibration and profiling tool focusing on accuracy and versatility
License:	GPL-3.0-or-later
URL:		https://github.com/eoyilmaz/displaycal-py3
Source0:        https://files.pythonhosted.org/packages/source/D/DisplayCAL/DisplayCAL-%{version}.tar.gz
Patch0:		displaycal-3.9.3-udev-dir.patch
Patch1:		displaycal-skip-update-check.patch
Patch2:		displaycal-3.9.15-fix-autostart-location.patch
Patch3:		displaycal-3.9.15-downgrade-wxpython.patch
Patch4:		displaycal-3.9.16-revert-license-field-change.patch
BuildArch:	noarch
Requires:	argyllcms
Requires:	hicolor-icon-theme
Requires:	SDL2_mixer
Provides:	%{lc_name} = %{version}-%{release}
Provides:	dispcalGUI = %{version}-%{release}
Obsoletes:	%{name} < 3.9.15-2
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-DisplayCAL = %{version}-%{release}
# /oreon:deps
%description
This utility calibrates and characterizes display devices using one
of many supported measurement instruments, with support for
multi-display setups and a variety of available options for advanced
users, such as verification and reporting functionality to evaluate
ICC profiles and display devices, creating video 3D LUTs, as well as
optional CIECAM02 gamut mapping to take into account varying viewing
conditions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -n %{lc_name}-%{version}

# Delete git data to prevent broken versioning
rm -rf .git

# Delete existing egg
rm -rf DisplayCAL.egg-info
# Delete PKG-INFO that causes inadvertent Python version restrictions
rm PKG-INFO

# hack to force creating dist/net.displaycal... (missed due pyproject)
sed -i -e 's|create_appdata = |create_appdata = True or |' setup.py

# drop prebuilt modules
find . -name '*.so' -print -delete

# fix paths
%ifarch %{arm32} %{ix86}
ln -s ./lib64 DisplayCAL/lib32
sed -i -e 's/DisplayCAL\.lib64/DisplayCAL\.lib32/g' DisplayCAL/RealDisplaySizeMM.py
%endif

%build

export CFLAGS="%{build_cflags} -Wno-incompatible-pointer-types"
%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart/
mv %{buildroot}%{_datadir}/DisplayCAL/z-displaycal-apply-profiles.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/
rm -rfv %{buildroot}%{python3_sitelib}/{misc,tests,util}
rm -rfv %{buildroot}%{_datadir}/doc-base
%oreon_autofiles main

%files

%changelog

%autochangelog
