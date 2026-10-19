%global source0_hash f4fdfbc451d1fb5764531290a202a0a871f6b81ba3c01a6b76c49435c85080a5
Name:		rcm
Version:	1.3.6
Release:        1%{?dist}
Summary:        Management suite for dotfiles
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/thoughtbot/rcm
Source0:        https://thoughtbot.github.io/rcm/dist/%{name}-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  python3-cram
# /oreon:deps
%description
A suite of tools for managing dot-files (.zshrc, .vimrc, etc.).  This suite is
useful for committing your .*rc files to a central repository to share, but it
also scales to a more complex situation such as multiple source directories
shared between computers with some host-specific or task-specific files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
