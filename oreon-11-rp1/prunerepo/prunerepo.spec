%global source0_hash e8a539387c14b9ee452596e5846b58721c38d6d70051b6c600f8fc4f7843e80d

Name:    prunerepo
Version: 1.26
Summary: Remove old packages from rpm-md repository
Release: 6%{?dist}
Url: https://pagure.io/prunerepo

%if 0%{?rhel} > 10 || 0%{?fedora} > 40
%bcond_without dnf5
%else
%bcond_with dnf5
%endif

# Source is created by:
# git clone %%url && cd prunerepo
# tito build --tgz --tag %%name-%%version-%%release
Source0: %name-%version.tar.gz

License: GPL-2.0-or-later
BuildArch: noarch
BuildRequires: bash
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-rpm
BuildRequires: createrepo_c
BuildRequires: asciidoc
BuildRequires: findutils
%if %{with dnf5}
BuildRequires: dnf5-command(repoquery)
BuildRequires: python3-libdnf5
Requires: dnf5-command(repoquery)
%else
BuildRequires: dnf-command(repoquery)
BuildRequires: dnf-plugins-core
Requires: dnf-command(repoquery)
# F40 needs this explicit requirement
Requires: /usr/bin/dnf
BuildRequires: /usr/bin/dnf
%endif
BuildRequires: coreutils
Requires: createrepo_c
Requires: python3-rpm
Requires: python3

%description
RPM packages that have newer version available in that same
repository are deleted from filesystem and the rpm-md metadata are
recreated afterwards. If there is a source rpm for a deleted rpm
(and they both share the same directory path), then the source rpm
will be deleted as well.

Support for specific repository structure (e.g. COPR) is also available
making it possible to additionally remove build logs and whole build
directories associated with a package.

After deletion of obsoleted packages, the command
"createrepo_c --database --update" is called
to recreate the repository metadata.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%check
tests/run.sh

%build
name="%{name}" version="%{version}" summary="%{summary}" %py3_build
a2x -d manpage -f manpage man/prunerepo.1.asciidoc

%install
name="%{name}" version="%{version}" summary="%{summary}" %py3_install

install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/prunerepo.1 %{buildroot}/%{_mandir}/man1/

%files
%license LICENSE

%{python3_sitelib}/*
%{_bindir}/prunerepo
%{_mandir}/man1/prunerepo.1*

%changelog
%autochangelog
