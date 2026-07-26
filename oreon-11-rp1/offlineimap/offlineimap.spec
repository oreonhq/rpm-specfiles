%global source0_hash ff4c63aaa17c540b056245720ac0114713c864709cc8801698be67e9aa4f3395

%global baserelease 2

#%%global commit 1e7ef9e7e6952f5d29ef0f5c25fd062798de55f3
#%%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global imaplib2_commit e969a3f37bf673502b0759c56d4d3ee380ec672b
%global imaplib2_shortcommit %(c=%{imaplib2_commit}; echo ${c:0:7})

Name:           offlineimap
Version:        8.0.1
Release:        %{baserelease}%{?dist}
Summary:        Powerful IMAP/Maildir synchronization and reader support

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.offlineimap.org/
#Source0:        https://github.com/OfflineIMAP/offlineimap3/archive/%{commit}/offlineimap3-%{shortcommit}.tar.gz
Source0:        https://github.com/OfflineIMAP/offlineimap3/archive/refs/tags/v%{version}.tar.gz

Source3:        https://github.com/jazzband/imaplib2/archive/%{imaplib2_commit}/imaplib2-%{imaplib2_shortcommit}.tar.gz

Patch0:         0001-PATCH-Vendor-imaplib2.patch
Patch1:         0002-PATCH-no-eyeballs.patch
Patch3:         0003-PATCH-Sphinx-doc-compat.patch
Patch4:         0004-PATCH-Loosen-urllib3-requirements.patch

# Patches for imaplib2, keep the numbers above 200
Patch201:       https://github.com/jazzband/imaplib2/pull/4.patch
Patch202:       https://github.com/jazzband/imaplib2/pull/6.patch
Patch203:       https://github.com/jazzband/imaplib2/pull/15.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-distro
BuildRequires:  python3-sphinx
BuildRequires:  asciidoc
BuildRequires:  make
BuildRequires:  gzip

Requires: sqlite
Requires: python3-distro
Provides: offlineimap3 = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: bundled(python3dist(imaplib2))

%description
OfflineIMAP is a tool to simplify your e-mail reading. With OfflineIMAP,
you can read the same mailbox from multiple computers.  You get a
current copy of your messages on each computer, and changes you make one
place will be visible on all other systems. For instance, you can delete
a message on your home computer, and it will appear deleted on your work
computer as well. OfflineIMAP is also useful if you want to use a mail
reader that does not have IMAP support, has poor IMAP support, or does
not provide disconnected operation.

%generate_buildrequires
%pyproject_buildrequires

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

# 'make docs' builds the man pages and the api documentation.
make docs SPHINXBUILD='%{__python3} -msphinx'
gzip -c docs/offlineimap.1 > docs/offlineimap.1.gz
gzip -c docs/offlineimapui.7 > docs/offlineimapui.7.gz
chmod a-x docs/offlineimap.1.gz
chmod a-x docs/offlineimapui.7.gz

%install

%pyproject_install

#  Fix python shebang in the offlineimap program.
%py3_shebang_fix %{buildroot}/%{_bindir}/offlineimap

mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_mandir}/man7
install -p docs/offlineimap.1.gz %{buildroot}/%{_mandir}/man1/
install -p docs/offlineimapui.7.gz %{buildroot}/%{_mandir}/man7/

%check

./offlineimap.py -V

%files
%license COPYING
%doc offlineimap.conf* docs/html/*.html
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}.dist-info/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man7/%{name}ui.7*

%changelog
%autochangelog
