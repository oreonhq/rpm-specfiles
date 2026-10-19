%global source0_hash 1397bba6774a6361171c72464ddcdcfbc36d44fa413ecc9a1d56092f8da58825
Name: firejail
Summary:        Linux namespaces sandbox program
%global ver_no 0.9.80
Version: %{expand:%{ver_no}%{?ver_rc:~}%{?ver_rc}}
Release:        1%{?dist}
Requires: xdg-dbus-proxy
License: GPL-2.0-or-later
URL: https://github.com/netblue30/firejail
%global git_tag %{expand:%{ver_no}%{?ver_rc:-}%{?ver_rc}}
Source0:        https://github.com/netblue30/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
%description
Firejail is a SUID sandbox program that reduces the risk of security
breaches by restricting the running environment of untrusted applications
using Linux namespaces. It includes a sandbox profile for Mozilla Firefox.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n firejail-%{git_tag}

%build

%configure --enable-selinux | tee fedconfig.txt
for FEATURE in DBUSPROXY LANDLOCK SELINUX X11 ; do
	grep -e "-DHAVE_${FEATURE}$" fedconfig.txt
done
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
