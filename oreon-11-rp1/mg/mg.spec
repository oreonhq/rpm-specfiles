%global source0_hash 8ca736b1e57d9681e7921d37b9cf0282e3098e2929ed37384400c78dae54762d
Name:          mg
Version:       20260719
Release:        1%{?dist}
Summary:        Tiny Emacs-like editor
License:       LicenseRef-Fedora-Public-Domain
URL:           https://github.com/hboetes/mg
Source0:        https://github.com/hboetes/%{name}/archive/%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libbsd-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
mg is a tiny public-domain Emacs-like editor included in the base OpenBSD
system. It is compatible with Emacs because there shouldn't be any reason to
learn more editor types than Emacs or vi.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%make_build CFLAGS="%{optflags}" LDFLAGS="%{optflags} -lncurses" libdir="%{_libdir}"
%install
rm -rf %{buildroot}
%make_install prefix=%{_prefix} mandir=%{_mandir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
