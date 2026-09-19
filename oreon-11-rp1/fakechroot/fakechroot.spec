%global source0_hash 7f9d60d0d48611969e195fadf84d05f6c74f71bbf8f41950ad8f5bf061773e18

Name:           fakechroot
Version:        2.20.1
Release:        24%{?dist}
Summary:        Gives a fake chroot environment
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/dex4er/fakechroot
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:         https://github.com/dex4er/fakechroot/commit/b42d1fb9538f680af2f31e864c555414ccba842a.patch
Patch2:         https://github.com/dex4er/fakechroot/pull/80.patch
Patch4:         https://github.com/dex4er/fakechroot/pull/104.patch
Patch10:        autoupdate.patch
Patch11:        disable_socket-af_unix.t.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
# Required for manpage
BuildRequires:  /usr/bin/pod2man
# BuildRequires:  gdbm-libs
# ldd.fakechroot
Requires:       /usr/bin/objdump
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
fakechroot runs a command in an environment were is additionally
possible to use the chroot(8) call without root privileges. This is
useful for allowing users to create their own chrooted environment
with possibility to install another packages without need for root
privileges.

%package        libs
Summary:        Libraries of %{name}

%description    libs
This package contains the libraries required by %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# For %%doc dependency-clean.
chmod -x scripts/{relocatesymlinks,restoremode,savemode}.sh

%build
autoreconf -vfi

%if 0%{?__isa_bits} == 64
%configure --disable-static --disable-silent-rules --with-libpath="%{_libdir}/fakechroot:/usr/lib/fakechroot"
%else
%configure --disable-static --disable-silent-rules --with-libpath="%{_libdir}/fakechroot:/usr/lib64/fakechroot"
%endif

%make_build

%install
%make_install
# Drop libtool files
find %{buildroot}%{_libdir} -name '*.la' -delete -print

%check
%ifnarch ppc64le
%make_build check
%endif

%files
%doc scripts/{relocatesymlinks,restoremode,savemode}.sh
%doc NEWS.md README.md THANKS.md
%license COPYING LICENSE
%{_bindir}/%{name}
%{_bindir}/env.%{name}
%{_bindir}/ldd.%{name}
%{_sbindir}/chroot.%{name}
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/chroot.env
%config(noreplace) %{_sysconfdir}/%{name}/debootstrap.env
%config(noreplace) %{_sysconfdir}/%{name}/rinse.env
%{_mandir}/man1/%{name}.1*

%files libs
%{_libdir}/%{name}/

%changelog
%autochangelog
