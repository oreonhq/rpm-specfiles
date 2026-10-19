%global source0_hash 2219a37cb3cd9ab5ae271c7a03c5dc0d2458ffb922f67def5b89a3a065662697
%define _empty_manifest_terminate_build 0
Name:           authselect
Version:        1.8.0
Release:        1%{?dist}
Summary:        Configures authentication and identity sources from supported profiles
URL:            https://github.com/authselect/authselect
License:        GPL-3.0-or-later
Source0:        https://github.com/authselect/authselect/archive/refs/tags/1.8.0.tar.gz#/authselect-1.7.1.tar.gz
%global makedir %{_builddir}/%{name}-%{version}
%global with_nis_profile 1
%{?fedora:%global default_profile local with-silent-lastlog}
%{?rhel:%global default_profile local}
Requires: authselect-libs%{?_isa} = %{version}-%{release}
Suggests(meta): sssd
Suggests(meta): samba-winbind
Suggests(meta): fprintd-pam
Suggests(meta): oddjob-mkhomedir
Obsoletes: authselect-compat < 1.3
# oreon:deps
BuildRequires:  /usr/bin/a2x
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libcmocka-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(popt)
BuildRequires:  po4a
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Authselect is designed to be a replacement for authconfig but it takes
a different approach to configure the system. Instead of letting
the administrator build the PAM stack with a tool (which may potentially
end up with a broken configuration), it would ship several tested stacks
(profiles) that solve a use-case and are well tested and supported.
At the same time, some obsolete features of authconfig are not
supported by authselect.

%package libs
Summary: Utility library used by the authselect tool
Requires: coreutils
Requires: sed
Suggests: systemd
%description libs
Common library files for authselect. This package is used by the authselect
command line tool and any other potential front-ends.

%package devel
Summary: Development libraries and headers for authselect
Requires: authselect-libs%{?_isa} = %{version}-%{release}
%description devel
System header files and development libraries for authselect. Useful if
you develop a front-end for the authselect library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

for p in %patches ; do
    %__patch -p1 -i $p
done

%build

autoreconf -if
%configure \
    --with-nis-profile \
    %{nil}
%make_build
%check

%make_build check
%install
%make_install
%find_lang %{name}
%find_lang %{name} %{name}.8.lang --with-man
%find_lang %{name}-migration %{name}-migration.7.lang --with-man
%find_lang %{name}-profiles %{name}-profiles.5.lang --with-man
%__sed -i '/LC_MESSAGES/d' %{name}.8.lang
find $RPM_BUILD_ROOT -name "*.la" -exec %__rm -f {} \;
find $RPM_BUILD_ROOT -name "*.a" -exec %__rm -f {} \;
%ldconfig_scriptlets libs
%oreon_autofiles authselect-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles authselect-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post libs

%systemd_post authselect-apply-changes.service
%preun libs

%systemd_preun authselect-apply-changes.service
%postun libs

%systemd_postun authselect-apply-changes.service
%posttrans libs

if test -e /run/ostree-booted; then
    for PROFILE in `ls %{_datadir}/authselect/default`; do
        %{_bindir}/authselect create-profile $PROFILE --vendor --base-on $PROFILE --symlink-pam --symlink-dconf --symlink=REQUIREMENTS --symlink=README &> /dev/null
        %__sed -i -e 's/{if "with-altfiles":\([^}]\+\)}/\1/g' %{_datadir}/authselect/vendor/$PROFILE/nsswitch.conf &> /dev/null
    done
fi
if [ $1 == 1 ] ; then
    %{_bindir}/authselect select %{default_profile} --force --nobackup &> /dev/null
    exit 0
fi
%__sed -i '1 s/^minimal$/local/'  %{_sysconfdir}/authselect/authselect.conf
for file in  %{_sysconfdir}/authselect/custom/*/*; do
    link=`%{_bindir}/readlink "$file"`
    if [[ "$link" == %{_datadir}/authselect/default/minimal/* ]]; then
        target=`%{_bindir}/basename "$link"`
        %{_bindir}/ln -sfn "%{_datadir}/authselect/default/local/$target" "$file"
    fi
done
%{_bindir}/find "%{_datadir}/authselect" -mindepth 2 -type f \
    -printf "%%P\n" -exec %{_bindir}/sha256sum {} + | %{_bindir}/sha256sum \
    > "%{_datadir}/authselect/checksum"
%{_bindir}/authselect apply-changes &> /dev/null
exit 0
%preun

if [ $1 == 0 ] ; then
    %{_bindir}/authselect opt-out
fi
%files -f %{oreon_filedir}/main.list
%files -n authselect-libs -f %{oreon_filedir}/authselect-libs.list
%files -n authselect-devel -f %{oreon_filedir}/authselect-devel.list

%changelog

%autochangelog
