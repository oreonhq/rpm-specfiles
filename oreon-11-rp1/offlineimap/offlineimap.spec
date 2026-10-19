%global source3_hash ff4c63aaa17c540b056245720ac0114713c864709cc8801698be67e9aa4f3395
%global source0_hash 967a8ca24e5f665cd22941ba1173db10cbd908085ec22ab9b0e4a64c94007d85
%global baserelease 2
%global imaplib2_commit e969a3f37bf673502b0759c56d4d3ee380ec672b
%global imaplib2_shortcommit %(c=%{imaplib2_commit}; echo ${c:0:7})
Name:           offlineimap
Version:        8.0.3
Release:        2%{?dist}
Summary:        Powerful IMAP/Maildir synchronization and reader support
License:        GPL-2.0-or-later
URL:            https://www.offlineimap.org/
Source0:        https://github.com/OfflineIMAP/offlineimap3/archive/refs/tags/v%{version}.tar.gz
Source3:        https://github.com/jazzband/imaplib2/archive/%{imaplib2_commit}/imaplib2-%{imaplib2_shortcommit}.tar.gz
Patch0:         0001-PATCH-Vendor-imaplib2.patch
Patch1:         0002-PATCH-no-eyeballs.patch
Patch3:         0003-PATCH-Sphinx-doc-compat.patch
Patch4:         0004-PATCH-Loosen-urllib3-requirements.patch
Patch201:       https://github.com/jazzband/imaplib2/pull/4.patch
Patch202:       https://github.com/jazzband/imaplib2/pull/6.patch
Patch203:       https://github.com/jazzband/imaplib2/pull/15.patch
BuildArch:      noarch
Requires: sqlite
Requires: python3-distro
Provides: offlineimap3 = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: bundled(python3dist(imaplib2))
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 18.5
Requires:       python3-offlineimap = %{version}-%{release}
# /oreon:deps
%package -n       python3-offlineimap+cygwin
Summary:        Metapackage for python3-offlineimap cygwin extras
Requires:       python3-offlineimap = %{version}-%{release}
Provides:       python3dist(offlineimap[cygwin]) = %{version}-%{release}

%description -n python3-offlineimap+cygwin
Metapackage for python3-offlineimap cygwin extras.

%package -n       python3-offlineimap+kerberos
Summary:        Metapackage for python3-offlineimap kerberos extras
Requires:       python3-offlineimap = %{version}-%{release}
Provides:       python3dist(offlineimap[kerberos]) = %{version}-%{release}

%description -n python3-offlineimap+kerberos
Metapackage for python3-offlineimap kerberos extras.

%package -n       python3-offlineimap+keyring
Summary:        Metapackage for python3-offlineimap keyring extras
Requires:       python3-offlineimap = %{version}-%{release}
Provides:       python3dist(offlineimap[keyring]) = %{version}-%{release}

%description -n python3-offlineimap+keyring
Metapackage for python3-offlineimap keyring extras.

%package -n       python3-offlineimap+pysocks
Summary:        Metapackage for python3-offlineimap pysocks extras
Requires:       python3-offlineimap = %{version}-%{release}
Provides:       python3dist(offlineimap[pysocks]) = %{version}-%{release}

%description -n python3-offlineimap+pysocks
Metapackage for python3-offlineimap pysocks extras.

%package -n       python3-offlineimap+testinternet
Summary:        Metapackage for python3-offlineimap testinternet extras
Requires:       python3-offlineimap = %{version}-%{release}
Requires:       python3dist(certifi) >= 2020.6.20
Requires:       python3dist(urllib3) >= 1.25.9
Provides:       python3dist(offlineimap[testinternet]) = %{version}-%{release}

%description -n python3-offlineimap+testinternet
Metapackage for python3-offlineimap testinternet extras.

%description
OfflineIMAP is a tool to simplify your e-mail reading. With OfflineIMAP,
you can read the same mailbox from multiple computers.  You get a
current copy of your messages on each computer, and changes you make one
place will be visible on all other systems. For instance, you can delete
a message on your home computer, and it will appear deleted on your work
computer as well. OfflineIMAP is also useful if you want to use a mail
reader that does not have IMAP support, has poor IMAP support, or does
not provide disconnected operation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n offlineimap3-%{version}
%autopatch -M200 -p1

# bundle imaplib2, patched version
cd ..
tar xf %{SOURCE3}
cd imaplib2-%{imaplib2_commit}
%autopatch -m200 -p1
mv imaplib2/imaplib2.py3 ../offlineimap3-%{version}/offlineimap/imaplib2.py

%build

%pyproject_wheel
make docs SPHINXBUILD='%{__python3} -msphinx'
gzip -c docs/offlineimap.1 > docs/offlineimap.1.gz
gzip -c docs/offlineimapui.7 > docs/offlineimapui.7.gz
chmod a-x docs/offlineimap.1.gz
chmod a-x docs/offlineimapui.7.gz
%install
%pyproject_install
%py3_shebang_fix %{buildroot}/%{_bindir}/offlineimap
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_mandir}/man7
install -p docs/offlineimap.1.gz %{buildroot}/%{_mandir}/man1/
install -p docs/offlineimapui.7.gz %{buildroot}/%{_mandir}/man7/
%oreon_autofiles main

%check

./offlineimap.py -V
%files

%changelog

%autochangelog
