%global source0_hash 1397bba6774a6361171c72464ddcdcfbc36d44fa413ecc9a1d56092f8da58825

# Based on initial .spec file from upstream, link here 
# https://github.com/netblue30/firejail/blob/master/platform/rpm/firejail.spec
# Originally created by Firejail authors

Name: firejail
Summary: Linux namespaces sandbox program

%global ver_no 0.9.80
#%%global ver_rc rc4

Version: %{expand:%{ver_no}%{?ver_rc:~}%{?ver_rc}}
Release: 1%{?dist}

BuildRequires: coreutils
BuildRequires: gcc
BuildRequires: make

BuildRequires: libselinux-devel
BuildRequires: kernel-headers
BuildRequires: python3-devel

Requires: xdg-dbus-proxy

# spec released under GPLv2+, contacted upstream whether it can be 
# released under MIT
License: GPL-2.0-or-later
URL: https://github.com/netblue30/firejail

%global git_tag %{expand:%{ver_no}%{?ver_rc:-}%{?ver_rc}}
Source0: %{url}/archive/%{git_tag}/%{name}-%{git_tag}.tar.gz

%description
Firejail is a SUID sandbox program that reduces the risk of security
breaches by restricting the running environment of untrusted applications
using Linux namespaces. It includes a sandbox profile for Mozilla Firefox.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n firejail-%{git_tag}

%build
# For some features, if --enable-feature is requested, but the requirements
# are not satisfied (e.g. missing library headers), configure will only print
# a warning, instead of erroring out. Capture the output to a file...
%configure --enable-selinux | tee fedconfig.txt

# ...and make sure that all the features we're interested in are enabled.
for FEATURE in DBUSPROXY LANDLOCK SELINUX X11 ; do
	grep -e "-DHAVE_${FEATURE}$" fedconfig.txt
done

# Also ensure that stuff we don't want is not enabled.
for ANTIFEATURE in ; do
	if grep -e "-DHAVE_${ANTIFEATURE}$" fedconfig.txt; then
		exit 1
	fi
done

%make_build

%install
%make_install
chmod 0755 %{buildroot}%{_libdir}/%{name}/lib*.so

for f in \
	%{buildroot}%{_libdir}/%{name}/fj-mkdeb.py \
	%{buildroot}%{_libdir}/%{name}/fjclip.py \
	%{buildroot}%{_libdir}/%{name}/fjdisplay.py \
	%{buildroot}%{_libdir}/%{name}/fjresize.py
do
	sed -i "1 s/^.*$/\#\!\/usr\/bin\/python3/" "$f";
done

rm %{buildroot}%{_datadir}/gtksourceview-5/language-specs/firejail-profile.lang

%files
%doc README RELNOTES CONTRIBUTING.md
%license COPYING

%{_bindir}/firecfg
%{_bindir}/firemon
%{_bindir}/jailcheck
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datarootdir}/bash-completion/completions/
%{_datarootdir}/vim/vimfiles
%{_datarootdir}/zsh/site-functions/_%{name}
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/profile.template
%{_docdir}/%{name}/redirect_alias-profile.template
%{_docdir}/%{name}/*syscalls.txt
%{_mandir}/man5/%{name}-login.5*
%{_mandir}/man5/%{name}-profile.5*
%{_mandir}/man5/%{name}-users.5*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/%{name}

%changelog
%autochangelog
