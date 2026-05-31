%global source0_hash e13f4df8ad055c05bcca2226d92e298156eb9ea6de81415c844e567e4e7ab117

Name:       beakerlib
Summary:    A shell-level integration testing library
Version:    1.33.2
Release:    1%{?dist}
License:    GPL-2.0-only
BuildArch:  noarch
URL:        https://github.com/%{name}
Autoreq:    0
Requires:   nfs-utils
Requires:   /bin/bash
Requires:   /bin/sh
%if 0%{?fedora}
Recommends: /usr/bin/python3
%endif
%if 0%{?rhel} > 7
Recommends: /usr/libexec/platform-python
%else
# rhel <= 7
Requires:   /usr/bin/python
%endif
%if 0%{?rhel} >= 8 || 0%{?fedora}
# rhel >= 8 and fedora
Recommends: /usr/bin/perl
Requires:   (wget or curl)
Suggests:   wget
Recommends: python3-lxml
Recommends: python3-six
Recommends: /usr/bin/xmllint
%else
# rhel < 8
Requires:   /usr/bin/perl
Requires:   wget
Requires:   python-lxml
Requires:   /usr/bin/xmllint
%endif
Requires:   grep
Requires:   sed
Requires:   iproute
Requires:   coreutils
Requires:   tar
Requires:   gzip
Requires:   util-linux
Requires:   which
%if 0%{?fedora} || 0%{?rhel} >= 11
Requires:   dnf5-command(download)
Requires:   dnf5-command(repoquery)
%else
%if 0%{?rhel} >= 8
Requires:   dnf-command(download)
Requires:   dnf-command(repoquery)
%else
Requires:   yum-utils
%endif
%endif
Requires:   /usr/bin/bc
Requires:   /usr/bin/time
%if 0%{?rhel} < 8
%else
Recommends: beakerlib-redhat
%endif
Conflicts:  beakerlib-redhat < 1-30

BuildRequires: /usr/bin/pod2man
BuildRequires: perl-generators
BuildRequires: util-linux
BuildRequires: make

Source0:        https://github.com/beakerlib/beakerlib/archive/%{version}/%{name}-%{version}.tar.gz
Source1:    %{name}-tmpfiles.conf

Patch0: bugzilla-links.patch
Patch1: bugzilla-links-epel.patch
Patch2: python3.patch
Patch3: python-platform.patch

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -N
%if 0%{?fedora}
# Patch0: bugzilla-links.patch
%patch -P 0 -p1
%else
# rhel
# Patch1: bugzilla-links-epel.patch
%patch -P 1 -p1
%endif

%if 0%{?fedora}
# Patch2: python3.patch
%patch -P 2 -p1
%endif
%if 0%{?rhel} > 7
# Patch3: python-platform.patch
%patch -P 3 -p1
%endif


%build
make build

%install
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%{!?_tmpfilesdir: %global _tmpfilesdir %{_prefix}/lib/tmpfiles.d/}
rm -rf $RPM_BUILD_ROOT
make PKGDOCDIR=%{buildroot}/%{_pkgdocdir} DESTDIR=%{buildroot}/usr install
mkdir -p %{buildroot}/%{_tmpfilesdir}
install -m 0644 %{SOURCE1} %{buildroot}/%{_tmpfilesdir}/%{name}.conf

%description
The BeakerLib project means to provide a library of various helpers, which
could be used when writing operating system level integration tests.

%files
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/xslt-templates
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/examples
%dir %{_pkgdocdir}/examples/*
%{_datadir}/%{name}/dictionary.vim
%{_datadir}/%{name}/*.sh
%{_datadir}/%{name}/xslt-templates/*
%{_bindir}/%{name}-*
%{_mandir}/man1/%{name}*1*
%doc %{_pkgdocdir}/*
%config %{_tmpfilesdir}/%{name}.conf

%package vim-syntax
Summary: Files for syntax highlighting BeakerLib tests in VIM editor
Requires: vim-common
BuildRequires: vim-common
BuildRequires: make

%description vim-syntax
Files for syntax highlighting BeakerLib tests in VIM editor

%files vim-syntax
%{_datadir}/vim/vimfiles/after/ftdetect/beakerlib.vim
%{_datadir}/vim/vimfiles/after/syntax/beakerlib.vim

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.33.2-1
- Prepare for Oreon 11 (RP1)
