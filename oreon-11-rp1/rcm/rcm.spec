%global source0_hash f4fdfbc451d1fb5764531290a202a0a871f6b81ba3c01a6b76c49435c85080a5

Name:		rcm
Version:	1.3.6
Release:	10%{?dist}
Summary:	Management suite for dotfiles

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/thoughtbot/rcm
Source0:	https://thoughtbot.github.io/rcm/dist/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	make
BuildRequires:	python3-cram
BuildRequires:	perl

%description
A suite of tools for managing dot-files (.zshrc, .vimrc, etc.).  This suite is
useful for committing your .*rc files to a central repository to share, but it
also scales to a more complex situation such as multiple source directories
shared between computers with some host-specific or task-specific files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install

%check
make check

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_mandir}/man{1,5,7}/*
%{_datadir}/rcm

%changelog
%autochangelog
