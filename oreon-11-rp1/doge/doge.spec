%global source0_hash b8349ea9d1fcd397ec9eda52149b753e0d76add14bc811cbb391632b86f3ba14
Name:           doge
Version:        3.9.1
Release:        1%{?dist}
Summary:        MOTD script based on the doge meme
License:        MIT
URL:            https://github.com/thiderman/doge
Source0:        https://github.com/thiderman/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-doge = %{version}-%{release}
# /oreon:deps
%description
doge is a simple motd script based on the doge meme. It prints random
grammatically incorrect statements that are sometimes based on things from your
computer.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# such shebangs wow
sed -i -e '/^#!\//, 1d' doge/*.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%files

%changelog

%autochangelog
