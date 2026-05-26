# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 5bb5d1be011158090157c9e7587ae5606c262a5020ecdc5caac6686b9910592e
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Summary: Utility to set/show the host name or domain name
Name: hostname
Version: 3.25
Release: %autorelease
License: GPL-2.0-or-later
URL: https://tracker.debian.org/pkg/hostname
Source0: https://ftp.debian.org/debian/pool/main/h/hostname/hostname_%{version}.tar.xz
Source1: https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
Source2: nis-domainname
Source3: nis-domainname.service
BuildRequires: gcc
BuildRequires: make

# NOTE: We are *not* requiring systemd on purpose, because we want to allow
#       hostname package to be installed in containers without the systemd.

# Initial changes
Patch1: hostname-rh.patch

%description
This package provides commands which can be used to display the system's
DNS name, and to display or set its hostname or NIS domain name.

%prep
%oreon_verify_sources
%setup -q -n hostname
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} .
%patch -P 1 -p1

%build
make CFLAGS="%{optflags} $CFLAGS -D_GNU_SOURCE" LDFLAGS="$RPM_LD_FLAGS"

%install
make DESTDIR=%{buildroot} install

install -m 0755 -d %{buildroot}%{_libexecdir}/%{name}
install -m 0755 -d %{buildroot}%{_prefix}/lib/systemd/system
install -m 0755 nis-domainname         %{buildroot}%{_libexecdir}/%{name}
install -m 0644 nis-domainname.service %{buildroot}%{_prefix}/lib/systemd/system

%post
if [ $1 -eq 1 ]; then
  # Initial installation...
  systemctl --no-reload preset nis-domainname.service &>/dev/null || :
fi

%preun
if [ $1 -eq 0 ]; then
  # Package removal, not upgrade...
  systemctl --no-reload disable --now nis-domainname.service &>/dev/null || :
fi

# NOTE: Nothing to do for upgrade (in postun), nis-domainname.service is oneshot.

%files
%doc COPYRIGHT
%{!?_licensedir:%global license %%doc}
%license gpl-2.0.txt
%{_bindir}/*
%{_mandir}/man1/*
%{_prefix}/lib/systemd/system/*
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.25-1
- Prepare for Oreon 11 (RP1)
