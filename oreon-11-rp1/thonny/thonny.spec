%global source0_hash efd0d28d143292f3943a6f3cb82edfecb91b88cc4f75f013209de5756aaf54b4
Name:           thonny
Version:        5.0.0
Release:        1%{?dist}
Summary:        Python IDE for beginners
License:        MIT AND EPL-1.0
URL:            https://thonny.org
Source0:        https://files.pythonhosted.org/packages/source/t/thonny/thonny-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-tkinter
Requires:       python3-pip
Requires:       python3-filelock
Requires:       hicolor-icon-theme
Provides:       bundled(python3dist(pipkin)) = 2.0~b2
Recommends:     python3-asttokens
Recommends:     python3-distro
Recommends:     zenity
Recommends:     xsel
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.12.0
BuildRequires:  python3dist(uv-build) >= 0.11.6
Requires:       python3-thonny = %{version}-%{release}
# /oreon:deps
%description
Thonny is a simple Python IDE with features useful for learning programming.
It comes with a debugger which is able to visualize all the conceptual steps
taken to run a Python program (executing statements, evaluating expressions,
maintaining the call stack). There is a GUI for installing 3rd party packages
and special mode for learning about references.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove localization helper scripts, we don't need them in the package
rm thonny/locale/compile_mo.bat thonny/locale/update_pot.bat thonny/locale/thonny.pot

# Remove the vendored python-filelock
rm -r thonny/vendored_libs/filelock/

%build

rm thonny/locale/*/LC_MESSAGES/*.mo
pybabel compile -d thonny/locale/ -D thonny
rm thonny/locale/*/LC_MESSAGES/*.po
%pyproject_wheel
%install
%pyproject_install
install -m 0644 -D -T packaging/icons/thonny-256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-64x64.png   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-48x48.png   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-32x32.png   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-22x22.png   %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-16x16.png   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/thonny.png
install -D -m 0644 -t %{buildroot}%{_datadir}/metainfo                    packaging/linux/org.thonny.Thonny.appdata.xml
install -D -m 0644 -t %{buildroot}%{_mandir}/man1                         packaging/linux/thonny.1
desktop-file-install --dir=%{buildroot}%{_datadir}/applications           packaging/linux/org.thonny.Thonny.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.thonny.Thonny.appdata.xml
%oreon_autofiles main

%check

%global __pytest xvfb-run %__pytest
%pytest --pyargs thonny
%files

%changelog

%autochangelog
