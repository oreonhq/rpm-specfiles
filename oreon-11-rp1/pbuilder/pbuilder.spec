%global source7_hash 8ee9ea9d37b271a3e02f7dc9383432caa050dbb69479e1b35c234bb6e2026157
%global source6_hash d2be31aae85e7398fd7d73062b89f8bf25fec15f8c17dd05fc8cdf140fe7486e
%global source5_hash 9af12fec6edd643b894b52aee5bd0f3298a7008e05f59da9af995bcb36e91c16
%global source4_hash 53d33d10f25a8f83db2133bdc999b44336473cadb2703f3e92ccac3730500f2e
%global source3_hash 4a899efd65e92f7c839f307bf3080e8ab8ef7520cedb152ff7890f49fcdd38ff
%global source2_hash daf4962fb5539a8a33b24c8809a4d159d0edca31f8195b9229eb6b8ec23989b6
%global source0_hash fc45535464761e0fc551a3997857603f4d36535efc0ec44c7b910aea9fa2d4a6
%global __brp_mangle_shebangs_exclude_from ^%{_prefix}/lib/pbuilder/pdebuild-internal$
Name:           pbuilder
Version:        0.231.3
Release:        1%{?dist}
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
Patch0:         pbuilder_pbuilderrc.patch
Patch1:         pbuilder_no-html-docs.patch
BuildArch:      noarch
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
# oreon:deps
BuildRequires:  dblatex
BuildRequires:  dpkg-dev
BuildRequires:  make
BuildRequires:  man-db
BuildRequires:  python3
BuildRequires:  tex(fancybox.sty)
BuildRequires:  tex(pdflscape.sty)
# /oreon:deps
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
install -Dpm 0644 debuild-pbuilder.1 %{buildroot}%{_mandir}/man1/debuild-pbuilder.1
install -Dpm 0644 pdebuild.1 %{buildroot}%{_mandir}/man1/pdebuild.1
install -Dpm 0644 pbuilderrc.5 %{buildroot}%{_mandir}/man5/pbuilderrc.5
install -Dpm 0644 pbuilder.8 %{buildroot}%{_mandir}/man8/pbuilder.8
install -d %{buildroot}%{_localstatedir}/cache/%{name}
install -d %{buildroot}%{_localstatedir}/cache/%{name}/build
install -d %{buildroot}%{_localstatedir}/cache/%{name}/ccache
install -Dpm 0777 %{SOURCE2} %{buildroot}%{_bindir}/pbuilder-config
install -Dpm 0777 %{SOURCE3} %{buildroot}%{_bindir}/debian-stable
install -Dpm 0777 %{SOURCE4} %{buildroot}%{_bindir}/pbuilder-ubuntu-old
install -Dpm 0777 %{SOURCE5} %{buildroot}%{_bindir}/pbuilder-ubuntu-old2
install -Dpm 0777 %{SOURCE6} %{buildroot}%{_bindir}/pbuilder-ubuntu-stable
install -Dpm 0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/pbuilderrc
cp -a %{SOURCE1} README.fedora
install -m0644 -D pbuilder.sysusers.conf %{buildroot}%{_sysusersdir}/pbuilder.conf
%oreon_autofiles main

%check

%ifarch %arm
make check || :
%else
make check
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
