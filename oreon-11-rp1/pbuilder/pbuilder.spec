%global source0_hash fc45535464761e0fc551a3997857603f4d36535efc0ec44c7b910aea9fa2d4a6

# https://bugzilla.redhat.com/show_bug.cgi?id=2414355
%global __brp_mangle_shebangs_exclude_from ^%{_prefix}/lib/pbuilder/pdebuild-internal$

Name:           pbuilder
Version:        0.231.3
Release:        2%{?dist}
Summary:        Personal package builder for Debian packages

License:        GPL-2.0-or-later
URL:            http://packages.debian.org/unstable/admin/%{name}
Source0:        http://ftp.debian.org/debian/pool/main/p/%{name}/%{name}_%{version}.tar.xz
Source1:        README.fedora
Source2:        https://bitbucket.org/amidevous/fedora-rpm/raw/master/pbuilder/debian/pbuilder-config
Source3:        https://bitbucket.org/amidevous/fedora-rpm/raw/master/pbuilder/debian/pbuilder-debian-stable
Source4:        https://bitbucket.org/amidevous/fedora-rpm/raw/master/pbuilder/debian/pbuilder-ubuntu-old
Source5:        https://bitbucket.org/amidevous/fedora-rpm/raw/master/pbuilder/debian/pbuilder-ubuntu-old2
Source6:        https://bitbucket.org/amidevous/fedora-rpm/raw/master/pbuilder/debian/pbuilder-ubuntu-stable
Source7:        https://bitbucket.org/amidevous/fedora-rpm/raw/master/pbuilder/debian/pbuilderrc
# Don't hardcode pbuilder user id, add a ccache section
Patch0:         pbuilder_pbuilderrc.patch
# Don't build HTML docs since it requires TLDP stylesheets which are not packaged for Fedora
Patch1:         pbuilder_no-html-docs.patch

BuildArch:      noarch

BuildRequires:  dblatex
BuildRequires:  dpkg-dev
BuildRequires:  make
BuildRequires:  man-db
BuildRequires:  python3
BuildRequires:  tex(fancybox.sty)
BuildRequires:  tex(pdflscape.sty)

#From https://salsa.debian.org/pbuilder-team/pbuilder/-/blob/master/debian/control
#Depends:
# debootstrap (>= 1.0.97) | cdebootstrap,
# dpkg-dev (>= 1.17.0),
# mount,
# ${misc:Depends},
#Recommends:
# devscripts,
# eatmydata,
# fakeroot,
# net-tools | iproute2,
# sudo,

Requires:       debootstrap
Requires:       dpkg-dev
Requires:       util-linux-core
Recommends:     devscripts
Recommends:     fakeroot
Recommends:     iproute
Recommends:     sudo
Requires:       gcc
Requires:       gnupg
Requires:       debconf
Requires:       debhelper
Requires:       wget
Requires:       debian-keyring
Requires:       ubu-keyring

%description
pbuilder constructs a chroot system, and builds a package inside the chroot.
It is an ideal system to use to check that a package has correct build-
dependencies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Adjust ccache path
sed -i 's|/usr/lib/ccache|%{_libdir}/ccache|g' pbuilderrc

# Create a sysusers.d config file
cat >pbuilder.sysusers.conf <<EOF
u pbuilder - '%{name}' %{_localstatedir}/run/%{name} -
EOF

%build
%make_build

%install
%make_install SBINDIR=%{buildroot}%{_bindir}

# Man pages
install -Dpm 0644 debuild-pbuilder.1 %{buildroot}%{_mandir}/man1/debuild-pbuilder.1
install -Dpm 0644 pdebuild.1 %{buildroot}%{_mandir}/man1/pdebuild.1
install -Dpm 0644 pbuilderrc.5 %{buildroot}%{_mandir}/man5/pbuilderrc.5
install -Dpm 0644 pbuilder.8 %{buildroot}%{_mandir}/man8/pbuilder.8

# Install directories
install -d %{buildroot}%{_localstatedir}/cache/%{name}
install -d %{buildroot}%{_localstatedir}/cache/%{name}/build
install -d %{buildroot}%{_localstatedir}/cache/%{name}/ccache
install -Dpm 0777 %{SOURCE2} %{buildroot}%{_bindir}/pbuilder-config
install -Dpm 0777 %{SOURCE3} %{buildroot}%{_bindir}/debian-stable
install -Dpm 0777 %{SOURCE4} %{buildroot}%{_bindir}/pbuilder-ubuntu-old
install -Dpm 0777 %{SOURCE5} %{buildroot}%{_bindir}/pbuilder-ubuntu-old2
install -Dpm 0777 %{SOURCE6} %{buildroot}%{_bindir}/pbuilder-ubuntu-stable

# Configuration file
install -Dpm 0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/pbuilderrc

# Copy README.fedora to root
cp -a %{SOURCE1} README.fedora

install -m0644 -D pbuilder.sysusers.conf %{buildroot}%{_sysusersdir}/pbuilder.conf

%check
%ifarch %arm
# Some tests fail on arm because ubuntu mirrors are unavailable for that arch
make check || :
%else
make check
%endif

%files
%doc README AUTHORS THANKS debian/TODO README.fedora
%config(noreplace) %{_sysconfdir}/pbuilderrc
%config(noreplace) %{_sysconfdir}/pbuilder/
%{_bindir}/debuild-pbuilder
%{_bindir}/pdebuild
%{_bindir}/pbuilder-config
%{_bindir}/debian-stable
%{_bindir}/pbuilder-ubuntu-old
%{_bindir}/pbuilder-ubuntu-old2
%{_bindir}/pbuilder-ubuntu-stable
%{_bindir}/pbuilder
%{_prefix}/lib/pbuilder/
%{_datadir}/bash-completion/
%{_datadir}/pbuilder/
%{_mandir}/man1/debuild-pbuilder.1*
%{_mandir}/man1/pdebuild.1*
%{_mandir}/man5/pbuilderrc.5*
%{_mandir}/man8/pbuilder.8*
%{_docdir}/pbuilder/*
# The ccache folder needs to be owned by the pbuilder user
%attr(0755,%{name},root) %{_localstatedir}/cache/%{name}/ccache
%{_sysusersdir}/pbuilder.conf

%changelog
%autochangelog
