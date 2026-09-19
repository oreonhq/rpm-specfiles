%global source0_hash 3b397446b609fe86ab35d767cfe26340ac9163a64dbccf6c25aa6a9fbe57dccc

# Use define instead of global to ensure it's evaluated when used
%define lc_name %(echo "%{name}" | tr '[:upper:]' '[:lower:]')

Name:		DisplayCAL
Version:	3.9.16
Release:	8%{?dist}
Summary:	Display calibration and profiling tool focusing on accuracy and versatility
License:	GPL-3.0-or-later
URL:		https://github.com/eoyilmaz/displaycal-py3
Source0:	%{pypi_source %{name}}
Patch0:		displaycal-3.9.3-udev-dir.patch
Patch1:		displaycal-skip-update-check.patch
Patch2:		displaycal-3.9.15-fix-autostart-location.patch
Patch3:		displaycal-3.9.15-downgrade-wxpython.patch
Patch4:		displaycal-3.9.16-revert-license-field-change.patch

BuildArch:	noarch

BuildRequires:	git-core
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pyproject-rpm-macros
BuildRequires:	xdg-user-dirs

Requires:	argyllcms
Requires:	hicolor-icon-theme
# workaround for crash with pyglet as sound backend
Requires:	SDL2_mixer

Provides:	%{lc_name} = %{version}-%{release}
Provides:	dispcalGUI = %{version}-%{release}

# For archful->noarch chnage
Obsoletes:	%{name} < 3.9.15-2

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

%generate_buildrequires
%pyproject_buildrequires

%build
export CFLAGS="%{build_cflags} -Wno-incompatible-pointer-types"
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart/
mv %{buildroot}%{_datadir}/DisplayCAL/z-displaycal-apply-profiles.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/

# Drop files that aren't supposed to be shipped
rm -rfv %{buildroot}%{python3_sitelib}/{misc,tests,util}
rm -rfv %{buildroot}%{_datadir}/doc-base

%files -f %{pyproject_files}
%docdir %{_docdir}/%{name}-%{version}/
%doc %{_docdir}/%{name}-%{version}/*
%license LICENSE.txt
%{_sysconfdir}/xdg/autostart/z-displaycal-apply-profiles.desktop
%{_bindir}/%{lc_name}*
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{lc_name}*.png
%{_datadir}/applications/%{lc_name}*.desktop
%{_metainfodir}/net.displaycal.%{name}.appdata.xml
%{_mandir}/man1/%{lc_name}*

%changelog
%autochangelog
