%global source0_hash d313d017665423a8f526e5fe8a44471a3e27be752074dbdeed29f9d6b6f7bf87
%bcond_without tests
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64
ExcludeArch:    ppc64 ppc64le
Name:       protontricks
Version:    1.14.0
Release:        1%{?dist}
Summary:        Simple wrapper that does winetricks things for Proton enabled games
BuildArch:  noarch
License:    GPL-3.0-or-later
URL:        https://github.com/Matoking/protontricks
Source0:        https://files.pythonhosted.org/packages/source/p/protontricks/protontricks-%{version}.tar.gz
%if %{with tests}
%endif
Requires:   winetricks
Recommends: yad
Suggests:   zenity
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-protontricks = %{version}-%{release}
# /oreon:deps
%description
Run Winetricks commands for Steam Play/Proton games among other common Wine
features, such as launching external Windows executables.

This is a fork of the original project created by sirmentio. The original
repository is available at Sirmentio/protontricks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
rm %{buildroot}%{_bindir}/%{name}-desktop-install
%oreon_autofiles main

%check

%if %{with tests}
%pyproject_check_import
%pytest
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files

%changelog

%autochangelog
