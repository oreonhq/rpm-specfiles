%global source0_hash 533d62ce9923b8ada7f138ac4bf298e62806ce678cd61499a7c131505c1ba3ec

Name:           pungi
Version:        4.10.1
Release:        5%{?dist}
Summary:        Distribution compose tool

License:        GPL-2.0-only
URL:            https://pagure.io/pungi
Source0:        https://pagure.io/releases/%{name}/%{name}-%{version}.tar.bz2
Patch:          https://pagure.io/pungi/pull-request/1860.patch
# https://pagure.io/pungi/pull-request/1885
Patch:          0001-Drop-parameterized-dependency.patch

BuildRequires:  make
BuildRequires:  python3-pytest
BuildRequires:  python3-devel
BuildRequires:  python3-kobo-rpmlib
BuildRequires:  createrepo_c
BuildRequires:  python3-kickstart
BuildRequires:  python3-rpm
BuildRequires:  python3-dnf
BuildRequires:  python3-multilib
BuildRequires:  python3-six
BuildRequires:  git-core
BuildRequires:  python3-libcomps
BuildRequires:  python3-koji
BuildRequires:  lorax
BuildRequires:  python3-PyYAML
BuildRequires:  python3-libmodulemd >= 2.8.0
BuildRequires:  python3-gobject
BuildRequires:  python3-createrepo_c
BuildRequires:  python3-flufl-lock

#deps for doc building
BuildRequires:  python3-sphinx

Requires:       python3-kobo-rpmlib
Requires:       python3-kickstart
Requires:       createrepo_c
Requires:       koji >= 1.10.1-13
Requires:       python3-koji-cli-plugins
Requires:       isomd5sum
Requires:       genisoimage
Requires:       git
Requires:       python3-dnf
Requires:       python3-multilib
Requires:       python3-libcomps
Requires:       python3-koji
Requires:       python3-libmodulemd >= 2.8.0
Requires:       python3-gobject
Requires:       python3-createrepo_c
Requires:       python3-PyYAML
Requires:       python3-flufl-lock
Requires:       xorriso

# This package is not available on i686, hence we cannot require it
# See https://bugzilla.redhat.com/show_bug.cgi?id=1743421
Recommends:     libguestfs-tools-c

Requires:       python3-%{name} = %{version}-%{release}

BuildArch:      noarch

%description
A tool to create anaconda based installation trees/isos of a set of rpms.

%package utils
Summary:    Utilities for working with finished composes
Requires:   pungi = %{version}-%{release}
Requires:   python3-fedora-messaging

%description utils
These utilities work with finished composes produced by Pungi. They can be used
for creating unified ISO images, validating config file or sending progress
notification to Fedora Message Bus.

%package -n python3-%{name}
Summary:    Python 3 libraries for pungi

%description -n python3-%{name}
Python library with code for Pungi. This is not a public library and there are
no guarantees about API stability.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
cd doc
make epub     SPHINXBUILD=/usr/bin/sphinx-build-3
make text     SPHINXBUILD=/usr/bin/sphinx-build-3
make man      SPHINXBUILD=/usr/bin/sphinx-build-3
gzip _build/man/pungi.1

%install
%pyproject_install
%{__install} -d %{buildroot}/var/cache/pungi/createrepo_c
%{__install} -d %{buildroot}%{_mandir}/man1
%{__install} -m 0644 doc/_build/man/pungi.1.gz %{buildroot}%{_mandir}/man1

%check
%pytest

%files
%license COPYING GPL
%doc AUTHORS
%doc doc/_build/epub/Pungi.epub doc/_build/text/*
%{_bindir}/%{name}-koji
%{_bindir}/%{name}-gather
%{_bindir}/comps_filter
%{_bindir}/%{name}-make-ostree
%{_mandir}/man1/pungi.1.gz
%{_datadir}/pungi
%dir %{_localstatedir}/cache/pungi
%dir %attr(1777, root, root) %{_localstatedir}/cache/pungi/createrepo_c
%{_tmpfilesdir}/pungi-clean-cache.conf

%files -n python3-%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}.dist-info

%files utils
%{python3_sitelib}/%{name}_utils
%{_bindir}/%{name}-create-unified-isos
%{_bindir}/%{name}-config-dump
%{_bindir}/%{name}-config-validate
%{_bindir}/%{name}-fedmsg-notification
%{_bindir}/%{name}-notification-report-progress
%{_bindir}/%{name}-patch-iso
%{_bindir}/%{name}-compare-depsolving
%{_bindir}/%{name}-wait-for-signed-ostree-handler
%{_bindir}/%{name}-cache-cleanup

%changelog
%autochangelog
