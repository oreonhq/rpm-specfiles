%global source0_hash cfa9faf659f2ed6b38e7a7c3fb43e177d00edbacc6265e6e32215ff40e3793c0

Name:           pass
Summary:        A password manager using standard Unix tools
Version:        1.7.4
Release:        19%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Url:            http://zx2c4.com/projects/password-store/
BuildArch:      noarch
Source:         http://git.zx2c4.com/password-store/snapshot/password-store-%{version}.tar.xz
Patch:          0001-Default-to-xclip-if-wl-clip-is-not-found.patch
Patch:          0002-Check-if-required-dependencies-are-available.patch

BuildRequires: make
BuildRequires:       git-core
BuildRequires:       gnupg2
BuildRequires:       perl-generators
BuildRequires:       tree >= 1.7.0
Recommends:          (wl-clipboard if libwayland-client)
Recommends:          (xclip if xorg-x11-server-Xorg)
Requires:            git-core
Requires:            gnupg2
Requires:            qrencode
Requires:            tree >= 1.7.0

%description
Stores, retrieves, generates, and synchronizes passwords securely using gpg
and git.

%package -n passmenu
Summary:        A dmenu based interface to pass.
Requires:       pass
Recommends:     (dmenu-wayland if libwayland-client)
Recommends:     (ydotool if libwayland-client)
Recommends:     (dmenu if xorg-x11-server-Xorg)
Recommends:     (xdotool if xorg-x11-server-Xorg)

%description -n passmenu
A dmenu based interface to pass, the standard Unix password manager. This
design allows you to quickly copy a password to the clipboard without having to
open up a terminal window if you don't already have one open. If `--type` is
specified, the password is typed using xdotool instead of copied to the
clipboard.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n password-store-%{version}
rm -f contrib/emacs/.gitignore

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} \
     BINDIR=%{_bindir} SYSCONFDIR=%{_sysconfdir} \
     MANDIR=%{_mandir} WITH_ALLCOMP="yes" \
     install

install -D -p -m 0755 contrib/dmenu/passmenu %{buildroot}%{_bindir}/passmenu

# Used by extensions
mkdir -p %{buildroot}%{_prefix}/lib/password-store/extensions

%check
make test

%files
%doc README COPYING contrib/emacs contrib/importers contrib/vim
%{_bindir}/pass
%{_datadir}/bash-completion/completions/pass
%{_datadir}/fish/vendor_completions.d/pass.fish
%{_datadir}/zsh/site-functions/_pass
%doc %{_mandir}/man1/*
%dir %{_prefix}/lib/password-store
%dir %{_prefix}/lib/password-store/extensions

%files -n passmenu
%doc contrib/dmenu/README.md
%{_bindir}/passmenu

%changelog
%autochangelog
