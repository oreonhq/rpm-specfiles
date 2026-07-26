%global source0_hash 5e9761c0db45716583ff8c285f3a742e34ce7dc71de237333a280cbe40098f7b

%global appdefaultsdir /usr/share/X11/app-defaults

Name:               x11-ssh-askpass
Version:            1.2.4.1
Release:            44%{?dist}
Summary:            A passphrase dialog for X and not only for OpenSSH
License:            LicenseRef-Fedora-Public-Domain

# The original site has disappeared, but the source itself has
# reappeared on github.  The original site was:
#
# http://www.jmknoble.net/software/x11-ssh-askpass/
#
# We will use the github mirror of the original source from now on.
%global forgeurl    https://github.com/sigmavirus24/x11-ssh-askpass/
%global tag         %{version}
%global archivename %{name}-%{tag}
%global archiveext  tar.gz
%global archiveurl  %{forgeurl}/archive/refs/tags/%{tag}.%{archiveext}
%forgemeta

URL:                %{forgeurl}
Source0:            %{forgesource}
Source1:            x11-ssh-askpass.csh
Source2:            x11-ssh-askpass.sh
Patch0:             x11-ssh-askpass-1.2.4-random.patch
Patch1:             x11-ssh-askpass-1.2.4.1-gcc-14.x-warnings.patch

Provides:           openssh-askpass-x11

BuildRequires:      make
BuildRequires:      gcc
BuildRequires:      imake
BuildRequires:      libXt-devel
BuildRequires:      coreutils
BuildRequires:      sed

%description
x11-ssh-askpass is a lightweight passphrase dialog for OpenSSH or
other open variants of SSH. In particular, x11-ssh-askpass is useful
with the Unix port of OpenSSH by Damien Miller and others, and Damien
includes it in his RPM packages of OpenSSH.

x11-ssh-askpass uses only the stock X11 libraries (libX11, libXt) for
its user interface. This reduces its dependencies on external libraries
(such as GNOME or Perl/Tk). See the README for further information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build
env LDFLAGS='-Wl,--as-needed' %configure --libexecdir=%{_libexecdir}/openssh --with-app-defaults-dir=%{appdefaultsdir}
xmkmf
# Modernize the features.h macros
sed -i -e 's|-D_XOPEN_SOURCE||g' Makefile
sed -i -e 's|-D_BSD_SOURCE|-D_DEFAULT_SOURCE|g' Makefile
make includes
%make_build

%install
%make_install install.man DESTDIR=%{buildroot}

install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/%(basename %{SOURCE1})
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/%(basename %{SOURCE2})

rm -f %{buildroot}%{_libexecdir}/openssh/ssh-askpass
rm -f %{buildroot}%{_mandir}/man1/ssh-askpass.1x*

%files
%doc ChangeLog README TODO *.ad
%config(noreplace) %{_sysconfdir}/profile.d/x11-ssh-askpass.csh
%config(noreplace) %{_sysconfdir}/profile.d/x11-ssh-askpass.sh
%{appdefaultsdir}/SshAskpass
%dir %{_libexecdir}/openssh
%{_libexecdir}/openssh/x11-ssh-askpass
%{_mandir}/man1/x11-ssh-askpass.1x.gz

%changelog
%autochangelog
