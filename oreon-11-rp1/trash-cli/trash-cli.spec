%global source0_hash 1d7dec1ad8f0264ceb1b0211d25fffee99c9409cd2e1d36dcc82ac5540f39ce5

Summary:        Command line interface to the freedesktop.org trashcan
Name:           trash-cli
Version:        0.24.5.26
Release:        %autorelease
License:        GPL-2.0-or-later
URL  :          https://github.com/andreafrancia/trash-cli
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:		virtualenv-versionlift.patch
# Replace parameterized with built-in pytest functionality
# https://github.com/andreafrancia/trash-cli/pull/373
Patch2:         trash-cli-0.24.5.26-no-parameterized.patch
# remove python-mock usage
Patch3:         trash-cli-rm-python-mock-usage.diff

BuildArch:      noarch
BuildRequires:  python3-devel

%description
trash-cli provides a command line trash usable with GNOME, KDE, Xfce or any
freedesktop.org compatible trash implementation. The command line interface is
compatible with rm and you can use trash-put as an alias to rm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l trashcli

%check
# There is a tox.ini in the repo and buildrequires -t works, but the README
# instructs to run pytest, so we do that. "not slow" should be enough for
# a quick verification.
%pytest -m "not slow"

%files -f %{pyproject_files}
%doc README.rst

%{_bindir}/trash*
%{_mandir}/man1/trash*

%changelog
%autochangelog
