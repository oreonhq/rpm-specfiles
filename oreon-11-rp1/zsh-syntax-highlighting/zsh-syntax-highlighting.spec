%global source0_hash 5981c19ebaab027e356fe1ee5284f7a021b89d4405cc53dc84b476c3aee9cc32

Name:    zsh-syntax-highlighting
Version: 0.8.0
Release: 7%{?dist}

Summary: Fish shell like syntax highlighting for Zsh
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL:     https://github.com/zsh-users/zsh-syntax-highlighting
Source0: https://github.com/zsh-users/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: zsh

Requires: zsh

%description
This package provides syntax highlighting for the shell zsh. It enables
highlighting of commands whilst they are typed at a zsh prompt into an
interactive terminal. This helps in reviewing commands before running them,
particularly in catching syntax errors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
make

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
rm %{buildroot}/%{_docdir}/%{name}/COPYING.md

%check
#make test
#make perf

%files
%doc INSTALL.md
%license COPYING.md
%{_docdir}/%{name}
%{_datadir}/%{name}

%changelog
%autochangelog
