%global source0_hash 382959c3bfa2765b5346232438650491b822a16607ff5699178aa1386e3878d4
Name:             mpc
Summary:        Command-line client for MPD
Version:          0.35
Release:        1%{?dist}
License:          GPL-2.0-or-later
URL:              http://www.musicpd.org/
Source0:        http://www.musicpd.org/download/mpc/0/mpc-%{version}.tar.xz
# oreon:deps
BuildRequires:  bash-completion
BuildRequires:  gcc
BuildRequires:  libmpdclient-devel
BuildRequires:  meson
BuildRequires:  python3-sphinx
BuildRequires:  rsync
# /oreon:deps
%description
A client for MPD, the Music Player Daemon. mpc connects to a MPD running
on a machine via a network.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
install -p -D -m0644 contrib/mpc-completion.bash %{buildroot}%{bash_completions_dir}/%{name}
for i in mpd-m3u-handler.sh mpd-pls-handler.sh; do
    install -p -D -m0755 %{buildroot}%{_datadir}/doc/%{name}/contrib/${i} \
        %{buildroot}%{_libexecdir}/%{name}/${i}
done
rm -rf %{buildroot}%{_pkgdocdir}/contrib
rm -f %{buildroot}%{_pkgdocdir}/COPYING
rm -f %{buildroot}%{_pkgdocdir}/html/.buildinfo
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
