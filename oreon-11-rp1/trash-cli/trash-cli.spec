%global source0_hash 734f5433adeec2b21b1a0cdb3e113bb670cc5e109b9ca8a3ed34fa0b8159f1f9
Summary:        Command line interface to the freedesktop.org trashcan
Name:           trash-cli
Version:        0.26.9.14
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL  :          https://github.com/andreafrancia/trash-cli
Source0:        https://github.com/andreafrancia/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:		virtualenv-versionlift.patch
Patch2:         trash-cli-0.24.5.26-no-parameterized.patch
Patch3:         trash-cli-rm-python-mock-usage.diff
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-trash-cli = %{version}-%{release}
# /oreon:deps
%description
trash-cli provides a command line trash usable with GNOME, KDE, Xfce or any
freedesktop.org compatible trash implementation. The command line interface is
compatible with rm and you can use trash-put as an alias to rm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pytest -m "not slow"
%files

%changelog

%autochangelog
